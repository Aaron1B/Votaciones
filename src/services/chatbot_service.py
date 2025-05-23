class ChatbotService:
    def __init__(self, poll_service):
        self.poll_service = poll_service

    def respond(self, message):
        if 'estado' in message:
            return 'Consulta de estado de encuestas no implementada.'
        return 'Respuesta generada por IA simulada.'
