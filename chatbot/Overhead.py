from interpreters.ApiInterpreter import ApiInterpreter
from interpreters.GoogleInterpreter import GoogleInterpreter
from interpreters.WitInterpreter import WitInterpreter


class Overhead:
    def __init__(self):
        self.googleInterpreter = GoogleInterpreter()
        self.witInterpreter = WitInterpreter()
        self.apiInterpreter = ApiInterpreter()

    def reply(self, message, log=print):
        # self.reply_entities(message, log)

        # get text from api.ai
        response = self.apiInterpreter.analyze_text(message)
        # if action==switching, switch platforms
        if response['action'] == 'switching':
            return str(response['fulfillment']['speech'])
        # else display raw response from appropriate bot
        return str(response)

    def reply_entities(self, message, log=print):
        response = "Google entities:\n"
        entities = self.googleInterpreter.analyzeEntities(message)
        for entity in entities:
            if len(response) > 500:
                break
            response += "name: " + str(entity.name) + "\n" + \
                        "type: " + str(entity.type) + "\n" + \
                        "wiki: " + str(entity.metadata['wikipedia_url']) + "\n" + \
                        "salience: " + str(entity.salience) + "\n"
            log("entity: {}".format(str(entity)))
        return response

    def reply_syntax(self, message, log=print):
        response = "Google syntax:\n"
        syntax = self.googleInterpreter.analyzeSyntax(message)
        log(str(syntax))
        for word in syntax:
            if len(response) + len(str(word)) > 638:
                break
            response += str(word)
        return response

    def reply_api(self, message, log=print):
        response = self.apiInterpreter.analyze_text(message)
        log("api.ai: {}".format(response))
        action = response['action']
        speech = response['fulfillment']['speech']
        return str(action) + ", " + str(speech)
