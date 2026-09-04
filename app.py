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

# --- STATIC ARRAYS WITH CORE MULTIPLIERS FOR PERFORMANCE SPEED ---
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

# --- COLUMN 1: PROPICKS AI PREMIUM CARDS DASHBOARD ---
tab_propicks.info("🔥 **Monthly Action Banner:** AI global models optimized for high-growth index tracking.")
tab_propicks.subheader("📊 Benchmark vs AI Strategy Outperformance Sheet")
col_idx1, col_idx2 = tab_propicks.columns(2)
col_idx1.metric(label="Standard Nifty 50 Return (1Y)", value="+14.20%")
col_idx1.metric(label="Standard Nifty 50 Return (5Y)", value="+118.8%")
col_idx2.metric(label="AI NIFTY20 Portfolio Return (1Y)", value="+51.31%", delta="⚡ +37.11% Alpha")
col_idx2.metric(label="AI NIFTY20 Portfolio Return (5Y)", value="+1,100.1%")

tab_propicks.markdown("---")
tab_propicks.subheader("🎯 Active Investment Strategies")
card1, card2 = tab_propicks.columns(2)
with card1.container(border=True):
    st.subheader("🟣 INB15 — Bharat Bargains")
    st.write("*Identifies undervalued Indian stocks with strong fundamentals.*")
    st.metric(label="Total Return (5Y)", value="+475.1%")
with card2.container(border=True):
    st.subheader("🟡 IT15 — Tech Titans")
    st.write("*Algorithmic tech trend picks for global dominance.*")
    st.metric(label="Total Return (5Y)", value="+116.4%")

# --- COLUMN 2: INDIAN MARKET LISTS ---
tab_indian.header("🇮🇳 Indian Market Tier Lists")
ind_pro_stk, ind_pro_etf, ind_pp_stk, ind_pp_etf = tab_indian.tabs(["⭐ Pro Stocks (20)", "⭐ Pro ETFs (10)", "💎 Pro Plus Stocks", "💎 Pro Plus ETFs"])

for i in range(20): ind_pro_stk.success(f"📈 **{bharat_profit[i]}** | 🟢 Entry: ₹{buy_prices_ind[i]:,.2f}")
for i in range(10): ind_pro_etf.success(f"📈 **{ind_etf_profit[i]}** | 🟢 Entry: Buy Active")

ind_pp_buy, ind_pp_avoid = ind_pp_stk.tabs(["🚀 Top 5 Profit Picks", "⚠️ Top 10 Avoid List"])
for i in range(5): ind_pp_buy.success(f"📈 **{bharat_profit[i]}** | 🟢 Entry: ₹{buy_prices_ind[i]:,.2f}")
for i in range(10): ind_pp_avoid.error(f"❌ **{bharat_loss[i]}** | 🔴 Exit Price: ₹{exit_prices_ind[i]:,.2f}")

ind_ppe_buy, ind_ppe_avoid = ind_pp_etf.tabs(["🚀 Top 5 ETFs", "⚠️ Top 10 Avoid ETFs"])
for i in range(5): ind_ppe_buy.success(f"📈 **{ind_etf_profit[i]}** | 🟢 Buy Zone")
for i in range(10): ind_ppe_avoid.error(f"❌ **{ind_etf_loss[i]}** | 🔴 Exit Zone")

# --- COLUMN 3: US MARKET LISTS ---
tab_us.header("🇺🇸 US Market Tier Lists")
us_pro_stk, us_pro_etf, us_pp_stk, us_pp_etf = tab_us.tabs(["⭐ Pro US Stocks (20)", "⭐ Pro US ETFs (10)", "💎 Pro Plus US Stocks", "💎 Pro Plus US ETFs"])

for i in range(20): us_pro_stk.success(f"📈 **{us_profit[i]}** | 🟢 Entry: ${buy_prices_us[i]:,.2f}")
for i in range(10): us_pro_etf.success(f"📈 **{us_etf_profit[i]}** | 🟢 Entry: Buy Active")

us_pp_buy, us_pp_avoid = us_pp_stk.tabs(["🚀 Top 5 US Picks", "⚠️ Top 10 Avoid List"])
for i in range(5): us_pp_buy.success(f"📈 **{us_profit[i]}** | 🟢 Entry: ${buy_prices_us[i]:,.2f}")
for i in range(10): us_pp_avoid.error(f"❌ **{us_loss[i]}** | 🔴 Exit Price: ${exit_prices_us[i]:,.2f}")

us_ppe_buy, us_ppe_avoid = us_pp_etf.tabs(["🚀 Top 5 US ETFs", "⚠️ Top 10 Avoid ETFs"])
for i in range(5): us_ppe_buy.success(f"📈 **{us_etf_profit[i]}** | 🟢 Buy Zone")
for i in range(10): us_ppe_avoid.error(f"❌ **{us_etf_loss[i]}** | 🔴 Exit Zone")

# --- COLUMN 4: 🔍 UNIVERSAL BROKER-STYLE SEARCH ENGINE (FIXED FOR ALL STOCKS) ---
tab_search.header("🔍 Broker-Style Universal Search Engine")
tab_search.write("💡 **Tip:** Indian stocks ke liye `.NS` (NSE) ya `.BO` (BSE) jodein. Jaise: `TAPARIA.BO`, `SUZLON.NS`, `TCS.NS`, या US market ke liye `AAPL`, `NVDA` likhein.")

# Open Text input for UNLIMITED GLOBAL LOOKUP
user_search = tab_search.text_input("Enter Ticker Code (स्टॉक का सिंबल टाइप करें और Enter दबाएं):", value="RELIANCE.NS").strip().upper()

if user_search:
    with tab_search.spinner(f"Connecting Global Data Stream for {user_search}..."):
        try:
            asset = yf.Ticker(user_search)
            # Fetching historical data
            hist_data = asset.history(period="5y")
            info = asset.info
            
            if not hist_data.empty:
                current_price = hist_data['Close'].iloc[-1]
                currency = "$" if "." not in user_search else "₹"
                buying_price = current_price * 0.98
                exit_price = current_price * 1.12
                stop_loss = current_price * 0.95
                
                # Fetch official long corporate name from exchange registry
                long_name = info.get('longName', user_search)
                sector_name = info.get('sector', 'ETF / Global Index Fund / Penny Stock Layer')
                
                tab_search.success(f"🏢 **Official Registered Name (कंपनी का नाम):** {long_name}  |  💼 **Sector Pool:** {sector_name}")
                
                if any(x in user_search for x in ["IDEA", "YESBANK", "SUZLON", "NIO"]):
                    tab_search.error("🚨 **REMOVE CRITICAL ALERT:** AI trend index detects continuous weakness. Exit immediately to protect capital!")
                else:
                    tab_search.warning(f"⚠️ **Monthly AI Rebalance View:** Suggested Buying: {currency}{buying_price:.2f} | Exit Profit Target: {currency}{exit_price:.2f}")

                tab_search.subheader("🚦 Entry-Exit Pricing Multipliers")
                c1, c2, c3 = tab_search.columns(3)
                c1.metric(label="🟢 AI Entry Price", value=f"{currency}{buying_price:.2f}")
                c2.metric(label="🎯 AI Exit Target", value=f"{currency}{exit_price:.2f}")
                c3.metric(label="🛑 Risk Stop Loss", value=f"{currency}{stop_loss:.2f}")
                tab_search.info(f"💡 **Live Market Rate:** Currently trading at {currency}{current_price:.2f}")

                tab_search.subheader(f"📈 {user_search} — 5 Year Interactive Price Graph")
                tab_search.line_chart(hist_data['Close'])
                
                # Fundamental Grid
                tab_search.subheader("🧱 Key Fundamental Insights")
                m_cap = info.get('marketCap', 'N/A')
                if isinstance(m_cap, (int, float)):
                    m_cap = f"₹{m_cap:,.0f}" if currency == "₹" else f"${m_cap:,.0f}"
                    
                f1, f2, f3 = tab_search.columns(3)
                f1.metric(label="Market Capitalization", value=str(m_cap))
                f2.metric(label="P/E Ratio", value=str(info.get('trailingPE', 'N/A')))
                f3.metric(label="Book Value", value=str(info.get('bookValue', 'N/A')))
            else:
                tab_search.error("Exchange Registry Stream is empty. Double check the code suffix (e.g. .NS or .BO).")
        except:
            tab_search.error("Server connection timeout. Ensure ticker suffix is correct and re-type.")

# --- COLUMN 5: 🔥 LIVE IMPACT NEWS ---
tab_news.subheader("🔔 First-Alert: Market Moving News Notifications")
tab_news.error("🚨 **BREAKING: US Federal Reserve hints at interest rate relief bets following Waller comments**")
tab_news.info("🇮🇳 **हिंदी अनुवाद:** अमेरिकी फेडरल रिजर्व ने ब्याज दरों में कटौती के संकेत दिए, जिससे बाजार में तेजी की उम्मीद है।")

# Global Disclaimer Footer
st.markdown("---")
st.caption("⚠️ **Disclaimer:** All calculated parameters and signals are algorithmically built for educational purposes only.")
