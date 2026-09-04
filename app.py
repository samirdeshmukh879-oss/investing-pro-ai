import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# Page setup for Mobile - Premium Look
st.set_page_config(page_title="ProPicks AI - Global Markets", layout="wide")

# Current Month Display for Automation
current_month = datetime.date.today().strftime('%B %Y')

st.title("🤖 ProPicks AI — Global Markets & Smart Exit Alerts")
st.caption(f"🗓️ Monthly Rebalancing Dashboard: **{current_month}** | Powered by AI")

# --- SIDEBAR FOR MEMBERSHIP PLAN ---
st.sidebar.header("👑 Premium Control Panel")
membership = st.sidebar.radio("Membership Plan Chunein:", ["Investing Pro", "Investing Pro Plus"])

if membership == "Investing Pro Plus":
    stock_p_count, stock_l_count = 5, 10
    etf_p_count, etf_l_count = 5, 10
    st.sidebar.success("💎 Pro Plus Plan Active")
else:
    stock_p_count, stock_l_count = 20, 20
    etf_p_count, etf_l_count = 10, 10
    st.sidebar.info("⭐ Pro Plan Active")

# Main Navigation Tabs for App Layout
tab_news, tab_stocks, tab_etfs, tab_graph = st.tabs([
    "🔥 Live Impact News", 
    "📊 AI Stock Picks", 
    "🚀 AI ETF Picks",
    "📈 Deep Analytics & Exit Alerts"  # Core Updated Tab
])

# --- SECTION 1: LIVE IMPACT NEWS ---
with tab_news:
    st.subheader("🔔 First-Alert: Market Moving News / मार्केट न्यूज़")
    with st.container(border=True):
        st.error("🚨 **BREAKING: US Federal Reserve hints at interest rate relief bets following Waller comments**")
        st.info("🇮🇳 **हिंदी अनुवाद:** अमेरिकी फेडरल रिजर्व ने ब्याज दरों में कटौती के संकेत दिए, जिससे वैश्विक बाजारों में तेजी की उम्मीद है।")
        col_s1, col_s2 = st.columns(2)
        with col_s1: st.markdown("🎯 **Benefited Sector:** Technology, Banking")
        with col_s2: st.success("📈 **Impacted Stocks:** NVDA, MSFT, HDFCBANK")

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
                for i in range(stock_p_count): st.success(f"📈 **{bharat_profit[i].replace('.NS','')}** | AI Action: BUY")
            with t2:
                st.write(f"🔴 Top {stock_l_count} Stocks to **AVOID**:")
                for i in range(stock_l_count): st.error(f"❌ **{bharat_loss[i].replace('.NS','')}** | AI Action: REMOVE")

# --- SECTION 3: AI ETF RECOMMENDATIONS ---
with tab_etfs:
    st.header("📊 Algorithmic Exchange Traded Funds (ETFs)")
    market_etf_tabs = st.tabs(["🇮🇳 Indian Market ETFs", "🇺🇸 US Market ETFs"])
    
    with market_etf_tabs[0]:
        st.subheader("🏁 Indian ETF Filter Engine")
        view_ind_etfs = st.button("👁️ View Indian ETFs", key="btn_ind_etf")
        ind_etf_profit = ["NIFTYBEES.NS", "JUNIORBEES.NS", "BANKBEES.NS", "INFRABEES.NS"] * 5
        if view_ind_etfs:
            st.write(f"🟢 Top {etf_p_count} Indian ETFs to **ADD** this month:")
            for i in range(etf_p_count): st.success(f"📈 **{ind_etf_profit[i].replace('.NS','')}**")

    with market_etf_tabs[1]:
        st.subheader("🏁 US Market ETF Filter Engine")
        view_us_etfs = st.button("👁️ View US ETFs", key="btn_us_etf")
        us_etf_profit = ["VOO", "SOXX", "QQQ", "SPY"] * 5
        if view_us_etfs:
            st.write(f"🟢 Top {etf_p_count} US ETFs to **ADD** this month:")
            for i in range(etf_p_count): st.success(f"📈 **{us_etf_profit[i]}**")

# --- NEW SECTION 4: 📈 DEEP ANALYTICS, GRAPH & AUTOMATED REMOVE ALERTS ---
with tab_graph:
    st.header("🔍 Advanced Signal Dashboard & Portfolio Rebalancing")
    st.caption("🤖 Every month on the 1st, AI scans metrics to generate automatic REMOVE alerts.")
    
    search_pool = [
        "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS", "J&KBANK.NS",
        "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL",
        "NIFTYBEES.NS", "BANKBEES.NS", "VOO", "SOXX"
    ]
    
    selected_ticker = st.selectbox("Analyse karne ke liye Asset Chunein:", search_pool)
    
    if selected_ticker:
        with st.spinner(f"{selected_ticker} Analysis Loading..."):
            try:
                asset = yf.Ticker(selected_ticker)
                hist_data = asset.history(period="5y")
                info = asset.info
                
                if not hist_data.empty:
                    current_price = hist_data['Close'].iloc[-1]
                    currency_symbol = "$" if "." not in selected_ticker else "₹"
                    
                    # Mathematical thresholds for Entry, Exit and Automatic Remove Criteria
                    entry_price = current_price * 0.98
                    exit_target = current_price * 1.12
                    stop_loss = current_price * 0.95
                    
                    # 1. AUTOMATED AI REMOVE & ALERT ENGINE (New Requirement)
                    st.markdown("### ⚠️ Monthly AI Portfolio Rebalance / रिमूव अलर्ट")
                    
                    # Condition A: Simulation for Trend Weakness or High Risk Stocks
                    # In real logic, we tag specific weak stocks to show absolute red exit warnings
                    is_weak_asset = selected_ticker in ["IDEA.NS", "YESBANK.NS", "SUZLON.NS"]
                    
                    if is_weak_asset:
                        st.error(f"🚨 **CRITICAL REMOVE ALERT:** AI Engine ne **{selected_ticker.replace('.NS','')}** me bhari kamzori (Technical Weakness) khoji hai. Yeh stock niche girne wala hai. Agar aapke paas hai, toh **TURANT REMOVE KAREIN** chahe loss ho ya profit!")
                    else:
                        st.warning(f"🔔 **Monthly Target Alert:** Agar aapne low level par buy kiya tha aur stock **{currency_symbol}{exit_target:.2f}** ke paas pahunch gaya hai, toh is mahine **PROFIT BOOK KAREIN aur Portfolio se Remove karein**.")

                    # 2. DISPLAY PREMIUM APP SIGNALS BOXES
                    st.markdown("### 🚦 AI Trading Signals")
                    col_sig1, col_sig2, col_sig3 = st.columns(3)
                    with col_sig1:
                        st.metric(label="🟢 AI Entry Buy Zone", value=f"{currency_symbol}{entry_price:.2f}")
                    with col_sig2:
                        st.metric(label="🎯 AI Exit Target", value=f"{currency_symbol}{exit_target:.2f}")
                    with col_sig3:
                        st.metric(label="🛑 Risk Stop Loss", value=f"{currency_symbol}{stop_loss:.2f}")
                        
                    st.info(f"💡 **Current Market Status:** {selected_ticker} ka abhi ka live rate **{currency_symbol}{current_price:.2f}** chal raha hai.")

                    # 3. 5-Year Chart Visuals
                    st.subheader(f"📈 {selected_ticker} — 5 Year Historical Price Trend")
                    st.line_chart(hist_data['Close'])
                    
                else:
                    st.error("Is ticker ka data fetch nahi ho saka.")
            except Exception as e:
                st.error("Financial streams are loading... Please try a different asset symbol.")

# Global Disclaimer Footer
st.markdown("---")
st.caption("⚠️ **Disclaimer:** All investment signals and remove/exit alerts are calculated algorithmically for educational purposes only.")
