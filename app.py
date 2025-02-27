from config import *
from flask import Flask, jsonify
from flask_cors import CORS
from apps.main import main as main_blueprint

app = Flask(__name__)
CORS(app)

# Register Blueprints
app.register_blueprint(main_blueprint, url_prefix = '/main')

address = '0.0.0.0'

if __name__ == '__main__':
    app.run(debug=True, host=address, port=5000)