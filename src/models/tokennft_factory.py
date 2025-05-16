from src.models.tokennft import TokenNFT
import uuid

class TokenNFTFactory:
    @staticmethod
    def create_token(tipo, poll_id, option, date, owner, **kwargs):
        if tipo == 'estandar':
            return TokenNFT(str(uuid.uuid4()), poll_id, option, date, owner)
        if tipo == 'edicion_limitada':
            token = TokenNFT(str(uuid.uuid4()), poll_id, option, date, owner)
            token.limited = True
            token.edition = kwargs.get('edition', 1)
            return token
        return TokenNFT(str(uuid.uuid4()), poll_id, option, date, owner)
