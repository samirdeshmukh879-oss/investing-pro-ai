import streamlit as st
import pandas as pd

# Page setup - Wide mode for premium chart view
st.set_page_config(page_title="ProPicks AI - Find Winning Stocks", layout="wide")

# Top Header matching the screenshot
st.title("🤖 ProPicks AI - Find Winning Stocks with AI")
st.caption("Next Update: Oct 1, 2026 | Stock Picks Updated: Sep 1, 2026")

# --- TOP OUTPERFORMERS BANNER ---
st.info("🇮🇳 **NIFTY20 — Bharat Market Outperformers**\n\nThis month's top 20 Indian stocks picked by our AI model based on momentum and value.")

# Unlock Stocks Button UI
st.button("🔒 Unlock Stocks Now 🚀", use_container_width=True)

# Graph section simulation (Historical Performance - Fixed Data)
st.subheader("📈 Simulated Past Performance (Nifty20 vs Nifty 50)")
chart_data = pd.DataFrame({
    'Nifty20 (AI Picked)':,
    'Nifty 50 (Benchmark)': [100, 120, 140, 180, 200, 218]
}, index=['2020', '2022', '2023', '2024', '2025', '2026'])
st.line_chart(chart_data)

# --- EXPLORE DIFFERENT STRATEGIES SECTION ---
st.markdown("---")
st.header("🎯 Explore Different AI Strategies")

# Tabs for strategy switching like the image buttons
strat_tabs = st.tabs(["All Strategies", "Popular Only"])

with strat_tabs[0]:
    # Strategy 1: Bharat Bargains
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("🟣 INB15 — Bharat Bargains")
            st.write("*Identifies undervalued Indian stocks with strong fundamentals.*")
            st.caption("🔄 Monthly Rebalancing | 📅 2019 - 2026")
        with col2:
            st.button("👁️ View Stocks", key="btn1")
            
        c1, c2 = st.columns(2)
        c1.metric(label="Total Return (1Y)", value="+4.7%")
        c2.metric(label="Total Return (5Y)", value="+475.1%", delta="Outperforming")

    # Strategy 2: Tech Titans
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("🟡 IT15 — Tech Titans")
            st.write("*Stay ahead of the latest tech trends with algorithmic picks.*")
            st.caption("🔄 Monthly Rebalancing | 📅 2013 - 2026")
        with col2:
            st.button("👁️ View Stocks", key="btn2")
            
        c1, c2 = st.columns(2)
        c1.metric(label="Total Return (1Y)", value="+23.9%")
        c2.metric(label="Total Return (5Y)", value="+116.4%")

    # Strategy 3: Beat the S&P 500 (US Market)
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("🔵 SP20 — Beat the S&P 500")
            st.write("*Picks from the S&P 500 refined by AI to outperform the US market.*")
            st.caption("🔄 Monthly Rebalancing | 📅 2013 - 2026")
        with col2:
            st.button("👁️ View Stocks", key="btn3")
            
        c1, c2 = st.columns(2)
        c1.metric(label="Total Return (1Y)", value="+8.7%")
        c2.metric(label="Total Return (5Y)", value="+74.0%")

    # Strategy 4: Bharat Small Cap Gems
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("🔴 IN9520 — Bharat Small Cap Gems")
            st.write("*Targets high-potential small-cap companies in India.*")
            st.caption("🔄 Monthly Rebalancing | 📅 2019 - 2026")
        with col2:
            st.button("👁️ View Stocks", key="btn4")
            
        c1, c2 = st.columns(2)
        c1.metric(label="Total Return (1Y)", value="+17.8%")
        c2.metric(label="Total Return (5Y)", value="+967.5%")

# --- HOW TO USE SECTION ---
st.markdown("---")
with st.expander("❓ How to Use ProPicks AI"):
    st.write("1. **Explore Strategies:** Choose a strategy that fits your style (Growth, Value, etc.).")
    st.write("2. **Generate Ideas:** Use these AI lists to find your next investment.")
    st.write("3. **Monthly Action:** Check on the 1st of every month to see which stocks to ADD or REMOVE.")

# Disclaimer Footer matching the original site
st.caption("⚠️ **Disclaimer:** The information presented in ProPicks AI Strategies is for general informational purposes only and should not be considered as investment or financial advice.")
