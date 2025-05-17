import sys
from src.repositories.encuesta_repository import EncuestaRepository
from src.repositories.usuario_repository import UsuarioRepository
from src.repositories.nft_repository import NFTRepository
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService
from src.controllers.cli_controller import CLIController
from src.ui.gradio_ui import GradioUI

PORT = 7860
POLL_JSON = 'polls.json'
USER_JSON = 'users.json'
NFT_JSON = 'nfts.json'

encuesta_repo = EncuestaRepository(json_path=POLL_JSON)
usuario_repo = UsuarioRepository(json_path=USER_JSON)
nft_repo = NFTRepository(json_path=NFT_JSON)
poll_service = PollService(encuesta_repo, usuario_repo, nft_repo)
user_service = UserService(usuario_repo)
nft_service = NFTService(nft_repo)
chatbot_service = ChatbotService(poll_service)

cli = CLIController(poll_service, user_service, nft_service)
ui = GradioUI(poll_service, user_service, nft_service, chatbot_service)

def main():
    if '--ui' in sys.argv or len(sys.argv) == 1:
        try:
            ui.launch()
        except Exception as e:
            print('Error al lanzar Gradio:', e)
    else:
        cli.run()

if __name__ == '__main__':
    main()
