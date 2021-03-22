from ..extension import Minio
from flask import Flask


def test_minio_created_without_client_if_no_app_provided():
    minio = Minio()

    assert minio.client is None


def test_minio_client_created_with_init_app():
    app = Flask(__name__)

    # Configuring flask for minio
    app.config['MINIO_URL'] = '172.17.0.1:9000'
    app.config['MINIO_ACCESS_KEY'] = 'minioaccesskey'
    app.config['MINIO_SECRET_KEY'] = 'miniosecretkey'
    app.config['MINIO_SECURE_CONNECTION'] = False
    app.config['MINIO_BUCKETS'] = ['img']

    # Creating minio instance, and registering into the app
    minio = Minio()
    minio.init_app(app)

    assert minio.client is not None
    assert minio.client.bucket_exists('img') is True


def test_minio_client_created_directly():
    app = Flask(__name__)

    # Configuring flask for minio
    app.config['MINIO_URL'] = '172.17.0.1:9000'
    app.config['MINIO_ACCESS_KEY'] = 'minioaccesskey'
    app.config['MINIO_SECRET_KEY'] = 'miniosecretkey'
    app.config['MINIO_SECURE_CONNECTION'] = False
    app.config['MINIO_BUCKETS'] = ['img']

    minio = Minio(app)

    assert minio.client is not None
    assert minio.client.bucket_exists('img') is True


def test_minio_could_be_created_without_bucket_provided():
    app = Flask(__name__)

    # Configuring flask for minio
    app.config['MINIO_URL'] = '172.17.0.1:9000'
    app.config['MINIO_ACCESS_KEY'] = 'minioaccesskey'
    app.config['MINIO_SECRET_KEY'] = 'miniosecretkey'
    app.config['MINIO_SECURE_CONNECTION'] = False

    minio = Minio(app)

    assert minio.client is not None
