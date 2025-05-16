import random
import json

class TieBreakerStrategy:
    def break_tie(self, winners):
        pass

class AlphabeticalTieBreaker(TieBreakerStrategy):
    def break_tie(self, winners):
        return sorted(winners)[0] if winners else None

class RandomTieBreaker(TieBreakerStrategy):
    def break_tie(self, winners):
        return random.choice(winners) if winners else None

class ExtraTimeTieBreaker(TieBreakerStrategy):
    def break_tie(self, winners):
        return None

class ResultFormatStrategy:
    def format(self, results):
        pass

class TextResultFormat(ResultFormatStrategy):
    def format(self, results):
        return str(results)

class AsciiGraphResultFormat(ResultFormatStrategy):
    def format(self, results):
        lines = []
        for k, v in results.items():
            lines.append(f"{k}: {'#'*v}")
        return '\n'.join(lines)

class JsonResultFormat(ResultFormatStrategy):
    def format(self, results):
        return json.dumps(results)
