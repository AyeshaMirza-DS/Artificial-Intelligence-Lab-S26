from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)

# Load Model + Encoders
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

# -----------------------------
# Helper Function
# -----------------------------
def encode_cols(le, value):
    return le.transform([value])[0] if value in le.classes_ else -1


# -----------------------------
# Home Page
# -----------------------------
@app.route('/')
def home():
    return render_template('index.html')


# -----------------------------
# Prediction
# -----------------------------
@app.route('/predict', methods=['POST'])
def predict():

    hotel = request.form['hotel']
    lead_time = int(request.form['lead_time'])
    arrival_year = int(request.form['arrival_date_year'])
    arrival_month = request.form['arrival_date_month']
    week_number = int(request.form['arrival_date_week_number'])
    day = int(request.form['arrival_date_day_of_month'])

    adults = int(request.form['adults'])
    children = int(request.form['children'])
    babies = int(request.form['babies'])

    weekend_nights = int(request.form['stays_in_weekend_nights'])
    week_nights = int(request.form['stays_in_week_nights'])

    meal = request.form['meal']
    country = request.form['country']
    market_segment = request.form['market_segment']
    distribution_channel = request.form['distribution_channel']

    repeated = int(request.form['is_repeated_guest'])
    prev_cancel = int(request.form['previous_cancellations'])
    prev_not_cancel = int(request.form['previous_bookings_not_canceled'])

    reserved_room = request.form['reserved_room_type']
    assigned_room = request.form['assigned_room_type']

    booking_changes = int(request.form['booking_changes'])

    deposit_type = request.form['deposit_type']
    waiting_days = int(request.form['days_in_waiting_list'])

    customer_type = request.form['customer_type']

    adr = float(request.form['adr'])

    parking = int(request.form['required_car_parking_spaces'])

    special_requests = int(request.form['total_of_special_requests'])

    # -----------------------------
    # User Input Dictionary
    # -----------------------------
    user_input = {

        'hotel': hotel,
        'lead_time': lead_time,
        'arrival_date_year': arrival_year,
        'arrival_date_month': arrival_month,
        'arrival_date_week_number': week_number,
        'arrival_date_day_of_month': day,

        'stays_in_weekend_nights': weekend_nights,
        'stays_in_week_nights': week_nights,

        'adults': adults,
        'children': children,
        'babies': babies,

        'meal': meal,
        'country': country,
        'market_segment': market_segment,
        'distribution_channel': distribution_channel,

        'is_repeated_guest': repeated,
        'previous_cancellations': prev_cancel,
        'previous_bookings_not_canceled': prev_not_cancel,

        'reserved_room_type': reserved_room,
        'assigned_room_type': assigned_room,

        'booking_changes': booking_changes,

        'deposit_type': deposit_type,

        'days_in_waiting_list': waiting_days,

        'customer_type': customer_type,

        'adr': adr,

        'required_car_parking_spaces': parking,

        'total_of_special_requests': special_requests
    }

    # -----------------------------
    # Encode Categorical Columns
    # -----------------------------
    categorical_cols = [

        'hotel',
        'arrival_date_month',
        'meal',
        'country',
        'market_segment',
        'distribution_channel',
        'reserved_room_type',
        'assigned_room_type',
        'deposit_type',
        'customer_type'

    ]

    for col in categorical_cols:
        user_input[col] = encode_cols(encoders[col], user_input[col])

    # -----------------------------
    # Prediction
    # -----------------------------
    X = np.array([[user_input[col] for col in user_input]])

    prediction = model.predict(X)

    # -----------------------------
    # Result
    # -----------------------------
    if prediction[0] == 1:
        result = "❌ Booking Likely to Cancel"
    else:
        result = "✅ Booking Confirmed"

    return render_template(
        'index.html',
        prediction_text=result
    )


# -----------------------------
# Run App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True)