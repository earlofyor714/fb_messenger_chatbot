from google.cloud import language


class GoogleInterpreter:
    def __init__(self):
        self.client = language.LanguageServiceClient()

    def analyzeSentiment(self, message):
        document = self.getDocument(message)
        response = self.client.analyze_sentiment(
            document=document,
            encoding_type='UTF32'
        )
        sentiment = response.document_sentiment
        return sentiment

    def analyzeEntities(self, message):
        document = self.getDocument(message)
        response = self.client.analyze_entities(
            document=document,
            encoding_type='UTF32'
        )
        return response.entities

    def analyzeSyntax(self, message):
        document = self.getDocument(message)
        response = self.client.analyze_syntax(
            document=document,
            encoding_type='UTF32'
        )
        return response.tokens

    def getDocument(self, content, lang='en', tp='PLAIN_TEXT'):
        document = language.types.Document(
            content=content,
            language=lang,
            type=tp
        )
        return document
