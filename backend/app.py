from flask import Flask
from flask_restful import Api

app = Flask(__name__)
@app.route('/users', methods=["GET", "POST"])
def users():
    return {"status" : "ok"}