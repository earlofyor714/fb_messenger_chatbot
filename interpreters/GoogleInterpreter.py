from google.cloud import language


class GoogleInterpreter:
    def interpret(self, message):
        client = language.LanguageServiceClient()
        document = self.getDocument(message)

        response = self.getSentiment(client, document)
        return response

    def getSentiment(self, client, document):
        response = client.analyze_sentiment(
            document=document,
            encoding_type='UTF32'
        )
        sentiment = response.document_sentiment
        sendingMessage = "score: " + str(sentiment.score) + ", mag: " + str(sentiment.magnitude)
        return sendingMessage

    def getDocument(self, content, lang='en', tp='PLAIN_TEXT'):
        document = language.types.Document(
            content=content,
            language=lang,
            type=tp
        )
        return document
