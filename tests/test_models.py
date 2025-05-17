import unittest
from src.models.poll import Poll
from src.models.vote import Vote
from src.models.user import User
from src.models.tokennft import TokenNFT

class TestModels(unittest.TestCase):
    def test_poll(self):
        poll = Poll('1', 'Pregunta?', ['a', 'b'], 5)
        self.assertEqual(poll.id, '1')
        self.assertEqual(poll.question, 'Pregunta?')
        self.assertEqual(poll.options, ['a', 'b'])
        self.assertEqual(poll.duration, 5)
        self.assertEqual(poll.state, 'active')

    def test_vote(self):
        vote = Vote('user1', '1', 'a')
        self.assertEqual(vote.user_id, 'user1')
        self.assertEqual(vote.poll_id, '1')
        self.assertEqual(vote.option, 'a')

    def test_user(self):
        user = User('test', 'hash')
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.password_hash, 'hash')
        self.assertEqual(user.tokens, [])

    def test_tokennft(self):
        token = TokenNFT('id', 'poll', 'a', 'date', 'owner')
        self.assertEqual(token.id, 'id')
        self.assertEqual(token.poll_id, 'poll')
        self.assertEqual(token.option, 'a')
        self.assertEqual(token.date, 'date')
        self.assertEqual(token.owner, 'owner')

if __name__ == '__main__':
    unittest.main()
