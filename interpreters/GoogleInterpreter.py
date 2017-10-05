from google.cloud import language


class GoogleInterpreter:
    def interpret(self, message):
        client = language.LanguageServiceClient()
        document = self.getDocument(message)

        response = self.analyzeSentiment(client, document)
        # response = self.analyzeEntities(client, document)
        # response = self.analyzeSyntax(client, document)

        return response

    def analyzeSentiment(self, client, document):
        response = client.analyze_sentiment(
            document=document,
            encoding_type='UTF32'
        )
        sentiment = response.document_sentiment
        # sendingMessage = "score: " + str(sentiment.score) + ", mag: " + str(sentiment.magnitude)
        # return sendingMessage
        return str(sentiment)

    def analyzeEntities(self, client, document):
        response = client.analyze_entities(
            document=document,
            encoding_type='UTF32'
        )
        return str(response.entities)

    def analyzeSyntax(self, client, document):
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
