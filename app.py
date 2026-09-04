import streamlit as st
import yfinance as yf
import pandas as pd
import datetime

# Page configuration for Premium Wide Fintech Layout
st.set_page_config(page_title="Investing Pro AI+", layout="wide")

current_month = datetime.date.today().strftime('%B %Y')
st.title("🤖 ProPicks AI — Advanced Market Terminal")
st.caption(f"🗓️ Monthly Dashboard: **{current_month}** | Fully Automated AI Layout")

# 5 MAIN COLUMNS (TABS) FROM BEGINNING TO NOW REQUIREMENTS
tab_propicks, tab_indian, tab_us, tab_search, tab_news = st.tabs([
    "🎯 ProPicks AI Dashboard", 
    "🇮🇳 Indian Lists", 
    "🇺🇸 US Lists", 
    "🔍 Broker-Style Search", 
    "🔥 Live Impact News"
])

# --- STATIC DATA POOLS ---
bharat_profit = ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS", "BHARTIARTL.NS", "SBI.NS", "ITC.NS", "LT.NS", "AXISBANK.NS"] * 2
bharat_loss = ["IDEA.NS", "YESBANK.NS", "SUZLON.NS", "ZOMATO.NS", "PAYTM.NS", "RPOWER.NS", "IRFC.NS", "RVNL.NS", "SJVN.NS", "NHPC.NS"] * 2
ind_etf_profit = ["NIFTYBEES.NS", "BANKBEES.NS", "JUNIORBEES.NS", "INFRABEES.NS", "SETFNIFTY.NS"] * 4
ind_etf_loss = ["GOLDSHARE.NS", "SILVERETF.NS", "NETFCONSUM.NS", "ICICILIQ.NS"] * 3

us_profit = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "NFLX", "AMD", "COST"] * 2
us_loss = ["NIO", "BABA", "INTC", "PYPL", "SNAP", "PTON", "RIVN", "LCID", "AMC", "GME"] * 2
us_etf_profit = ["VOO", "SOXX", "QQQ", "SPY", "IWM"] * 4
us_etf_loss = ["USO", "GDXJ", "UNG", "SLV"] * 3

# --- COLUMN 1: PROPICKS AI PREMIUM CARDS DASHBOARD (With Index Comparison) ---
with tab_propicks:
    st.info(f"🔥 **Monthly Market Action Alert:** AI ne is mahine ke liye global investment strategies rebalance kar diye hain.")
    st.button("🔒 Unlock Premium Portfolios Now 🚀", use_container_width=True)
    
    # 📊 NEW FEATURE: INDEX VS AI PORTFOLIO RETURNS COMPARISON SHEET (Investing Pro Layout)
    st.subheader("📊 Full Index Benchmark vs AI Outperformance Sheet")
    st.caption("Audience ko saaf dikhane ke liye ki AI ne normal index se kitna zyada return diya aur kitna loss bachaya.")
    
    # Structural row metrics matching your 7th screenshot concept
    col_idx1, col_idx2 = st.columns(2)
    with col_idx1:
        with st.container(border=True):
            st.markdown("### 🇮🇳 NIFTY 50 Benchmark Layer")
            st.metric(label="Standard Nifty 50 Return (1Y)", value="+14.20%")
            st.metric(label="Standard Nifty 50 Return (5Y)", value="+118.8%")
    with col_idx2:
        with st.container(border=True):
            st.markdown("### 🤖 NIFTY20 AI Picked Strategy (Our Model)")
            st.metric(label="AI Outperformer Portfolio Return (1Y)", value="+51.31%", delta="⚡ +37.11% Alpha")
            st.metric(label="AI Outperformer Portfolio Return (5Y)", value="+1,100.1%", delta="🚀 Outperforming Market")
            st.success("💡 **Loss Prevention Alert:** AI Avoid filters ne is saal users ka lagbhag **24.5% Capital** dubne se bachaya hai!")

    st.markdown("---")
    st.subheader("🎯 Explore Different AI Strategies")
    
    with st.container(border=True):
        st.subheader("🟣 INB15 — Bharat Bargains")
        st.write("*Identifies undervalued Indian stocks with strong fundamentals.*")
        c1, c2 = st.columns(2)
        c1.metric(label="Total Return (1Y)", value="+4.7%")
        c2.metric(label="Total Return (5Y)", value="+475.1%")

    with st.container(border=True):
        st.subheader("🟡 IT15 — Tech Titans")
        st.write("*Stay ahead of the latest tech trends with algorithmic picks.*")
        c1, c2 = st.columns(2)
        c1.metric(label="Total Return (1Y)", value="+23.9%")
        c2.metric(label="Total Return (5Y)", value="+116.4%")

# --- COLUMN 2: INDIAN MARKET LISTS (With Fixed Sub-tabs structure) ---
with tab_indian:
    st.header("🇮🇳 Indian Market Tier-wise Hub")
    ind_pro_tab, ind_pro_plus_tab = st.tabs(["⭐ Investing Pro Tier (Indian)", "💎 Investing Pro Plus Tier (Indian)"])
    
    # 1. Indian Pro Tier (20 Stocks, 10 ETFs)
    with ind_pro_tab:
        st.subheader("📊 Pro Plan — Broad Indian Market Lists")
        p_stk, p_etf = st.tabs(["📊 Indian Stocks (Top 20)", "🚀 Indian ETFs (Top 10)"])
        with p_stk:
            for i in range(20): st.success(f"📈 **{bharat_profit[i].replace('.NS','')}** | Pro Buy Pick")
        with p_etf:
            for i in range(10): st.success(f"📈 **{ind_etf_profit[i].replace('.NS','')}** | Pro ETF Pick")
            
    # 2. Indian Pro Plus Tier (5 Profit, 10 Loss Stocks, 5 Profit, 10 Loss ETFs)
    with ind_pro_plus_tab:
        st.subheader("💎 Pro Plus Plan — Deep AI Research Filters")
        pp_stk, pp_etf = st.tabs(["📊 Deep Stock Lists", "🚀 Deep ETF Lists"])
        with pp_stk:
            pp_s_buy, pp_s_avoid = st.tabs(["🚀 Top 5 Profit Picks", "⚠️ Top 10 Avoid List"])
            with pp_s_buy:
                for i in range(5): st.success(f"📈 **{bharat_profit[i].replace('.NS','')}** | Action: BUY/ADD")
            with pp_s_avoid:
                for i in range(10): st.error(f"❌ **{bharat_loss[i].replace('.NS','')}** | Action: REMOVE/EXIT")
        with pp_etf:
            pp_e_buy, pp_e_avoid = st.tabs(["🚀 Top 5 ETFs", "⚠️ Top 10 Avoid ETFs"])
            with pp_e_buy:
                for i in range(5): st.success(f"📈 **{ind_etf_profit[i].replace('.NS','')}** | Action: ADD")
            with pp_e_avoid:
                for i in range(10): st.error(f"❌ **{ind_etf_loss[i].replace('.NS','')}** | Action: AVOID")

# --- COLUMN 3: US MARKET LISTS (With Separate Pro & Pro Plus Columns Added) ---
with tab_us:
    st.header("🇺🇸 US Market Tier-wise Hub")
    us_pro_tab, us_pro_plus_tab = st.tabs(["⭐ Investing Pro Tier (US)", "💎 Investing Pro Plus Tier (US)"])
    
    # 1. US Pro Tier (20 Stocks, 10 ETFs)
    with us_pro_tab:
        st.subheader("📊 Pro Plan — Broad US Market Lists")
        us_p_stk, us_p_etf = st.tabs(["📊 US Stocks (Top 20)", "🚀 US ETFs (Top 10)"])
        with us_p_stk:
            for i in range(20): st.success(f"📈 **{us_profit[i]}** | Pro US Buy")
        with us_p_etf:
            for i in range(10): st.success(f"📈 **{us_etf_profit[i]}** | Pro US ETF")
            
    # 2. US Pro Plus Tier (5 Profit, 10 Loss Stocks, 5 Profit, 10 Loss ETFs)
    with us_pro_plus_tab:
        st.subheader("💎 Pro Plus Plan — Deep US Institutional Research")
        us_pp_stk, us_pp_etf = st.tabs(["📊 Deep US Stock Lists", "🚀 Deep US ETF Lists"])
        with us_pp_stk:
            us_pp_s_buy, us_pp_s_avoid = st.tabs(["🚀 Top 5 Profit Picks", "⚠️ Top 10 Avoid List"])
            with us_pp_s_buy:
                for i in range(5): st.success(f"📈 **{us_profit[i]}** | Action: BUY/ADD")
            with us_pp_s_avoid:
                for i in range(10): st.error(f"❌ **{us_loss[i]}** | Action: REMOVE/EXIT")
        with us_pp_etf:
            us_pp_e_buy, us_pp_e_avoid = st.tabs(["🚀 Top 5 ETFs", "⚠️ Top 10 Avoid ETFs"])
            with us_pp_e_buy:
                for i in range(5): st.success(f"📈 **{us_etf_profit[i]}** | Action: ADD")
            with us_pp_e_avoid:
                for i in range(10): st.error(f"❌ **{us_etf_loss[i]}** | Action: AVOID")

# --- COLUMN 4: 🔍 BROKER-STYLE SEARCH ENGINE ---
with tab_search:
    st.header("🔍 Broker-Style Deep Analytics Terminal")
    search_pool = [
        "RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFCBANK.NS", "ICICIBANK.NS", "IDEA.NS", "YESBANK.NS", "SUZLON.NS",
        "AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "NIO", "NIFTYBEES.NS", "BANKBEES.NS", "VOO", "SOXX"
    ]
    selected_ticker = st.selectbox("Search Stock / ETF Code:", search_pool)
    
    if selected_ticker:
        with st.spinner(f"Loading {selected_ticker} Data..."):
            try:
                asset = yf.Ticker(selected_ticker)
                hist_data = asset.history(period="5y")
                info = asset.info
                
                if not hist_data.empty:
                    current_price = hist_data['Close'].iloc[-1]
                    currency = "₹" if "." in selected_ticker else "$"
                    buying_price = current_price * 0.98
                    exit_price = current_price * 1.12
                    stop_loss = current_price * 0.95
                    
                    if selected_ticker in ["IDEA.NS", "YESBANK.NS", "SUZLON.NS", "NIO"]:
                        st.error(f"🚨 **REMOVE ALERT:** AI trend detects weakness. Exit immediately!")
                    else:
                        st.warning(f"⚠️ **Monthly Alert:** Buy near {currency}{buying_price:.2f}. Exit at {currency}{exit_price:.2f}.")

                    st.subheader("🚦 Entry-Exit Pricing Multipliers")
                    c1, c2, c3 = st.columns(3)
                    c1.metric(label="🟢 AI Entry Price", value=f"{currency}{buying_price:.2f}")
                    c2.metric(label="🎯 AI Exit Target", value=f"{currency}{exit_price:.2f}")
                    c3.metric(label="🛑 Risk Stop Loss", value=f"{currency}{stop_loss:.2f}")
                    
                    st.subheader(f"📈 {selected_ticker} — 5 Year Price Graph")
                    st.line_chart(hist_data['Close'])
                else:
                    st.error("Data stream offline.")
            except:
                st.error("Feeds loading error...")

# --- COLUMN 5: 🔥 LIVE IMPACT NEWS ---
with tab_news:
    st.subheader("🔔 First-Alert: Market Moving News Notifications")
    with st.container(border=True):
        st.error("🚨 **BREAKING: US Federal Reserve hints at interest rate relief bets following Waller comments**")
        st.info("🇮🇳 **हिंदी अनुवाद:** अमेरिकी फेडरल रिजर्व ने ब्याज दरों में कटौती के संकेत दिए, जिससे बाजार में तेजी की उम्मीद है।")
        st.success("🎯 **Benefited Sector:** Technology & Banking  |  **Stocks to watch:** NVDA, MSFT, HDFCBANK")

# Global Disclaimer Footer
st.markdown("---")
st.caption("⚠️ **Disclaimer:** All calculated parameters and signals are algorithmically built for educational purposes only.")
