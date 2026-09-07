import requests
import json
import time

class AIInvestingAppBackend:
    def __init__(self, api_base_url, api_key):
        self.base_url = api_base_url
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def get_market_signals(self, market_type="INDIAN", asset_type="STOCKS", tier="PRO"):
        """
        AI platform se Gainers (Profit) aur Losers (Avoid List) ke live signals fetch karne ke liye.
        market_type: 'INDIAN' ya 'US'
        asset_type: 'STOCKS' ya 'ETFS'
        tier: 'PRO' ya 'PRO_PLUS'
        """
        endpoint = f"{self.base_url}/v1/market/signals"
        params = {
            "market": market_type,
            "asset_class": asset_type,
            "tier": tier
        }
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params, timeout=10)
            if response.status_code == 200:
                return response.json() # Returns full lists of gainers & avoid stocks
            else:
                print(f"API Error [{response.status_code}]: {response.text}")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Connection Failed: {e}")
            return None

    def get_stock_analytics(self, ticker_code):
        """
        Jab koi user specific stock par click karega, tab asset details page ka data load karne ke liye.
        Isme 5-year graph coordinate data, Market Cap, P/E, aur Buying/Exit prices milenge.
        """
        endpoint = f"{self.base_url}/v1/stocks/{ticker_code}/analytics"
        
        try:
            response = requests.get(endpoint, headers=self.headers, timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error fetching detail for {ticker_code}: {e}")
            return None

# ==========================================
# TESTING THE CODE STRUCTURE (EXAMPLE USAGE)
# ==========================================
if __name__ == "__main__":
    # Example Configuration (Apne actual AI Provider ka URL aur Key dalein)
    API_URL = "https://ai-stock-provider.com"
    API_KEY = "sk_live_your_actual_api_key_here"

    # Backend Initialize karein
    app_backend = AIInvestingAppBackend(api_base_url=API_URL, api_key=API_KEY)

    print("--- Fetching Indian Market Pro Tier Stocks ---")
    # Indian market ke Pro tier stocks ke signals call karein
    indian_pro_stocks = app_backend.get_market_signals(market_type="INDIAN", asset_type="STOCKS", tier="PRO")
    
    if indian_pro_stocks:
        print("Data Received Successfully!")
        # Print sample structure of response
        print(json.dumps(indian_pro_stocks, indent=2)[:500] + "...\n[Truncated]")

    print("\n--- Fetching Detailed Asset Analytics for Clicked Ticker ---")
    # Maan lijiye user ne kisi specific stock (e.g., RELIANCE) par click kiya
    reliance_details = app_backend.get_stock_analytics(ticker_code="RELIANCE")
    
    if reliance_details:
        print("Asset Detail Page Data Loaded!")
        print(json.dumps(reliance_details, indent=2)[:500] + "...\n[Truncated]")
