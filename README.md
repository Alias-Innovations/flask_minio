
 ## Flask minio factory

  A package, which provides easy usage for minio with flask.

  Via this package you can easily create this connection
  - with directly creating a minio instance
  - or by using the application factory pattern

  ### Intallation

  You can install the package from pip:

  ```
  pip install flask-minio-factory
  ```

  ### Usage

  If you want to create a minio instance directly
  you can achieve it by:

  ```
  from flask import Flask
  from flask_minio import Minio

  app = Flask(__name__)
  minio_client = Minio(app)
  ```

  If you want to create the client via the application
  factory, you are able to do that with:

  ```
  from flask import Flask, send_file
  from flask_minio import Minio

  app = Flask(__name__)

  minio = Minio()
  minio.init_app(app)
  ```

  If you have the client you can simply call the available
  methods on it:
  ```
  @app.route("/img/<id_>")
  def query_image(id_):
      with NamedTemporaryFile(suffix="png") as file:
          minio.fget_object("img", id_, file.name)

          return send_file(file.name)
  ```

  (an example code can be tested under `/example`)

  The following config variables are avialble in the flask config:

  |Variable|Description|Default|
  |-|-|-|
  |MINIO_URL| Hostname of a S3 service.| - |
  |MINIO_ACCESS_KEY| (Optional) Access key (aka user ID) of your account in S3 service.| - |
  |MINIO_SECRET_KEY| (Optional) Secret Key (aka password) of your account in S3 service.| - |
  |MINIO_SESSION_TOKEN| (Optional) Session token of your account in S3 service.| - |
  |MINIO_SECURE_CONNECTION| (Optional) Flag to indicate to use secure (TLS) connection to S3 service or not.| `False` |
  |MINIO_REGION| (Optional) Region name of buckets in S3 service.| - |
  |MINIO_HTTP_CLIENT| (Optional) Customized HTTP client.| - |
  |MINIO_CREDENTIALS| (Optional) Credentials of your account in S3 service.| - |
  |MINIO_BUCKETS| (Optional) A list of buckets, that should be created at startup | - |