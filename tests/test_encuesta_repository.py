import unittest
import os
from src.repositories.encuesta_repository import EncuestaRepository
from src.models.poll import Poll
from src.models.vote import Vote

class TestEncuestaRepository(unittest.TestCase):
    def setUp(self):
        self.test_file = 'tests/test_polls.json'
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.repo = EncuestaRepository(json_path=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_poll(self):
        poll = Poll('1', 'Pregunta?', ['a', 'b'], 5)
        self.repo.save_poll_json(poll)
        polls = self.repo.get_polls_json()
        self.assertEqual(len(polls), 1)
        self.assertEqual(polls[0]['question'], 'Pregunta?')

    def test_save_and_get_vote(self):
        vote = Vote('user1', '1', 'a')
        self.repo.save_vote_json(vote)
        votes = self.repo.get_votes_json()
        self.assertEqual(len(votes), 1)
        self.assertEqual(votes[0]['user_id'], 'user1')

if __name__ == '__main__':
    unittest.main()
