from minio import Minio as _Minio


class Minio(object):
    """
    The Minio class initializes a new Flask-Minio extension

    :param Flask app: an instance of a flask application
    """

    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)
        else:
            self.client = None

    def init_app(self, app):
        """
        Extends the provided flask application with the minio extension

        :param Flask app: an instance of a flask application
        """

        self.client = _Minio(
            app.config.get('MINIO_URL'),
            access_key=app.config.get('MINIO_ACCESS_KEY'),
            secret_key=app.config.get('MINIO_SECRET_KEY'),
            session_token=app.config.get('MINIO_SESSION_TOKEN'),
            secure=app.config.get('MINIO_SECURE_CONNECTION') or False,
            region=app.config.get('MINIO_REGION'),
            http_client=app.config.get('MINIO_HTTP_CLIENT'),
            credentials=app.config.get('MINIO_CREDENTIALS'),
        )

        for bucket in app.config.get('MINIO_BUCKETS', []):
            if not self.client.bucket_exists(bucket):
                self.client.make_bucket(bucket)

        app.extensions = getattr(app, "extensions", {})
        app.extensions["minio"] = self.client

    def __getattr__(self, name):
        return getattr(self.client, name, None)
