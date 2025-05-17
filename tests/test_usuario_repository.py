import unittest
import os
from src.repositories.usuario_repository import UsuarioRepository
from src.models.user import User

class TestUsuarioRepository(unittest.TestCase):
    def setUp(self):
        self.test_file = 'tests/test_users.json'
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        self.repo = UsuarioRepository(self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_get_user(self):
        user = User('testuser', 'hash')
        self.repo.save_user(user)
        users = self.repo.get_users()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0]['username'], 'testuser')

if __name__ == '__main__':
    unittest.main()
