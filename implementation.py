import json

# Function to read the JSON file containing herd information
def read_herd_information(file_path):
    with open(file_path, 'r') as file:
        herd_data = json.load(file)
    return herd_data

# Function to calculate stock and herd management after T days
def calculate_stock_and_herd(herd_info, elapsed_days, stock_data):
    # Extract initial stock values
    initial_milk_stock = stock_data['milk']
    initial_skins_stock = stock_data['skins']

    # Placeholder calculation for milk and skins stock after T days
    # (Modify as needed based on the actual logic)
    milk_stock_after_t = initial_milk_stock + (elapsed_days * 10)  # Placeholder calculation
    skins_stock_after_t = initial_skins_stock + (elapsed_days // 5)  # Placeholder calculation
    
    # Update the herd information after T days (e.g., simulate aging or changes)
    updated_herd_info = update_herd_after_t(herd_info, elapsed_days)

    return milk_stock_after_t, skins_stock_after_t, updated_herd_info

# Placeholder function for updating herd information after T days (Modify as needed)
def update_herd_after_t(herd_info, elapsed_days):
    # Placeholder update for herd information after T days
    # Simulating aging or changes in the herd
    updated_herd = herd_info.copy()
    for yak in updated_herd['herd']:
        yak['age'] += elapsed_days / 365  # Assuming a year has 365 days
        yak['last_shaved_age'] = round(yak['age'] - 1, 1)  # Assuming shaving happens yearly
    return updated_herd

# Function for order fulfillment checking stock availability
def order_fulfillment(milk_stock, skins_stock, requested_milk, requested_skins):
    # Check if requested stock is available
    if milk_stock >= requested_milk and skins_stock >= requested_skins:
        # Order can be fully fulfilled
        return {"status": 200, "message": "Order Fulfilled", "details": f"Ordered {requested_milk} units of milk and {requested_skins} skins"}
    elif milk_stock > 0 and skins_stock > 0:
        # Order partially fulfilled
        milk_fulfilled = min(milk_stock, requested_milk)
        skins_fulfilled = min(skins_stock, requested_skins)
        return {
            "status": 206,
            "message": "Partial Order Fulfilled",
            "details": f"Partially fulfilled with {milk_fulfilled} units of milk and {skins_fulfilled} skins"
        }
    else:
        # Order cannot be fulfilled
        return {"status": 404, "message": "Insufficient Stock", "details": "Stock unavailable for the order"}

# Example usage
file_path = 'sample_diverse_dataset.json'
stock_data = {"milk": 1261.34, "skins": 1}
herd_information = read_herd_information(file_path)
elapsed_time_days = 30  # Example: elapsed time in days

# Calculate stock and herd management after T days
milk_stock_after_t, skins_stock_after_t, updated_herd_info = calculate_stock_and_herd(herd_information, elapsed_time_days, stock_data)
print(f"Milk Stock after {elapsed_time_days} days: {milk_stock_after_t}")
print(f"Skins Stock after {elapsed_time_days} days: {skins_stock_after_t}")
print("Updated Herd Information after", elapsed_time_days, "days:")
print(json.dumps(updated_herd_info, indent=2))

# Example Order Fulfillment
requested_milk_units = 1500
requested_skins_units = 3
order_status = order_fulfillment(milk_stock_after_t, skins_stock_after_t, requested_milk_units, requested_skins_units)
print("\nOrder Fulfillment Status:")
print(json.dumps(order_status, indent=2))


