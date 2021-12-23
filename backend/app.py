from Flask import Flask
from flask_restful import Api

app = Flask(__name__)
@app.route('/', methods=["GET"])
def get_users():
    return 'you can render your template'
