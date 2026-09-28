from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

orders = []


@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running"
    })


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()

    order = {
        "order_id": str(uuid.uuid4()),
        "customer_id": data.get("customer_id"),
        "items": data.get("items", []),
        "total_amount": data.get("total_amount", 0),
        "status": "PLACED"
    }

    orders.append(order)

    return jsonify(order), 201


@app.route("/orders/<order_id>", methods=["GET"])
def get_order(order_id):

    for order in orders:
        if order["order_id"] == order_id:
            return jsonify(order)

    return jsonify({"error": "Order not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8004)