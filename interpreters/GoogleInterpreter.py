from google.cloud import language


class GoogleInterpreter:
    def interpret(self, message):
        client = language.LanguageServiceClient()
        document = self.getDocument(message)

        # response = self.getSentiment(client, document)
        # response = self.getEntities(client, document)
        response = self.getSyntax(client, document)

        return response

    def getSentiment(self, client, document):
        response = client.analyze_sentiment(
            document=document,
            encoding_type='UTF32'
        )
        sentiment = response.document_sentiment
        sendingMessage = "score: " + str(sentiment.score) + ", mag: " + str(sentiment.magnitude)
        return sendingMessage

    def getEntities(self, client, document):
        response = client.analyze_entities(
            document=document,
            encoding_type='UTF32'
        )
        return str(response.entities)

    def getSyntax(self, client, document):
        response = client.analyze_syntax(
            document=document,
            encoding_type='UTF32'
        )
        return str(response.tokens)

    def getDocument(self, content, lang='en', tp='PLAIN_TEXT'):
        document = language.types.Document(
            content=content,
            language=lang,
            type=tp
        )
        return document
