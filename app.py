import streamlit as st

def calculate_price(cost_price):
    net_margin = 0.30  # 30% net margin (Deliveroo + our margin)
    selling_price = cost_price / (1 - net_margin)
    return round(selling_price, 2)

st.title("Real Pharmacy Pricing Calculator")

cost_price = st.number_input("Enter Cost Price (AED):", min_value=0.01, step=0.01)

if st.button("Calculate"):
    selling_price = calculate_price(cost_price)
    st.success(f"Selling Price: {selling_price} AED")
