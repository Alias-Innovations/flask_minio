from flask import Flask, send_file
from flask_minio import Minio
from tempfile import NamedTemporaryFile

app = Flask(__name__)

# Configuring flask for minio
app.config['MINIO_URL'] = '172.17.0.1:9000'
app.config['MINIO_ACCESS_KEY'] = 'minioaccesskey'
app.config['MINIO_SECRET_KEY'] = 'miniosecretkey'
app.config['MINIO_SECURE_CONNECTION'] = False
app.config['MINIO_BUCKETS'] = ['img']

# Creating minio instance, adn registering into the app
minio = Minio()
minio.init_app(app)


@app.route("/img/<id_>")
def query_image(id_):
    with NamedTemporaryFile(suffix="png") as file:
        minio.fget_object("img", id_, file.name)

        return send_file(file.name)


if __name__ == "__main__":
    app.run()
