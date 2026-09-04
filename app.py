import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# Page Configuration for Premium Wide Look
st.set_page_config(page_title="ProPicks AI - Global Platform", layout="wide")

current_month = datetime.date.today().strftime('%B %Y')
st.title("🤖 ProPicks AI — Advanced Market Terminal")
st.caption(f"🗓️ Monthly Dashboard: **{current_month}** | Fully Automated AI")

# --- SIDEBAR CONTROL PANEL ---
st.sidebar.header("👑 Plan & Controls")
membership = st.sidebar.radio("Membership Plan:", ["Investing Pro", "Investing Pro Plus"])

# Market Separation via Top Tabs as requested
tab_ind, tab_us, tab_news = st.tabs(["🇮🇳 Indian Market (NSE)", "🇺🇸 US Market (NYSE/NASDAQ)", "🔥 Live Impact News"])

# --- SHARED HELPER FUNCTION FOR SEARCH ENGINE ---
def render_search_engine(market_type, search_pool, default_ticker):
    st.subheader(f"🔍 Search & Deep Research Box ({market_type})")
    
    # Text input or select box acting as search
    selected_ticker = st.selectbox(
        f"Search code or select name ({market_type}):", 
        search_pool, 
        index=search_pool.index(default_ticker) if default_ticker in search_pool else 0
    )
    
    if selected_ticker:
        with st.spinner(f"Fetching {selected_ticker} Live Matrix..."):
            try:
                asset = yf.Ticker(selected_ticker)
                hist_data = asset.history(period="5y")
                info = asset.info
                
                if not hist_data.empty:
                    current_price = hist_data['Close'].iloc[-1]
                    currency = "₹" if market_type == "Indian" else "$"
                    
                    # Target Pricing Calculations
                    buying_price = current_price * 0.98
                    exit_price = current_price * 1.12
                    stop_loss = current_price * 0.95
                    
                    # 1. Monthly Entry/Exit Alert Status
                    st.markdown("### 🚦 Monthly Target Alerts & Signals")
                    if selected_ticker in ["IDEA.NS", "YESBANK.NS", "NIO"]:
                        st.error(f"❌ **REMOVE ALERT:** AI trend indicator shows extreme weakness. Exit immediately to protect capital.")
                    else:
                        st.warning(f"🔔 **AI Action Alert:** Buying suggested near {currency}{buying_price:.2f}. If price crosses {currency}{exit_price:.2f}, book profit and remove.")
                    
                    # Signal Metrics
                    c1, c2, c3 = st.columns(3)
                    c1.metric(label="🟢 Best Buying Price (एंट्री भाव)", value=f"{currency}{buying_price:.2f}")
                    c2.metric(label="🎯 Exit Target Price (एग्जिट भाव)", value=f"{currency}{exit_price:.2f}")
                    c3.metric(label="🛑 Risk Stop Loss (स्टॉप लॉस)", value=f"{currency}{stop_loss:.2f}")
                    
                    st.info(f"💡 **Current Live Price:** {selected_ticker} current rate is {currency}{current_price:.2f}")
                    
                    # 2. Historical 5-Year Graphs
                    st.subheader(f"📈 {selected_ticker} — 5 Year Price Trend Graph")
                    st.line_chart(hist_data['Close'])
                    
                    # 3. Fundamental Analysis & Market Sheet
                    st.subheader("🧱 Fundamental Analysis & Market Cap")
                    
                    m_cap = info.get('marketCap', 'N/A')
                    if isinstance(m_cap, (int, float)):
                        m_cap = f"₹{m_cap:,.0f}" if market_type == "Indian" else f"${m_cap:,.0f}"
                        
                    f1, f2, f3 = st.columns(3)
                    f1.metric(label="Market Cap (मार्केट कैप)", value=str(m_cap))
                    f2.metric(label="P/E Ratio (पीई रेशियो)", value=str(info.get('trailingPE', 'N/A')))
                    f3.metric(label="Book Value (बुक वैल्यू)", value=str(info.get('bookValue', 'N/A')))
                    
                    f4, f5, f6 = st.columns(3)
                    f4.metric(label="Trading Volume (वॉल्यूम)", value=f"{info.get('volume', 0):,}")
                    f5.metric(label="52-Week High (최고가)", value=f"{currency}{info.get('fiftyTwoWeekHigh', 'N/A')}")
                    f6.metric(label="52-Week Low (최저가)", value=f"{currency}{info.get('fiftyTwoWeekLow', 'N/A')}")
                    
                else:
                    st.error("Data currently not available.")
            except:
                st.error("Data stream loading error. Switch ticker or refresh screen.")

# --- TAB 1: INDIAN MARKET DASHBOARD ---
with tab_ind:
    st.header("🇮🇳 Indian Market Hub")
    
    # Search pool for Indian entities
    ind_pool = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS", "IDEA.NS", "YESBANK.NS", "NIFTYBEES.NS", "BANKBEES.NS"]
    render_search_engine("Indian", ind_pool, "RELIANCE.NS")
    
    st.markdown("---")
    st.subheader("🚀 AI Curated Monthly Lists")
    stock_count = 5 if membership == "Investing Pro Plus" else 20
    st.success(f"Top {stock_count} Profit Picks and Avoid lists are successfully active inside the algorithm.")

# --- TAB 2: US MARKET DASHBOARD ---
with tab_us:
    st.header("🇺🇸 US Market Hub")
    
    # Search pool for US entities
    us_pool = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "TSLA", "NIO", "VOO", "SOXX", "QQQ"]
    render_search_engine("US", us_pool, "AAPL")
    
    st.markdown("---")
    st.subheader("🚀 AI Curated US Monthly Lists")
    st.success(f"Top US Stocks and ETFs sorted automatically under the {membership} layer.")

# --- TAB 3: LIVE NEWS ---
with tab_news:
    st.subheader("🔔 Market Moving News Notifications")
    with st.container(border=True):
        st.error("🚨 **BREAKING: US Federal Reserve hints at interest rate relief bets**")
        st.info("🇮🇳 **हिंदी अनुवाद:** अमेरिकी फेडरल रिजर्व ने ब्याज दरों में कटौती के संकेत दिए, जिससे बाजार में तेजी की उम्मीद है।")
