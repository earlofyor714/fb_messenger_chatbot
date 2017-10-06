import uuid

import apiai
import json


class ApiInterpreter:
    def __init__(self):
        access_token = "bc2f0a6d4a4943ca9c3c73125ffbd68c"
        self.client = apiai.ApiAI(access_token)

    def interpret(self, message):
        request = self.client.text_request()
        request.entities = [
            apiai.Entity("practice", ["practice"])
        ]
        request.query = message
        response = self.parseHttpResponse(request.getresponse())
        return response["result"]

    def parseHttpResponse(self, httpResponse):
        byteResponse = httpResponse.read()
        jsonResponse = byteResponse.decode('utf8').replace("'", '"')
        data = json.loads(jsonResponse)
        return data
        # return json.dumps(data, indent=4, sort_keys=True)

    def analyze_event(self, message="Welcome", log=print):
        event = apiai.events.Event(message)
        request = self.client.event_request(event)

        #entries = [
        #    apiai.Entry("practice", None)
        #]

        #request.entities = [
        #    apiai.Entity("New", entries)
        #]

        response = self.parseHttpResponse(request.getresponse())
        return response["result"]

# 2017-10-04T17:07:52.509428+00:00 app[web.1]: sending message to 1562796290438836:
# {
#     "id": "ad4eba5b-ed4d-42b2-b9fc-ed12ab2e6bf0",
#     "timestamp": "2017-10-04T17:07:52.491Z",
#     "lang": "en",
#     "result": {
#         "source": "agent",
#         "resolvedQuery": "what do you say now",
#         "action": "input.unknown",
#         "actionIncomplete": false,
#         "parameters": {},
#         "contexts": [],
#         "metadata": {
#             "intentId": "bcc2e3e5-f565-46ca-a955-d466c24fe380",
#             "webhookUsed": "false",
#             "webhookForSlotFillingUsed": "false",
#             "intentName": "Default Fallback Intent"
#         },
#         "fulfillment": {
#             "speech": "What was that?",
#             "messages": [
#                 {
#                     "type": 0,
#                     "id": "483486cc-2d38-4333-b74a-29c4803fb039",
#                     "speech": "What was that?"
#                 }
#             ]
#         },
#         "score": 1.0
#     },
#     "status": {
#         "code": 200,
#         "errorType": "success"
#     },
#     "sessionId": "087cd9d41544469dbb4f19d0b87b9f33"
# }
