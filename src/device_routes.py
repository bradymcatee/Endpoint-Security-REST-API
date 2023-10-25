from flask import Blueprint, request, jsonify
from example_devices import example_devices

device_routes = Blueprint('device_routes', __name__)

registered_devices = {}

registered_devices.update(example_devices)

@device_routes.route('/register_device', methods=['POST'])
def register_device():
    data = request.json
    device_id = data.get('device_id', None)
    device_name = data.get('device_name', None)

    if not device_id or not device_name:
        return jsonify({"message": "Bad Request", "details": "Device ID and Device Name required"}), 400
    
    registered_devices[device_id] = device_name

    return jsonify({"message": "Device registered"}), 201

@device_routes.route('/devices/<device_id>', methods=['GET'])
def get_device(device_id):
    device = registered_devices.get(device_id)

    if device:
        return jsonify({'device_id': device_id, 'device_name': device}), 200
    else: 
        return jsonify({'message': 'Device not found'}), 404


@device_routes.route('/devices/<device_id>', methods=['DELETE'])
def delete_device(device_id):
    if device_id in registered_devices:
        del registered_devices[device_id]
        return jsonify({'message': 'Device deleted'}), 201
    else:
        return jsonify({'message': 'Device not found'}), 404

@device_routes.route('/display_devices', methods=['GET'])
def display_devices():
    if not registered_devices:
        return jsonify({'message': 'No devices registered'}), 404
    else:
        return jsonify(registered_devices), 200
