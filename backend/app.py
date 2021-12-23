from Flask import Flask
from flask_restful import Api

app = Flask(__name__)
@app.route('/get', methods=["GET"])
def get_users():
    all_users = Users.query.all()
    results = users_schema.dump(all_users)
    return jsonify(results)
