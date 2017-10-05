from interpreters.ApiInterpreter import ApiInterpreter
from interpreters.GoogleInterpreter import GoogleInterpreter
from interpreters.WitInterpreter import WitInterpreter


class Overhead:
    def __init__(self):
        self.googleInterpreter = GoogleInterpreter()
        self.witInterpreter = WitInterpreter()
        self.ApiInterpreter = ApiInterpreter()

    def reply(self, message, log=None):
        response = "Google:\n"
        entities = self.googleInterpreter.analyzeEntities(message)
        for entity in entities:
            #response += "name: " + str(entity.name) + ",\n" + \
            #            "metadata: " + str(entity.metadata) + ",\n" + \
            #            "type: " + str(entity.metadata) + "\n"
            response += str(entity) + "\n"

        return response
