{
  "$schema": "https://json-schema.org",
  "title": "AssetDetailsPayload",
  "type": "object",
  "required": ["ticker", "name", "market", "asset_class", "key_metrics", "ai_indicators", "historical_graph_5y", "latest_news"],
  "properties": {
    "ticker": {
      "type": "string",
      "description": "Unique identifier code jaise AAPL ya NTPC.NS"
    },
    "name": {
      "type": "string",
      "description": "Company ya ETF ka full formal naam"
    },
    "market": {
      "type": "string",
      "enum": ["INDIAN", "US"]
    },
    "asset_class": {
      "type": "string",
      "enum": ["STOCKS", "ETFS"]
    },
    "key_metrics": {
      "type": "object",
      "required": ["market_cap", "pe_ratio", "book_value", "volume", "cmp"],
      "properties": {
        "cmp": { "type": "number", "description": "Current Market Price" },
        "market_cap": { "type": "number", "description": "Market Capitalization in local currency" },
        "pe_ratio": { "type": "number", "description": "Price to Earnings Ratio" },
        "book_value": { "type": "number", "description": "Book Value per share" },
        "volume": { "type": "integer", "description": "Current trading day volume count" }
      }
    },
    "ai_indicators": {
      "type": "object",
      "required": ["status", "buying_price", "exit_price"],
      "properties": {
        "status": { 
          "type": "string", 
          "enum": ["BUY_RECOMMENDED", "LOSS_AVOID"],
          "description": "AI prediction output category"
        },
        "buying_price": { 
          "type": ["number", "null"], 
          "description": "Monthly recommended entry point, null agar avoid list me ho" 
        },
        "exit_price": { 
          "type": ["number", "null"], 
          "description": "Predefined strict target stop-loss target, null agar clear buy ho" 
        }
      }
    },
    "historical_graph_5y": {
      "type": "array",
      "description": "5-year trend line render karne ke liye timestamps aur closing values",
      "items": {
        "type": "object",
        "required": ["timestamp", "close"],
        "properties": {
          "timestamp": { "type": "string", "format": "date", "description": "YYYY-MM-DD format" },
          "close": { "type": "number" }
        }
      }
    },
    "latest_news": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["source", "timestamp", "title_en", "title_hi"],
        "properties": {
          "source": { "type": "string", "description": "Sidekick AI, Trendlyne etc." },
          "timestamp": { "type": "string", "format": "date-time" },
          "title_en": { "type": "string", "description": "Headline in English" },
          "title_hi": { "type": "string", "description": "Headline translated in Hindi" }
        }
      }
    }
  }
}
