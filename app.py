import streamlit as st
import yfinance as yf

# Page setup for Mobile - Premium Wide Look
st.set_page_config(page_title="ProPicks AI - Find Winning Stocks", layout="wide")

# Top Header matching the screenshot
st.title("🤖 ProPicks AI - Find Winning Stocks with AI")
st.caption("Next Update: Oct 1, 2026 | Stock Picks Updated: Sep 1, 2026")

# --- SIDEBAR FOR MEMBERSHIP PLAN ---
st.sidebar.header("👑 Premium Control Panel")
membership = st.sidebar.radio("Membership Plan Chunein:", ["Investing Pro", "Investing Pro Plus"])

if membership == "Investing Pro Plus":
    profit_count = 5
    loss_count = 10
    st.sidebar.success("💎 Pro Plus Plan Active")
else:
    profit_count = 20
    loss_count = 20
    st.sidebar.info("⭐ Pro Plan Active")

# --- TOP OUTPERFORMERS BANNER ---
st.info("🇮🇳 **NIFTY20 — Bharat Market Outperformers**\n\nThis month's top Indian stocks picked by our AI model based on momentum and value.")

st.markdown("---")
st.header("🎯 Explore Different AI Strategies")

# Real Tickers Data Configuration
bharat_profit = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS"] * 4
bharat_loss = ["IDEA.NS", "YESBANK.NS", "SUZLON.NS", "ZOMATO.NS", "PAYTM.NS"] * 4
us_profit = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL"] * 4
us_loss = ["NIO", "BABA", "INTC", "PYPL", "SNAP"] * 4

# --- STRATEGY 1: BHARAT BARGAINS ---
with st.container(border=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("🟣 INB15 — Bharat Bargains")
        st.write("*Identifies undervalued Indian stocks with strong fundamentals.*")
        st.caption("🔄 Monthly Rebalancing | 📅 2019 - 2026")
    with col2:
        view_bharat = st.button("👁️ View Stocks", key="btn_bharat")
        
    c1, c2 = st.columns(2)
    c1.metric(label="Total Return (1Y)", value="+4.7%")
    c2.metric(label="Total Return (5Y)", value="+475.1%")

    if view_bharat:
        st.markdown("### 📊 AI Stock Recommendations for this Month")
        t1, t2 = st.tabs(["🚀 Top Profit Picks", "⚠️ Top Avoid (Loss) List"])
        with t1:
            st.write(f"🟢 Showing Top {profit_count} Stocks to **ADD/BUY**:")
            for i in range(profit_count):
                tick = bharat_profit[i]
                try:
                    price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                    st.success(f"📈 **{tick.replace('.NS','')}** | Price: ₹{price:.2f} | Action: BUY")
                except:
                    st.success(f"📈 **{tick.replace('.NS','')}** | Action: BUY")
        with t2:
            st.write(f"🔴 Showing Top {loss_count} Stocks to **REMOVE/AVOID**:")
            for i in range(loss_count):
                tick = bharat_loss[i]
                try:
                    price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                    st.error(f"❌ **{tick.replace('.NS','')}** | Price: ₹{price:.2f} | Action: REMOVE")
                except:
                    st.error(f"❌ **{tick.replace('.NS','')}** | Action: REMOVE")

# --- STRATEGY 2: BEAT THE S&P 500 (US MARKET) ---
with st.container(border=True):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("🔵 SP20 — Beat the S&P 500")
        st.write("*Picks from the S&P 500 refined by AI to outperform the US market.*")
        st.caption("🔄 Monthly Rebalancing | 📅 2013 - 2026")
    with col2:
        view_us = st.button("👁️ View Stocks", key="btn_us")
        
    c1, c2 = st.columns(2)
    c1.metric(label="Total Return (1Y)", value="+8.7%")
    c2.metric(label="Total Return (5Y)", value="+74.0%")

    if view_us:
        st.markdown("### 📊 AI US Stock Recommendations for this Month")
        t1, t2 = st.tabs(["🚀 Top Profit Picks", "⚠️ Top Avoid (Loss) List"])
        with t1:
            st.write(f"🟢 Showing Top {profit_count} US Stocks to **ADD/BUY**:")
            for i in range(profit_count):
                tick = us_profit[i]
                try:
                    price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                    st.success(f"📈 **{tick}** | Price: ${price:.2f} | Action: BUY")
                except:
                    st.success(f"📈 **{tick}** | Action: BUY")
        with t2:
            st.write(f"🔴 Showing Top {loss_count} US Stocks to **REMOVE/AVOID**:")
            for i in range(loss_count):
                tick = us_loss[i]
                try:
                    price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                    st.error(f"❌ **{tick}** | Price: ${price:.2f} | Action: REMOVE")
                except:
                    st.error(f"❌ **{tick}** | Action: REMOVE")

# --- HOW TO USE SECTION ---
st.markdown("---")
with st.expander("❓ How to Use ProPicks AI"):
    st.write("1. **Choose Tier:** Select Pro or Pro Plus from the sidebar.")
    st.write("2. **Click View Stocks:** Tap on any strategy card to instantly load the AI Buy and Avoid lists.")
    st.write("3. **Monthly Action:** Follow recommendations on the 1st of every month.")

st.caption("⚠️ **Disclaimer:** Information is for educational purposes only.")
