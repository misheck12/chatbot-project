# Mock order tracking function
def track_order(order_id):
    mock_order_data = {
        "1001": "Order 1001 is being prepared",
        "1002": "Order 1002 has been shipped",
        "1003": "Order 1003 has been delivered",
    }
    return mock_order_data.get(order_id, "Order not found. Please check the ID.")
