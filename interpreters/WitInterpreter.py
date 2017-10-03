from wit import Wit


class WitInterpreter:
    def interpret(self, message):
        access_token = "RKNTEIQC6WV3AUNWMVBMSBQM7GORSSFU"
        actions = {
            'send': self.send
        }

        # client = Wit(access_token=access_token, actions=actions)
        client = Wit(access_token)
        response = client.message(message)

        if response is None:
            return "response failed"

        return str(response)

    def send(self, request, response):
        message = request + ": " + response
        return message
