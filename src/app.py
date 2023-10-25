from flask import Flask, jsonify
from device_routes import device_routes
from activity_routes import activity_routes

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Endpoint Security Rest API!"}), 200

app.register_blueprint(device_routes)
app.register_blueprint(activity_routes)

if __name__ == '__main__':
    app.run(debug=True)
