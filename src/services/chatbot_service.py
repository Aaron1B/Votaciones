from transformers import pipeline

class ChatbotService:
    def __init__(self, poll_service):
        self.poll_service = poll_service
        self.chatbot = pipeline('text-generation', model='gpt2')

    def respond(self, message):
        if 'estado' in message:
            return 'Consulta de estado de encuestas no implementada.'
        response = self.chatbot(message, max_length=60, num_return_sequences=1)
        return response[0]['generated_text']
