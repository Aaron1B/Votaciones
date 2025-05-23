from src.repositories.nft_repository import NFTRepository
from src.models.tokennft import TokenNFT
import datetime
import uuid
import json

class NFTService:
    def __init__(self, nft_repo: NFTRepository):
        self.nft_repo = nft_repo

    def generate_token(self, poll_id, option, owner, amount=1):
        token_id = str(uuid.uuid4())
        date = datetime.datetime.now().isoformat()
        token = TokenNFT(token_id, poll_id, option, date, owner)
        token.amount = amount
        self.nft_repo.save_token(token)
        return token

    def transfer_token(self, token_id, new_owner):
        tokens = self.nft_repo.get_tokens()
        for t in tokens:
            if t['id'] == token_id:
                t['owner'] = new_owner
        with open(self.nft_repo.json_path, 'w') as f:
            json.dump(tokens, f)

    def get_tokens_by_user(self, username):
        tokens = self.nft_repo.get_tokens()
        return [t for t in tokens if t['owner'] == username]

    def get_all_tokens(self):
        return self.nft_repo.get_tokens()

    def transfer_tokens(self, from_user, to_user, amount):
        tokens = self.nft_repo.get_tokens()
        user_tokens = [t for t in tokens if t['owner'] == from_user]
        transferred = 0
        for t in user_tokens:
            if transferred >= amount:
                break
            t['owner'] = to_user
            transferred += 1
        with open(self.nft_repo.json_path, 'w') as f:
            json.dump(tokens, f)
        return transferred
