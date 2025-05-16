import json
import os
import sqlite3
from src.models.poll import Poll
from src.models.vote import Vote

class EncuestaRepository:
    def __init__(self, db_path=None, json_path=None):
        self.db_path = db_path
        self.json_path = json_path

    def save_poll_json(self, poll):
        data = poll.__dict__
        if not os.path.exists(self.json_path):
            with open(self.json_path, 'w') as f:
                json.dump([data], f)
        else:
            with open(self.json_path, 'r+') as f:
                polls = json.load(f)
                polls.append(data)
                f.seek(0)
                json.dump(polls, f)

    def get_polls_json(self):
        if not os.path.exists(self.json_path):
            return []
        with open(self.json_path, 'r') as f:
            return json.load(f)

    def save_vote_json(self, vote):
        vote_data = vote.__dict__
        votes_path = self.json_path.replace('polls', 'votes')
        if not os.path.exists(votes_path):
            with open(votes_path, 'w') as f:
                json.dump([vote_data], f)
        else:
            with open(votes_path, 'r+') as f:
                votes = json.load(f)
                votes.append(vote_data)
                f.seek(0)
                json.dump(votes, f)

    def get_votes_json(self):
        votes_path = self.json_path.replace('polls', 'votes')
        if not os.path.exists(votes_path):
            return []
        with open(votes_path, 'r') as f:
            return json.load(f)
