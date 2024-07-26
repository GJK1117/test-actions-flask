from . import main
from flask import jsonify
import json

@main.route('/', methods=['GET'])
def index():
    """
    main route
    """
    
    return jsonify({"message":"test good"})