from google.cloud import language


class GoogleInterpreter:
    def interpret(self, message):
        client = language.LanguageServiceClient()
        document = self.getDocument(message)

        response = client.analyze_sentiment(
            document=document,
            encoding_type='UTF32'
        )

        sentiment = response.document_sentiment
        entities = response.entities
        sendingMessage = "score: " + str(sentiment.score) + ", mag: " + str(sentiment.magnitude) + ", ent: " + entities[0].name
        return sendingMessage

    def getDocument(self, content, lang='en', tp='PLAIN_TEXT'):
        document = language.types.Document(
            content=content,
            language=lang,
            type=tp
        )
        return document
