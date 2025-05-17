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
        def registrar_usuario(username, password):
            user = self.user_service.register(username, password)
            if user:
                return 'Usuario registrado correctamente'
            return 'El usuario ya existe'
        def ver_usuarios():
            users = self.user_service.user_repo.get_users()
            if not users:
                return []
            # Solo mostrar username
            return [[u['username']] for u in users]
        def crear_encuesta(pregunta, opciones, duracion):
            opciones_list = [o.strip() for o in opciones.split(',') if o.strip()]
            poll_id = str(len(self.poll_service.encuesta_repo.get_polls_json()) + 1)
            poll = self.poll_service.create_poll(poll_id, pregunta, opciones_list, duracion)
            if poll:
                return f'Encuesta creada: {poll.question}'
            return 'Error al crear la encuesta'
        def votar(poll_id, username, opcion):
            return self.poll_service.vote(poll_id, username, opcion)
        def ver_encuestas():
            polls = self.poll_service.encuesta_repo.get_polls_json()
            if not polls:
                return []
            # Mostrar solo columnas relevantes
            return [[p['id'], p['question'], ', '.join(p['options']), p['state']] for p in polls]
        def chat(mensaje):
            return self.chatbot_service.respond(mensaje)
        def ver_tokens(username):
            tokens = self.nft_service.nft_repo.get_tokens()
            return [t for t in tokens if t['owner'] == username]
        def transferir(token_id, nuevo_owner):
            self.nft_service.transfer_token(token_id, nuevo_owner)
            return 'Transferido'
        with gr.Blocks() as demo:
            gr.Markdown('### Registro de usuario')
            reg_username = gr.Textbox(label='Nombre de usuario')
            reg_password = gr.Textbox(label='Contraseña', type='password')
            reg_btn = gr.Button('Registrar')
            reg_out = gr.Textbox(label='Estado de registro')
            reg_btn.click(registrar_usuario, [reg_username, reg_password], reg_out)
            gr.Markdown('#### Usuarios registrados')
            users_out = gr.Dataframe(ver_usuarios, headers=["Usuario"], label='Usuarios')
            gr.Markdown('---')
            gr.Markdown('### Crear nueva encuesta')
            pregunta = gr.Textbox(label='Pregunta de la encuesta')
            opciones = gr.Textbox(label='Opciones (separadas por coma)')
            duracion = gr.Number(label='Duración (minutos)', value=5)
            crear_btn = gr.Button('Crear encuesta')
            crear_out = gr.Textbox(label='Estado de creación')
            crear_btn.click(crear_encuesta, [pregunta, opciones, duracion], crear_out)
            gr.Markdown('---')
            gr.Markdown('### Encuestas activas')
            encuestas = gr.Dataframe(ver_encuestas, headers=["ID", "Pregunta", "Opciones", "Estado"], label='Encuestas')
            poll_id = gr.Textbox(label='ID Encuesta')
            username = gr.Textbox(label='Usuario')
            opcion = gr.Textbox(label='Opción')
            votar_btn = gr.Button('Votar')
            votar_btn.click(votar, [poll_id, username, opcion], None)
            gr.Markdown('---')
            gr.Markdown('### Chatbot')
            chat_in = gr.Textbox(label='Mensaje')
            chat_out = gr.Textbox(label='Respuesta')
            chat_btn = gr.Button('Enviar')
            chat_btn.click(chat, chat_in, chat_out)
            gr.Markdown('---')
            gr.Markdown('### Tus Tokens')
            user_token = gr.Textbox(label='Usuario')
            tokens_out = gr.Dataframe(label='Tokens')
            def actualizar_tokens(username):
                tokens = ver_tokens(username)
                return tokens
            user_token.change(actualizar_tokens, inputs=user_token, outputs=tokens_out)
            token_id = gr.Textbox(label='ID Token')
            nuevo_owner = gr.Textbox(label='Nuevo Dueño')
            transfer_btn = gr.Button('Transferir')
            transfer_btn.click(transferir, [token_id, nuevo_owner], None)
        demo.launch(server_port=7860, share=True)
