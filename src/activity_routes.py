from flask import Blueprint, request, jsonify
from shared_resources import activity_logs, registered_devices

activity_routes = Blueprint('activity_routes', __name__)

activity_logs = []


@activity_routes.route('/activity', methods=['POST'])
def activity():
    data = request.json
    device_id = data.get('device_id') 

    required_fields = ['timestamp', 'device_id', 'user_id', 'activity_type', 'details', 'status']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({"message": f"{field} is missing or empty"}), 400

    if device_id not in registered_devices:
        return jsonify({"message": "Invalid device ID"}), 400

    log_entry = {
        'timestamp': data.get('timestamp'),
        'device_id': data.get('device_id'),
        'user_id': data.get('user_id'),
        'activity_type': data.get('activity_type'),
        'details': data.get('details'),
        'status': data.get('status')
    }


    activity_logs.append(log_entry)

    return jsonify({"message": "Activity recorded"}), 201
@activity_routes.route('/activity_logs', methods=['GET'])
def get_activity_logs():
    return jsonify(activity_logs), 200
