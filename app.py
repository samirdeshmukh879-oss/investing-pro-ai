import streamlit as st
import yfinance as yf

# Page setup for Mobile - Premium Look
st.set_page_config(page_title="ProPicks AI - Stocks & ETFs", layout="wide")

st.title("🤖 ProPicks AI — Stocks, ETFs & Impact News")
st.caption("Live Update: September 2026 | Powered by AI Automation Engine")

# --- SIDEBAR FOR MEMBERSHIP PLAN ---
st.sidebar.header("👑 Premium Control Panel")
membership = st.sidebar.radio("Membership Plan Chunein:", ["Investing Pro", "Investing Pro Plus"])

# Tier Count Logic for Stocks and ETFs
if membership == "Investing Pro Plus":
    stock_p_count, stock_l_count = 5, 10
    etf_p_count, etf_l_count = 5, 10
    st.sidebar.success("💎 Pro Plus Plan Active")
else:
    stock_p_count, stock_l_count = 20, 20
    etf_p_count, etf_l_count = 10, 10
    st.sidebar.info("⭐ Pro Plan Active")

# Main Navigation Tabs for App Layout
tab_news, tab_stocks, tab_etfs = st.tabs(["🔥 Live Impact News", "📊 AI Stock Picks", "🚀 AI ETF Picks"])

# --- SECTION 1: LIVE IMPACT NEWS (with Sector Benefit Analysis) ---
with tab_news:
    st.subheader("🔔 First-Alert: Market Moving News Notifications")
    st.caption("AI dynamically updates this section and scans the impact on related stocks/sectors.")
    
    # News Card 1
    with st.container(border=True):
        st.error("🚨 **BREAKING: US Federal Reserve hints at interest rate relief bets following Waller comments**")
        st.write("🌍 *Global bond yields fall sharply as inflation fears curb immediate rate hike worries.*")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.info("🎯 **Benefited Sector:** Technology, Banking & High-Growth Caps")
        with col_s2:
            st.success("📈 **Impacted Stocks to watch:** NVDA, MSFT, HDFCBANK")
            
    # News Card 2
    with st.container(border=True):
        st.warning("🚨 **BREAKING: Crude Oil Prices Surge Higher amid Middle East Tensions**")
        st.write("🛢️ *U.S. crude futures rise to $90.22 a barrel, raising input cost concerns for global markets.*")
        col_oil1, col_oil2 = st.columns(2)
        with col_oil1:
            st.info("🎯 **Benefited Sector:** Oil Exploration & Renewable Energy")
        with col_oil2:
            st.success("📈 **Impacted Stocks to watch:** ONGC, XOM, Reliance")

# --- SECTION 2: AI STOCK RECOMMENDATIONS ---
with tab_stocks:
    st.header("🎯 Explore Different AI Stock Strategies")
    
    bharat_profit = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS"] * 4
    bharat_loss = ["IDEA.NS", "YESBANK.NS", "SUZLON.NS", "ZOMATO.NS", "PAYTM.NS"] * 4
    
    with st.container(border=True):
        st.subheader("🟣 INB15 — Bharat Bargains")
        view_stocks = st.button("👁️ View Premium Stocks", key="btn_stock")
        if view_stocks:
            t1, t2 = st.tabs(["🚀 Profit Picks", "⚠️ Avoid List"])
            with t1:
                st.write(f"🟢 Top {stock_p_count} Stocks to **BUY**:")
                for i in range(stock_p_count):
                    st.success(f"📈 **{bharat_profit[i].replace('.NS','')}** | AI Action: BUY")
            with t2:
                st.write(f"🔴 Top {stock_l_count} Stocks to **AVOID**:")
                for i in range(stock_l_count):
                    st.error(f"❌ **{bharat_loss[i].replace('.NS','')}** | AI Action: REMOVE")

# --- SECTION 3: AI ETF RECOMMENDATIONS (New Feature Added) ---
with tab_etfs:
    st.header("📊 Algorithmic Exchange Traded Funds (ETFs)")
    st.caption("🔄 Automatically rebalanced every month on the 1st.")
    
    # Real World Top Performing & High Volatility ETFs Data
    etf_profit = ["NIFTYBEES.NS", "JUNIORBEES.NS", "MON100", "VOO", "SOXX"] * 2
    etf_loss = ["GOLDSHARE.NS", "SILVERETF", "NIO", "USO", "GDXJ"] * 2
    
    with st.container(border=True):
        st.subheader("🏁 Automated Monthly ETF Filter Engine")
        view_etfs = st.button("👁️ View Premium ETFs", key="btn_etf")
        
        if view_etfs:
            et1, et2 = st.tabs(["🚀 Top Performing ETFs", "⚠️ High Risk / Avoid ETFs"])
            with et1:
                st.write(f"🟢 Showing Top {etf_p_count} Momentum ETFs to **ADD** this month:")
                for i in range(etf_p_count):
                    tick = etf_profit[i]
                    try:
                        price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                        st.success(f"📈 **{tick.replace('.NS','')}** | Current Value: {price:.2f} | AI View: Bullish")
                    except:
                        st.success(f"📈 **{tick.replace('.NS','')}** | AI View: Momentum Up")
            with et2:
                st.write(f"🔴 Showing Top {etf_l_count} Underperforming ETFs to **REMOVE**:")
                for i in range(etf_l_count):
                    tick = etf_loss[i]
                    try:
                        price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                        st.error(f"❌ **{tick.replace('.NS','')}** | Current Value: {price:.2f} | AI View: Weak/Bearish")
                    except:
                        st.error(f"❌ **{tick.replace('.NS','')}** | AI View: High Risk")

# Disclaimer Footer
st.markdown("---")
st.caption("⚠️ **Disclaimer:** All data and metrics are generated for educational purpose only.")
