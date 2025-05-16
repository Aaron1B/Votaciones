import json
import os
from src.models.user import User

class UsuarioRepository:
    def __init__(self, json_path):
        self.json_path = json_path

    def save_user(self, user):
        data = user.__dict__
        if not os.path.exists(self.json_path):
            with open(self.json_path, 'w') as f:
                json.dump([data], f)
        else:
            with open(self.json_path, 'r+') as f:
                users = json.load(f)
                users.append(data)
                f.seek(0)
                json.dump(users, f)

    def get_users(self):
        if not os.path.exists(self.json_path):
            return []
        with open(self.json_path, 'r') as f:
            return json.load(f)
