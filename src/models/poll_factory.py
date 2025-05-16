from src.models.poll import Poll

class PollFactory:
    @staticmethod
    def create_poll(tipo, id, question, options, duration, **kwargs):
        if tipo == 'simple':
            return Poll(id, question, options, duration)
        if tipo == 'multiple':
            poll = Poll(id, question, options, duration)
            poll.multiple = True
            return poll
        if tipo == 'ponderada':
            poll = Poll(id, question, options, duration)
            poll.ponderada = kwargs.get('ponderada', {})
            return poll
        return Poll(id, question, options, duration)
