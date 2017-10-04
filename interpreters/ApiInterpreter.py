import apiai

class ApiInterpreter:
    def interpret(self, message):
        access_token = "bc2f0a6d4a4943ca9c3c73125ffbd68c"

        client = apiai.ApiAI(access_token)
        request = client.text_request()
        request.query = message
        response = request.getresponse()
        return str(response)
