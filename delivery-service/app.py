from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

deliveries = []


@app.route("/")
def home():
    return jsonify({
        "service": "Delivery Service",
        "status": "running"
    })


@app.route("/deliveries", methods=["GET"])
def get_deliveries():
    return jsonify(deliveries)


@app.route("/deliveries", methods=["POST"])
def create_delivery():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Request body is required"}), 400

    delivery = {
        "delivery_id": str(uuid.uuid4()),
        "order_id": data.get("order_id"),
        "customer_id": data.get("customer_id"),
        "address": data.get("address"),
        "status": "OUT_FOR_DELIVERY"
    }

    deliveries.append(delivery)

    return jsonify(delivery), 201


@app.route("/deliveries/<delivery_id>", methods=["GET"])
def get_delivery(delivery_id):

    for delivery in deliveries:
        if delivery["delivery_id"] == delivery_id:
            return jsonify(delivery)

    return jsonify({"error": "Delivery not found"}), 404


@app.route("/deliveries/<delivery_id>", methods=["PUT"])
def update_delivery(delivery_id):

    for delivery in deliveries:

        if delivery["delivery_id"] == delivery_id:

            data = request.get_json()

            if "status" in data:
                delivery["status"] = data["status"]

            return jsonify(delivery)

    return jsonify({"error": "Delivery not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8005)