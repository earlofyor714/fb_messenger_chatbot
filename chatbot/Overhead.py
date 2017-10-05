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
            response += "name: " + str(entity.name) + "\n"
            log("entity:\n {}".format(str(entity)))
            log("type:\n {}".format(str(entity.metadata)))
            log("metadata:\n {}".format(str(entity.metadata)))
        return response
