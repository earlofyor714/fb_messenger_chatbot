from google.cloud import language


class GoogleInterpreter:
    def __init__(self):
        self.client = language.LanguageServiceClient()

    def interpret(self, message):
        document = self.getDocument(message)

        # response = self.analyzeSentiment(client, document)
        response = self.analyzeEntities(document)
        # response = self.analyzeSyntax(client, document)

        return response

    def analyzeSentiment(self, document):
        response = self.client.analyze_sentiment(
            document=document,
            encoding_type='UTF32'
        )
        sentiment = response.document_sentiment
        return str(sentiment)

    def analyzeEntities(self, document):
        response = self.client.analyze_entities(
            document=document,
            encoding_type='UTF32'
        )
        return str(response.entities)

    def analyzeSyntax(self, document):
        response = self.client.analyze_syntax(
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
