import os

DEBUG = True
SECRET_KEY = 'my precious'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
HOST = 'localhost'
PORT = int(os.environ.get('PORT', 5000))

UPLOAD_FOLDER = "static/uploads"
MAX_CONTENT_LENGTH = 20 * 1024 * 1024
