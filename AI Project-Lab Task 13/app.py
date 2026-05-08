import streamlit as st
import numpy as np
import joblib

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(page_title="Hotel Booking Prediction", layout="centered")

# -----------------------------
# 💙 CLEAN SKY BLUE THEME
# -----------------------------
st.markdown("""
<style>

/* ========================= */
/* 🌆 PREMIUM CITY BACKGROUND */
/* ========================= */

.stApp {
    background:
    linear-gradient(rgba(7,12,20,0.50), rgba(7,12,20,0.50)),
    url("https://images.unsplash.com/photo-1494526585095-c41746248156?q=80&w=1974&auto=format&fit=crop");
    
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}


/* ========================= */
/* 🧊 GLASS CONTAINER */
/* ========================= */

.block-container {
    background: rgba(255,255,255,0.00);
    backdrop-filter: blur(18px);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 28px;

    padding: 2.5rem;
    margin-top: 2rem;

    box-shadow:
    0 8px 32px rgba(0,0,0,0.35),
    0 0 20px rgba(14,165,233,0.15);

    animation: fadeIn 1s ease;
}


/* ========================= */
/* ✨ FADE ANIMATION */
/* ========================= */

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(20px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* ========================= */
/* 🏨 MAIN TITLE */
/* ========================= */

h1 {
    text-align: center;
    color: white;

    font-size: 52px;
    font-weight: 800;

    letter-spacing: 1px;

    margin-bottom: 5px;

    text-shadow:
    0 0 10px rgba(56,189,248,0.6),
    0 0 30px rgba(56,189,248,0.3);
}


/* ========================= */
/* 💎 SUBHEADINGS */
/* ========================= */

h3 {
    color: black !important;
    font-weight: 700;
}


/* ========================= */
/* 🏷 LABELS */
/* ========================= */

label {
    color: #f8fafc !important;
    font-weight: 600 !important;
}


/* ========================= */
/* ✨ INPUTS */
/* ========================= */

input,
textarea {

    background: rgba(255,255,255,0.96) !important;

    color: black !important;

    border-radius: 14px !important;

    border: none !important;

    padding: 10px !important;
}


/* ========================= */
/* 📦 SELECT BOX */
/* ========================= */

.stSelectbox div,
[data-baseweb="select"] {

    background: rgba(255,255,255,0.96) !important;

    color: black !important;

    border-radius: 14px !important;
}


/* ========================= */
/* 🎚 SLIDER */
/* ========================= */

/* ========================= */
/* 🎚 SLIDER */
/* ========================= */

.stSlider span {
    color: white !important;
    font-size: 25px !important;  /* 👈 font size increase */
}


/* ========================= */
/* 🌟 HOVER EFFECTS */
/* ========================= */

.stTextInput:hover,
.stSelectbox:hover,
.stNumberInput:hover {

    transform: translateY(-2px);

    transition: 0.25s ease;
}


/* ========================= */
/* 🔘 PREDICT BUTTON */
/* ========================= */

.stButton > button {

    width: 100%;

    height: 60px;

    border: none;

    border-radius: 18px;

    font-size: 21px;

    font-weight: bold;

    color: white;

    background:
    linear-gradient(
    90deg,
    #0ea5e9,
    #2563eb,
    #38bdf8);

    background-size: 200% auto;

    box-shadow:
    0 6px 20px rgba(14,165,233,0.35);

    transition: all 0.3s ease;
}


/* Hover */

.stButton > button:hover {

    transform: scale(1.03);

    background-position: right center;

    box-shadow:
    0 0 25px rgba(56,189,248,0.8);
}


/* ========================= */
/* 🎉 RESULT BOX */
/* ========================= */

.prediction-box {

    padding: 24px;

    border-radius: 18px;

    text-align: center;

    font-size: 25px;

    font-weight: bold;

    color: white;

    margin-top: 25px;

    animation: fadeIn 0.7s ease;
}


/* ========================= */
/* 📏 BETTER SPACING */
/* ========================= */

.stSelectbox,
.stSlider,
.stNumberInput,
.stTextInput {

    margin-bottom: 18px !important;
}
            

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Load model
# -----------------------------
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")

# -----------------------------
# Title (OUTSIDE BOX NOW FIXED)
# -----------------------------
st.markdown("<h1>🏨 Hotel Booking Cancellation Prediction</h1>", unsafe_allow_html=True)
#st.markdown("### 💙 AI Powered Cancellation Predictor")

# -----------------------------
# Helper
# -----------------------------
def encode_cols(le, value):
    return le.transform([value])[0] if value in le.classes_ else -1

# -----------------------------
# Inputs
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Booking Info")
    hotel = st.selectbox("Hotel", ["Resort Hotel", "City Hotel"])
    lead_time = st.slider("Lead Time", 0, 500, 50)
    arrival_year = st.number_input("Year", 2015, 2030, 2017)
    arrival_month = st.selectbox("Month",
        ["January","February","March","April","May","June",
         "July","August","September","October","November","December"])
    week_number = st.slider("Week Number", 1, 52, 25)
    day = st.slider("Day", 1, 31, 15)

with col2:
    st.subheader("👨‍👩‍👧 Guest Info")
    adults = st.slider("Adults", 1, 5, 2)
    children = st.slider("Children", 0, 5, 0)
    babies = st.slider("Babies", 0, 3, 0)
    weekend_nights = st.slider("Weekend Nights", 0, 10, 1)
    week_nights = st.slider("Week Nights", 0, 20, 2)

st.markdown("### 🏨 Booking Details")
meal = st.selectbox("Meal", ["BB","HB","FB","SC"])
country = st.text_input("Country", "PRT")
market_segment = st.selectbox("Market Segment",
    ["Online TA","Offline TA/TO","Direct","Corporate"])
distribution_channel = st.selectbox("Channel",
    ["TA/TO","Direct","Corporate","GDS"])
deposit_type = st.selectbox("Deposit",
    ["No Deposit","Non Refund","Refundable"])

st.markdown("### ⚙️ Extra Details")
repeated = st.selectbox("Repeated Guest", [0,1])
prev_cancel = st.slider("Previous Cancellations", 0, 10, 0)
prev_not_cancel = st.slider("Previous Not Cancelled", 0, 20, 0)
reserved_room = st.selectbox("Reserved Room", list("ABCDEFG"))
assigned_room = st.selectbox("Assigned Room", list("ABCDEFG"))
booking_changes = st.slider("Booking Changes", 0, 10, 0)
waiting_days = st.slider("Waiting Days", 0, 500, 0)
customer_type = st.selectbox("Customer Type",
    ["Transient","Contract","Group","Transient-Party"])
adr = st.number_input("ADR", 0.0, 1000.0, 100.0)
parking = st.slider("Parking", 0, 5, 0)
special_requests = st.slider("Special Requests", 0, 5, 1)

# -----------------------------
# Prediction
# -----------------------------
if st.button("🔮 Predict Booking Status"):

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

    categorical_cols = [
        'hotel','arrival_date_month','meal','country',
        'market_segment','distribution_channel',
        'reserved_room_type','assigned_room_type',
        'deposit_type','customer_type'
    ]

    for col in categorical_cols:
        user_input[col] = encode_cols(encoders[col], user_input[col])

    X = np.array([[user_input[col] for col in user_input]])
    prediction = model.predict(X)

    if prediction[0] == 1:
        st.markdown('<div class="prediction-box" style="background:#ff4d6d;">❌ Booking Likely to Cancel</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="prediction-box" style="background:#28a745;">✅ Booking Confirmed</div>', unsafe_allow_html=True)