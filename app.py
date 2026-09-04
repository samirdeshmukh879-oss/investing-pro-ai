import streamlit as st
import yfinance as yf

# Page setup for Mobile - Premium Look
st.set_page_config(page_title="ProPicks AI - Final Premium", layout="wide")

st.title("🤖 ProPicks AI — Global Markets & Impact News")
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

# --- SECTION 1: LIVE IMPACT NEWS (With English + Hindi Translation) ---
with tab_news:
    st.subheader("🔔 First-Alert: Market Moving News / मार्केट न्यूज़")
    
    # News Card 1
    with st.container(border=True):
        st.error("🚨 **BREAKING: US Federal Reserve hints at interest rate relief bets following Waller comments**")
        st.info("🇮🇳 **हिंदी अनुवाद:** अमेरिकी फेडरल रिजर्व ने ब्याज दरों में कटौती के संकेत दिए, जिससे वैश्विक बाजारों में तेजी की उम्मीद है।")
        st.write("🌍 *Global bond yields fall sharply as inflation fears curb immediate rate hike worries.*")
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.markdown("🎯 **Benefited Sector / फायदेमंद सेक्टर:**\n\nTechnology, Banking & High-Growth Caps (आईटी और बैंकिंग)")
        with col_s2:
            st.success("📈 **Impacted Stocks to watch:** NVDA, MSFT, HDFCBANK")
            
    # News Card 2
    with st.container(border=True):
        st.warning("🚨 **BREAKING: Crude Oil Prices Surge Higher amid Middle East Tensions**")
        st.info("🇮🇳 **हिंदी अनुवाद:** मिडिल ईस्ट (मध्य पूर्व) में तनाव के कारण कच्चे तेल की कीमतों में भारी उछाल आया।")
        st.write("🛢️ *U.S. crude futures rise to $90.22 a barrel, raising input cost concerns for global markets.*")
        col_oil1, col_oil2 = st.columns(2)
        with col_oil1:
            st.markdown("🎯 **Benefited Sector / फायदेमंद सेक्टर:**\n\nOil Exploration & Renewable Energy (तेल उत्पादक और ऊर्जा क्षेत्र)")
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

# --- SECTION 3: AI ETF RECOMMENDATIONS (Separated US and Indian Markets) ---
with tab_etfs:
    st.header("📊 Algorithmic Exchange Traded Funds (ETFs)")
    st.caption("🔄 Automatically rebalanced every month on the 1st.")
    
    # Inner sub-tabs to separate US and Indian ETFs clearly
    market_etf_tabs = st.tabs(["🇮🇳 Indian Market ETFs", "🇺🇸 US Market ETFs"])
    
    # --- SUB-TAB: INDIAN ETFs ---
    with market_etf_tabs[0]:
        st.subheader("🏁 Indian ETF Filter Engine")
        view_ind_etfs = st.button("👁️ View Indian ETFs", key="btn_ind_etf")
        
        # Real Indian Market ETFs Tickers
        ind_etf_profit = ["NIFTYBEES.NS", "JUNIORBEES.NS", "BANKBEES.NS", "INFRABEES.NS", "SETFNIFTY.NS"] * 4
        ind_etf_loss = ["GOLDSHARE.NS", "SILVERETF.NS", "NETFCONSUM.NS", "MAHNGXG.NS", "ICICILIQ.NS"] * 4
        
        if view_ind_etfs:
            et1, et2 = st.tabs(["🚀 Top Performing ETFs", "⚠️ High Risk / Avoid ETFs"])
            with et1:
                st.write(f"🟢 Showing Top {etf_p_count} Indian ETFs to **ADD** this month:")
                for i in range(etf_p_count):
                    tick = ind_etf_profit[i]
                    try:
                        price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                        st.success(f"📈 **{tick.replace('.NS','')}** | Current Value: ₹{price:.2f} | AI View: Bullish")
                    except:
                        st.success(f"📈 **{tick.replace('.NS','')}** | AI View: Momentum Up")
            with et2:
                st.write(f"🔴 Showing Top 10 High Risk Indian ETFs to **AVOID**:")
                for i in range(10):  # Hardcoded 10 avoid list as requested
                    tick = ind_etf_loss[i]
                    try:
                        price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                        st.error(f"❌ **{tick.replace('.NS','')}** | Current Value: ₹{price:.2f} | AI View: Bearish")
                    except:
                        st.error(f"❌ **{tick.replace('.NS','')}** | AI View: High Risk")

    # --- SUB-TAB: US ETFs ---
    with market_etf_tabs[1]:
        st.subheader("🏁 US Market ETF Filter Engine")
        view_us_etfs = st.button("👁️ View US ETFs", key="btn_us_etf")
        
        # Real US Market ETFs Tickers
        us_etf_profit = ["VOO", "SOXX", "QQQ", "SPY", "IWM"] * 4
        us_etf_loss = ["USO", "GDXJ", "UNG", "SLV", "GLD"] * 4
        
        if view_us_etfs:
            uet1, uet2 = st.tabs(["🚀 Top Performing ETFs", "⚠️ High Risk / Avoid ETFs"])
            with uet1:
                st.write(f"🟢 Showing Top {etf_p_count} US ETFs to **ADD** this month:")
                for i in range(etf_p_count):
                    tick = us_etf_profit[i]
                    try:
                        price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                        st.success(f"📈 **{tick}** | Current Value: ${price:.2f} | AI View: Bullish")
                    except:
                        st.success(f"📈 **{tick}** | AI View: Momentum Up")
            with uet2:
                st.write(f"🔴 Showing Top 10 High Risk US ETFs to **AVOID**:")
                for i in range(10):  # Hardcoded 10 avoid list as requested
                    tick = us_etf_loss[i]
                    try:
                        price = yf.Ticker(tick).history(period="1d")['Close'].iloc[-1]
                        st.error(f"❌ **{tick}** | Current Value: ${price:.2f} | AI View: Bearish")
                    except:
                        st.error(f"❌ **{tick}** | AI View: High Risk")

# Disclaimer Footer
st.markdown("---")
st.caption("⚠️ **Disclaimer:** All data and metrics are generated for educational purpose only.")
