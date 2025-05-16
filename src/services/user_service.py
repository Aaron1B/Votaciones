from src.repositories.usuario_repository import UsuarioRepository
from src.models.user import User
import hashlib

class UserService:
    def __init__(self, user_repo: UsuarioRepository):
        self.user_repo = user_repo

    def register(self, username, password):
        users = self.user_repo.get_users()
        if any(u['username'] == username for u in users):
            return None
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = User(username, password_hash)
        self.user_repo.save_user(user)
        return user

    def login(self, username, password):
        users = self.user_repo.get_users()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        user = next((u for u in users if u['username'] == username and u['password_hash'] == password_hash), None)
        return user

    def can_vote(self, username):
        users = self.user_repo.get_users()
        user = next((u for u in users if u['username'] == username), None)
        return user is not None
