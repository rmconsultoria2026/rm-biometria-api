from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os
from datetime import datetime
import random

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def health():
    return jsonify({
        "status": "online",
        "service": "RM Identity API",
        "version": "2.1.0",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/api/v1/verify', methods=['POST'])
def verify():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados invalidos"}), 400

        photo_live = data.get('photo_live', '')
        photo_ref = data.get('photo_ref', '')

        if not photo_live:
            return jsonify({"error": "Foto obrigatoria"}), 400

        # Simulacao do motor biometrico
        score = round(random.uniform(82.0, 97.5), 1)
        approved = score >= 80.0
        tx_id = "RMID-" + datetime.now().strftime("%Y%m%d%H%M%S")

        return jsonify({
            "status": "success",
            "approved": approved,
            "score": score,
            "tx_id": tx_id,
            "timestamp": datetime.now().isoformat(),
            "api": "RM Identity v2.1"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port
