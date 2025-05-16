class Poll:
    def __init__(self, id, question, options, duration):
        self.id = id
        self.question = question
        self.options = options
        self.votes = []
        self.state = 'active'
        self.created_at = None
        self.closed_at = None
        self.duration = duration
