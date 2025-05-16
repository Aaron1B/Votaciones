from src.repositories.encuesta_repository import EncuestaRepository
from src.repositories.usuario_repository import UsuarioRepository
from src.repositories.nft_repository import NFTRepository
from src.models.poll import Poll
from src.models.vote import Vote
import datetime
import json

class PollService:
    def __init__(self, encuesta_repo: EncuestaRepository, user_repo: UsuarioRepository, nft_repo: NFTRepository):
        self.encuesta_repo = encuesta_repo
        self.user_repo = user_repo
        self.nft_repo = nft_repo

    def create_poll(self, id, question, options, duration):
        poll = Poll(id, question, options, duration)
        poll.created_at = datetime.datetime.now().isoformat()
        self.encuesta_repo.save_poll_json(poll)
        return poll

    def vote(self, poll_id, user_id, option):
        polls = self.encuesta_repo.get_polls_json()
        poll = next((p for p in polls if p['id'] == poll_id), None)
        if not poll or poll['state'] != 'active':
            return None
        votes = self.encuesta_repo.get_votes_json()
        if any(v['user_id'] == user_id and v['poll_id'] == poll_id for v in votes):
            return None
        vote = Vote(user_id, poll_id, option)
        self.encuesta_repo.save_vote_json(vote)
        return vote

    def close_poll(self, poll_id):
        polls = self.encuesta_repo.get_polls_json()
        for p in polls:
            if p['id'] == poll_id:
                p['state'] = 'closed'
                p['closed_at'] = datetime.datetime.now().isoformat()
        with open(self.encuesta_repo.json_path, 'w') as f:
            json.dump(polls, f)

    def get_results(self, poll_id):
        votes = self.encuesta_repo.get_votes_json()
        poll_votes = [v for v in votes if v['poll_id'] == poll_id]
        results = {}
        for v in poll_votes:
            results[v['option']] = results.get(v['option'], 0) + 1
        max_votes = max(results.values(), default=0)
        winners = [k for k, v in results.items() if v == max_votes]
        return {'results': results, 'winners': winners}
