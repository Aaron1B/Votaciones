import gradio as gr
from src.services.poll_service import PollService
from src.services.user_service import UserService
from src.services.nft_service import NFTService
from src.services.chatbot_service import ChatbotService

class GradioUI:
    def __init__(self, poll_service: PollService, user_service: UserService, nft_service: NFTService, chatbot_service: ChatbotService):
        self.poll_service = poll_service
        self.user_service = user_service
        self.nft_service = nft_service
        self.chatbot_service = chatbot_service

    def launch(self):
        gr.close_all()
        def votar(poll_id, username, opcion):
            return self.poll_service.vote(poll_id, username, opcion)
        def ver_encuestas():
            return self.poll_service.encuesta_repo.get_polls_json()
        def chat(mensaje):
            return self.chatbot_service.respond(mensaje)
        def ver_tokens(username):
            tokens = self.nft_service.nft_repo.get_tokens()
            return [t for t in tokens if t['owner'] == username]
        def transferir(token_id, nuevo_owner):
            self.nft_service.transfer_token(token_id, nuevo_owner)
            return 'Transferido'
        with gr.Blocks() as demo:
            with gr.Tab('Encuestas'):
                gr.Markdown('### Encuestas activas')
                encuestas = gr.Dataframe(ver_encuestas, label='Encuestas')
                poll_id = gr.Textbox(label='ID Encuesta')
                username = gr.Textbox(label='Usuario')
                opcion = gr.Textbox(label='Opción')
                votar_btn = gr.Button('Votar')
                votar_btn.click(votar, [poll_id, username, opcion], None)
            with gr.Tab('Chatbot'):
                gr.Markdown('### Chatbot')
                chat_in = gr.Textbox(label='Mensaje')
                chat_out = gr.Textbox(label='Respuesta')
                chat_btn = gr.Button('Enviar')
                chat_btn.click(chat, chat_in, chat_out)
            with gr.Tab('Tokens'):
                gr.Markdown('### Tus Tokens')
                user_token = gr.Textbox(label='Usuario')
                tokens_out = gr.Dataframe(ver_tokens, user_token, label='Tokens')
                token_id = gr.Textbox(label='ID Token')
                nuevo_owner = gr.Textbox(label='Nuevo Dueño')
                transfer_btn = gr.Button('Transferir')
                transfer_btn.click(transferir, [token_id, nuevo_owner], None)
        demo.launch(server_port=7860, share=True)
