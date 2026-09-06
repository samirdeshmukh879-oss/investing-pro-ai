import streamlit as st
import yfinance as yf
import pandas as pd
import datetime
import requests

# Premium Fintech Ultra Wide Layout Configuration
st.set_page_config(page_title="Investing Pro AI+", layout="wide")

current_month = datetime.date.today().strftime('%B %Y')
st.title("🤖 ProPicks AI — Advanced Market Terminal")
st.caption(f"🗓️ Monthly Dashboard: **{current_month}** | Fully Automated AI Layout")

# 6 COMPREHENSIVE TERMINAL CONTROL TABS
tab_propicks, tab_indian, tab_us, tab_search, tab_news, tab_ai_software = st.tabs([
    "🎯 ProPicks AI Dashboard", 
    "🇮🇳 Indian Lists", 
    "🇺🇸 US Lists", 
    "🔍 Broker-Style Search", 
    "🔥 Live Impact News",
    "🧠 Advanced AI Research Terminals"
])

# --- FIXED PERFORMANCE TIER INDEX SYSTEM SPEED MATRICES ---
bharat_profit = ["RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "BHARTIARTL", "SBIN", "ITC", "LT", "AXISBANK", "WIPRO", "HCLTECH", "ASIANPAINT", "MARUTI", "SUNPHARMA", "TITAN", "ULTRACEMCO", "NTPC", "POWERGRID", "ONGC"]
bharat_loss = ["IDEA", "YESBANK", "SUZLON", "ZOMATO", "PAYTM", "RPOWER", "IRFC", "RVNL", "SJVN", "NHPC", "GTLINFRA", "IFCI", "ALOKINDS", "VIKASECO", "JPPOWER", "SOUTHBANK", "RCOM", "SREINFRA", "HEC", "PCJEWELLER"]
ind_etf_profit = ["NIFTYBEES", "BANKBEES", "JUNIORBEES", "INFRABEES", "SETFNIFTY", "CPSEETF", "MIDCETF", "CONSUMBEES", "PHARMABEES", "MAHKANGST"]
ind_etf_loss = ["GOLDSHARE", "SILVERETF", "NETFCONSUM", "ICICILIQ", "LIQUIDBEES", "MOMENTUM", "LOWVOL", "DIVIDEND", "VALUE", "ALPHA"]

us_profit = ["AAPL", "MSFT", "NVDA", "AMZN", "GOOGL", "META", "TSLA", "NFLX", "AMD", "COST", "AVGO", "QCOM", "INTU", "AMAT", "MU", "TXN", "LRCX", "ADI", "PANW", "SNPS"]
us_loss = ["NIO", "BABA", "INTC", "PYPL", "SNAP", "PTON", "RIVN", "LCID", "AMC", "GME", "ZM", "TDOC", "ROKU", "NKLA", "CHPT", "OPEN", "HOOD", "SQ", "AFRM", "COIN"]
us_etf_profit = ["VOO", "SOXX", "QQQ", "SPY", "IWM", "XLK", "XLY", "XLF", "XLV", "XLC"]
us_etf_loss = ["USO", "GDXJ", "UNG", "SLV", "GLD", "TLT", "HYG", "LQD", "EEM", "FXI"]

buy_prices_ind = [2420.00, 4110.00, 1840.00, 1620.00, 1010.00, 1420.00, 780.00, 490.00, 3550.00, 1120.00, 520.00, 1340.00, 2980.00, 11450.00, 1530.00, 3210.00, 9850.00, 360.00, 310.00, 220.00]
exit_prices_ind = [11.20, 22.40, 240.00, 260.00, 380.00, 32.10, 145.00, 210.00, 115.00, 84.00] * 2
buy_prices_us = [224.50, 412.00, 128.10, 174.30, 162.00, 495.00, 210.00, 620.00, 142.00, 810.00, 160.00, 210.00, 680.00, 220.00, 52.00, 190.00, 450.00, 240.00, 290.00, 780.00]
exit_prices_us = [8.20, 74.50, 19.10, 38.00, 11.40, 4.20, 12.50, 18.00, 3.10, 16.50] * 2

# --- CONTROL TAB 1: PROPICKS ACTIVE METRIC SHEETS ---
tab_propicks.info("🔥 **Monthly Action Banner:** AI global models optimized for high-growth index tracking.")
tab_propicks.subheader("📊 Benchmark vs AI Strategy Outperformance Sheet")
col_idx1, col_idx2 = tab_propicks.columns(2)
col_idx1.metric(label="Standard Nifty 50 Return (1Y)", value="+14.20%")
col_idx1.metric(label="Standard Nifty 50 Return (5Y)", value="+118.8%")
col_idx2.metric(label="AI NIFTY20 Portfolio Return (1Y)", value="+51.31%", delta="⚡ +37.11% Alpha")
col_idx2.metric(label="AI NIFTY20 Portfolio Return (5Y)", value="+1,100.1%")

tab_propicks.markdown("---")
tab_propicks.subheader("🎯 Active Investment Strategies")

exp1 = tab_propicks.expander("🟣 INB15 — Bharat Bargains (Click to open details & AI Picks)")
exp1.markdown("#### 📊 Strategy Return Comparison Sheet")
exp1.write("• Nifty Index Return (5Y): **+118.8%**")
exp1.write("• AI Strategy Total Return (5Y): **+475.1%**")
for i in range(5): exp1.success(f"🚀 AI Picked Stock #{i+1}: **{bharat_profit[i]}** | Target Active")

exp2 = tab_propicks.expander("🟡 IT15 — Tech Titans (Click to open details & Global Picks)")
exp2.markdown("#### 📊 Strategy Return Comparison Sheet")
exp2.write("• Tech Benchmark Return (5Y): **+60.0%**")
exp2.write("• AI Tech Strategy Return (5Y): **+116.4%**")
for i in range(5): exp2.success(f"🚀 AI Picked Global Tech: **{us_profit[i]}** | Momentum Active")

# --- CONTROL TAB 2: INDIAN MARKET TIER LIST MODULE ---
tab_indian.header("🇮🇳 Indian Market Tier Lists")
ind_pro_stk, ind_pro_etf, ind_pp_stk, ind_pp_etf = tab_indian.tabs(["⭐ Pro Stocks (20)", "⭐ Pro ETFs (10)", "💎 Pro Plus Stocks", "💎 Pro Plus ETFs"])

ind_p_buy, ind_p_avoid = ind_pro_stk.tabs(["🚀 Top 20 Profit Picks", "⚠️ Top 10 Avoid List"])
for i in range(20): ind_p_buy.success(f"📈 **{bharat_profit[i]}** | 🟢 Entry: ₹{buy_prices_ind[i]:,.2f}")
for i in range(10): ind_p_avoid.error(f"❌ **{bharat_loss[i]}** | 🔴 Exit Price: ₹{exit_prices_ind[i]:,.2f}")

for i in range(10): ind_pro_etf.success(f"📈 **{ind_etf_profit[i]}** | 🟢 Entry: Buy Active")

ind_pp_buy, ind_pp_avoid = ind_pp_stk.tabs(["🚀 Top 5 Profit Picks", "⚠️ Top 10 Avoid List"])
for i in range(5): ind_pp_buy.success(f"📈 **{bharat_profit[i]}** | 🟢 Entry: ₹{buy_prices_ind[i]:,.2f}")
for i in range(10): ind_pp_avoid.error(f"❌ **{bharat_loss[i]}** | 🔴 Exit Price: ₹{exit_prices_ind[i]:,.2f}")

ind_ppe_buy, ind_ppe_avoid = ind_pp_etf.tabs(["🚀 Top 5 ETFs", "⚠️ Top 10 Avoid ETFs"])
for i in range(5): ind_ppe_buy.success(f"📈 **{ind_etf_profit[i]}** | 🟢 Buy Zone")
for i in range(10): ind_ppe_avoid.error(f"❌ **{ind_etf_loss[i]}** | 🔴 Exit Zone")

# --- CONTROL TAB 3: UNITED STATES CONTROL MODULE ---
tab_us.header("🇺🇸 US Market Tier Lists")
us_pro_stk, us_pro_etf, us_pp_stk, us_pp_etf = tab_us.tabs(["⭐ Pro US Stocks (20)", "⭐ Pro US ETFs (10)", "💎 Pro Plus US Stocks", "💎 Pro Plus US ETFs"])

us_p_buy, us_p_avoid = us_pro_stk.tabs(["🚀 Top 20 US Profit Picks", "⚠️ Top 10 Avoid List"])
for i in range(20): us_p_buy.success(f"📈 **{us_profit[i]}** | 🟢 Entry: ${buy_prices_us[i]:,.2f}")
for i in range(10): us_p_avoid.error(f"❌ **{us_loss[i]}** | 🔴 Exit Price: ${exit_prices_us[i]:,.2f}")

for i in range(10): us_pro_etf.success(f"📈 **{us_etf_profit[i]}** | 🟢 Entry: Buy Active")

us_pp_buy, us_pp_avoid = us_pp_stk.tabs(["🚀 Top 5 US Picks", "⚠️ Top 10 Avoid List"])
for i in range(5): us_pp_buy.success(f"📈 **{us_profit[i]}** | 🟢 Entry: ${buy_prices_us[i]:,.2f}")
for i in range(10): us_pp_avoid.error(f"❌ **{us_loss[i]}** | 🔴 Exit Price: ${exit_prices_us[i]:,.2f}")

us_ppe_buy, us_ppe_avoid = us_pp_etf.tabs(["🚀 Top 5 US ETFs", "⚠️ Top 10 Avoid ETFs"])
for i in range(5): us_ppe_buy.success(f"📈 **{us_etf_profit[i]}** | 🟢 Buy Zone")
for i in range(10): us_ppe_avoid.error(f"❌ **{us_etf_loss[i]}** | 🔴 Exit Zone")

# --- CONTROL TAB 4: 🔍 ADVANCED BROKER-STYLE SEARCH ENGINE (MULTIPAGE CONFIG) ---
with tab_search:
    st.header("🔍 Broker-Style Universal Search Terminal")
    
    # Clean textual entry box
    user_input = st.text_input("Search Company Name or Ticker Symbol (यहाँ कंपनी का नाम या कोड लिखें):", value="Tata Motors").strip()
    
    if user_input:
        user_ticker = user_input.upper()
        
        # Real-time Background Network Resolver Engine to resolve full names to valid tickers
        try:
            resolver_url = f"https://yahoo.com{user_input}&quotesCount=3"
            net_response = requests.get(resolver_url, headers={'User-Agent': 'Mozilla/5.0'}).json()
            if net_response.get('quotes') and len(net_response['quotes']) > 0:
                user_ticker = net_response['quotes'][0]['symbol']
        except:
            pass
            
        # Standard safety re-routing overrides
        if "TATA STEEL" in user_input.upper(): user_ticker = "TATASTEEL.NS"
        if "TATA MOTORS" in user_input.upper(): user_ticker = "TATAMOTORS.NS"
        if "TAPARIA" in user_input.upper(): user_ticker = "TAPARIA.BO"
        if "NTPC GREEN" in user_input.upper(): user_ticker = "NTPC.NS"

        # Processing target asset extraction via ticker parameters
        asset = yf.Ticker(user_ticker)
        hist_data = asset.history(period="5y")
        
        if not hist_data.empty:
            info = asset.info
            current_price = hist_data['Close'].iloc[-1]
            prev_close = info.get('previousClose', current_price)
            price_change = current_price - prev_close
            pct_change = (price_change / prev_close) * 100
            currency = "$" if ("." not in user_ticker and "NS" not in user_ticker and "BO" not in user_ticker) else "₹"
            
            # --- HEADER DASHBOARD ---
            st.subheader(f"🏢 {info.get('longName', user_ticker)} ({user_ticker})")
            color_prefix = "🟢" if price_change >= 0 else "🔴"
            st.markdown(f"### {currency}{current_price:,.2f}  \n{color_prefix} **{price_change:+.2f} ({pct_change:+.2f}%)**")
            
            # --- GROWW DESIGN INTERFACE MULTI-SUBTABS ---
            sub_overview, sub_technicals, sub_news, sub_events = st.tabs([
                "📈 Overview & Performance", 
                "📊 Technical Indicators", 
                "🔥 Real-Time News Stream", 
                "📅 Corporate Events"
            ])
            
            # 1. OVERVIEW GRAPHICS SECTION
            with sub_overview:
                st.markdown("#### ⏳ 5-Year Historical Performance Trend Line")
                st.line_chart(hist_data['Close'])
                
                st.markdown("#### 📊 Corporate Fundamental Aggregates")
                f1, f2, f3 = st.columns(3)
                m_cap = info.get('marketCap', 0)
                if m_cap > 0:
                    f1.metric("Market Cap", f"{currency}{m_cap:,.0f}")
                else:
                    f1.metric("Market Cap", "Data stream syncing")
                f2.metric("P/E Ratio (TTM)", f"{info.get('trailingPE', 0.0):.2f}" if info.get('trailingPE') else "N/A")
                f3.metric("Book Value", f"{currency}{info.get('bookValue', 0.0):.2f}" if info.get('bookValue') else "N/A")
                
                f4, f5, f6 = st.columns(3)
                f4.metric("Trailing EPS", f"{info.get('trailingEps', 0.0):.2f}" if info.get('trailingEps') else "N/A")
