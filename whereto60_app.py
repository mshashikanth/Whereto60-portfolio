import streamlit as st
import random

# --- Page Config ---
st.set_page_config(
    page_title="WhereTo60",
    layout="centered",
)

# --- Header ---
st.markdown("<h1 style='text-align:center'>WhereTo60</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;color:gray'>Decide where to eat in under 60 seconds — fast, confident choices.</h4>", unsafe_allow_html=True)

# --- ZIP Code Input ---
zip_code = st.text_input("Enter your ZIP code:", placeholder="e.g. 94105")

# --- Mood Tabs ---
moods = ["Casual", "Fancy", "Healthy", "Comfort food", "Quick bite", "Surprise me"]
tabs = st.tabs(moods)

# --- Mood → Cuisine Mapping ---
mood_to_cuisine = {
    "Casual": ["Burger", "Pizza", "Tacos"],
    "Fancy": ["French", "Italian", "Sushi"],
    "Healthy": ["Salad", "Vegan", "Smoothie"],
    "Comfort food": ["Indian", "American", "Mexican"],
    "Quick bite": ["Sandwich", "Fast food", "Coffee"],
    "Surprise me": ["Any"]
}

# --- Price Options ---
price_options = ["Under $15", "$15 - $30", "$30+"]

# --- Initialize selections ---
selected_mood = None
selected_cuisine = []
selected_price = None

# --- Capture selections per tab ---
for idx, mood in enumerate(moods):
    with tabs[idx]:
        # capture only if this tab is selected
        if st.session_state.get("active_tab_index", 0) == idx:
            selected_mood = mood
            selected_cuisine = st.multiselect(
                "Select cuisine(s):",
                mood_to_cuisine[mood],
                key=f"cuisine_{mood}"
            )
            selected_price = st.radio(
                "Pick your price range:",
                price_options,
                key=f"price_{mood}"
            )
            st.session_state.active_tab_index = idx

# --- Recommendation Logic ---
if st.button("Find My Spot 🚀"):
    if not zip_code:
        st.warning("Please enter your ZIP code first.")
    elif not selected_mood:
        st.warning("Please select a mood and cuisine.")
    else:
        with st.spinner("Finding your next meal spot... 🍽️"):
            # Mock recommendation list
            spots = [
                {"name":"Thai Basil","address":"345 Market St, Midtown, Laveen","rating":4.6,
                 "reviews":823,"price":"$$","wait":"15-20 min","hours":"11 AM - 10 PM","must_try":"Green Curry","phone":"(555) 444-5555",
                 "reason":"Perfect comfort food vibes! Thai Basil's green curry is exactly what you need."},
                {"name":"Urban Diner","address":"123 Main St","rating":4.3,"reviews":512,"price":"$","wait":"10-15 min",
                 "hours":"10 AM - 11 PM","must_try":"Burger","phone":"(555) 111-2222","reason":"Great casual spot for a quick bite."},
                {"name":"Sushi & Co","address":"77 Elm St","rating":4.8,"reviews":1023,"price":"$$$","wait":"20-25 min",
                 "hours":"12 PM - 10 PM","must_try":"Salmon Nigiri","phone":"(555) 333-4444","reason":"Fresh sushi with an upscale vibe."}
            ]
            recommendation = random.choice(spots)

            # --- Card Layout ---
            st.markdown(
                f"""
                <div style='border:2px solid #e2e8f0; border-radius:12px; padding:24px; margin:24px auto; max-width:500px; box-shadow: 2px 2px 12px #f0f0f0;'>
                    <h2 style='color:#10b981'>{recommendation['name']}</h2>
                    <p style='margin:4px 0;'>{recommendation['address']}</p>
                    <p style='margin:4px 0;'>⭐ {recommendation['rating']} | {recommendation['reviews']} reviews</p>
                    <p style='margin:4px 0;'>💲 {recommendation['price']} | ⏱ {recommendation['wait']} | 🕒 {recommendation['hours']}</p>
                    <p style='margin:4px 0;'>🍴 Must Try: <b>{recommendation['must_try']}</b></p>
                    <p style='margin:4px 0;'>📞 {recommendation['phone']}</p>
                    <p style='margin-top:12px;'><b>Why this spot:</b> {recommendation['reason']}</p>
                    <div style='display:flex; justify-content:space-between; margin-top:16px;'>
                        <a href='https://www.google.com/maps/search/{recommendation['name']}+{recommendation['address']}' target='_blank' style='background:#6366f1; color:white; padding:10px 20px; border-radius:8px; text-decoration:none;'>Get Directions</a>
                        <button onclick="window.location.reload();" style='background:#f97316; color:white; padding:10px 20px; border-radius:8px; border:none;'>Try Again 🔁</button>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# --- Footer ---
st.markdown("---")
st.markdown("<p style='text-align:center'>Project by shashikanthm</p>", unsafe_allow_html=True)

