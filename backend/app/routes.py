from flask import Blueprint, jsonify, request 

routes = Blueprint("routes", __name__)

@routes.route('/health', methods = ["GET"])
def health_check(): 
    return {'status': 'healthy'}