# app.py
from flask import Flask, jsonify, request
import os

app = Flask(__name__)
# A very simple in-memory database
bills = {}

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok"}), 200

@app.route('/bills', methods=['POST'])
def create_bill():
    bill_id = str(len(bills) + 1)
    bills[bill_id] = {"id": bill_id, "status": "created", "details": request.json}
    print(f"Bill {bill_id} created.")
    # In a real app, we'd publish to Kafka here
    return jsonify(bills[bill_id]), 201

@app.route('/bills/<bill_id>', methods=['GET'])
def get_bill(bill_id):
    return jsonify(bills.get(bill_id, {})), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)