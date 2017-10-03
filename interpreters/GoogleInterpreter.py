from google.cloud import storage


class GoogleInterpreter:
    def interpret(self):
        storage_client = storage.Client()
        buckets = list(storage_client.list_buckets())
        return buckets
