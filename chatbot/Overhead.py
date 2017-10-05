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
            response += "name: " + str(entity.name) + "\n" + \
                        "type: " + str(entity.type) + "\n" + \
                        "wiki: " + str(entity.metadata['wikipedia_url']) + "\n" + \
                        "salience: " + str(entity.salience) + "\n"
            log("entity: {}".format(str(entity)))
        return response
