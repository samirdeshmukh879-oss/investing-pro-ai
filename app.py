import streamlit as st

st.set_page_config(page_title="Investing Pro AI", layout="centered")
st.title("🎯 Investing Pro & Pro Plus AI")
st.write("Step 2: App Interface & Tier Structure")

st.sidebar.header("⚙️ App Control Panel")
membership = st.sidebar.radio("Membership Plan Chunein:", ["Investing Pro", "Investing Pro Plus"])
market = st.sidebar.selectbox("Market Dashboard:", ["Indian Market (NSE)", "US Market (NYSE/NASDAQ)"])
asset_type = st.sidebar.selectbox("Asset Class:", ["Stocks (Index-wise)", "ETFs & Mutual Funds"])

st.warning("🤖 **AI Monthly Action Alert:**\n\n🟢 **ADD:** AI ne is mahine ke liye naye trends dhoond liye hain.\n\n🔴 **REMOVE:** Purane kharab perform karne wale assets ko portfolio se hataen.")

st.header(f"📊 {market} - {asset_type}")

if membership == "Investing Pro Plus":
    st.info("💎 **Pro Plus Active:** Is plan me aapko har Index ke **Top 5 Profit** picks aur **Top 10 Loss (Avoid)** stocks dikhenge.")
    tab1, tab2 = st.tabs(["🚀 Top 5 Profit Picks", "⚠️ Top 10 Avoid List"])
    with tab1:
        st.subheader("🟢 Top 5 Profit Dene Wale Assets")
        for i in range(1, 6): st.success(f"Asset #{i} - Bullish Trend 📈")
    with tab2:
        st.subheader("🔴 Top 10 Loss/Risk Wale Assets (Se Bachein)")
        for i in range(1, 11): st.error(f"❌ Asset #{i} - Bearish Trend 📉 (AI Suggestion: REMOVE)")
else:
    st.info("⭐ **Pro Active:** Is plan me aapko har Index ke **Top 20 Profit** aur **Top 20 Loss (Avoid)** assets dikhenge.")
    tab1, tab2 = st.tabs(["🚀 Top 20 Profit Picks", "⚠️ Top 20 Avoid List"])
    with tab1:
        st.subheader("🟢 Top 20 Profit Dene Wale Assets")
        for i in range(1, 21): st.success(f"Asset #{i} - Broad Market Pick 📈")
    with tab2:
        st.subheader("🔴 Top 20 Loss/Risk Wale Assets")
        for i in range(1, 21): st.error(f"❌ Asset #{i} - High Risk Alert 📉")
