import apiai
import json


class ApiInterpreter:
    def interpret(self, message):
        access_token = "bc2f0a6d4a4943ca9c3c73125ffbd68c"

        client = apiai.ApiAI(access_token)
        request = client.text_request()
        request.query = message
        response = self.parseHttpResponse(request.getresponse())
        return str(response)

    def parseHttpResponse(self, httpResponse):
        byteResponse = httpResponse.read()
        jsonResponse = byteResponse.decode('utf8').replace("'", '"')
        data = json.loads(jsonResponse)
        return json.dumps(data, indent=4, sort_keys=True)

# {
#     'object': 'page',
#     'entry': [
#         {
#             'id': '454685428250537',
#             'time': 1507136872150,
#             'messaging': [
#                 {
#                     'sender': {
#                         'id': '1562796290438836'
#                     },
#                     'recipient': {
#                         'id': '454685428250537'
#                     }, 'timestamp': 1507136872014,
#                     'message': {
#                         'mid': 'mid.$cAAGdiJXkr_1lGaDmTle6FuU856Zf',
#                         'seq': 29100,
#                         'text': 'what do you say now'
#                     }
#                 }
#             ]
#         }
#     ]
# }

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
