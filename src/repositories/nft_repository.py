import json
import os
from src.models.tokennft import TokenNFT

class NFTRepository:
    def __init__(self, json_path):
        self.json_path = json_path

    def save_token(self, token):
        data = token.__dict__
        if not os.path.exists(self.json_path):
            with open(self.json_path, 'w') as f:
                json.dump([data], f)
        else:
            with open(self.json_path, 'r+') as f:
                tokens = json.load(f)
                tokens.append(data)
                f.seek(0)
                json.dump(tokens, f)

    def get_tokens(self):
        if not os.path.exists(self.json_path):
            return []
        with open(self.json_path, 'r') as f:
            return json.load(f)
