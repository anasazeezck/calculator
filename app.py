import streamlit as st

def round_price(price):
    return int(price) + 0.99  # Always round to .99

def calculate_price(cost_price):
    net_margin = 0.30  # 30% net margin (Deliveroo + our margin)
    selling_price = cost_price / (1 - net_margin)
    return round_price(selling_price)

st.title("Real Pharmacy Pricing Calculator")

cost_price = st.number_input("Enter Cost Price (AED):", min_value=0.01, step=0.01)

if cost_price:
    selling_price = calculate_price(cost_price)
    st.success(f"Selling Price: {selling_price} AED")
