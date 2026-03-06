# MacroLens: AI Market Intelligence Dashboard

An AI-powered dashboard that aggregates financial news, summarizes macro events, predicts likely market effects on equities, commodities, and currencies, and visualizes related asset movements through interactive charts.

## Overview

MacroLens helps traders, analysts, and investors stay ahead of market-moving events by:
- **Fetching** latest financial news from Finnhub
- **Summarizing** articles with AI (OpenAI GPT-4o-mini)
- **Predicting** market impact (Bullish/Bearish/Neutral)
- **Identifying** affected assets with confidence scores
- **Visualizing** price movements with interactive Plotly charts

This is a decision-support analytics tool for understanding market events—**not** a price prediction or trading system.

## Features

### MVP (Production Ready)
- ✅ Live financial news feed with search filters
- ✅ AI-powered article summaries and market-impact analysis
- ✅ Market sentiment classification (Bullish/Bearish/Neutral)
- ✅ Affected assets identification with tickers
- ✅ Real-time market snapshot (S&P 500, Nasdaq, Gold, Oil, Forex, Crypto)
- ✅ Interactive 1-month price charts for selected assets
- ✅ Confidence scoring for predictions
- ✅ Direct links to original articles

### Supported Assets
- **Equities:** S&P 500, Nasdaq, XOM, CVX, DAL, and more
- **Commodities:** Gold, Oil (WTI)
- **Forex:** EUR/USD
- **Crypto:** BTC-USD

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **Backend Logic** | Python |
| **Charts** | Plotly |
| **Market Data** | yfinance |
| **News** | Finnhub API |
| **AI Analysis** | OpenAI GPT-4o-mini |
| **Deployment** | Streamlit Community Cloud / Railway |

## Quick Start

### Prerequisites
- Python 3.8+
- NewsAPI key (free tier: [newsapi.org](https://finnhub.io/dashboard))
- OpenAI API key ([openai.com](https://openai.com))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/maxamedjaamac34/ai-market-intelligence.git
   cd ai-market-intelligence
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys:
   NEWS_API_KEY=your_news_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the app**
   ```bash
   streamlit run app.py
   ```

   The app will open at `http://localhost:8501`

## How It Works

### Data Flow
```
Financial News API
         ↓
   NewsAPI (latest articles)
         ↓
   User selects article
         ↓
   AI Analysis Module
         ↓
   GPT-4o analyzes:
   • Summary
   • Market Impact (Bullish/Bearish/Neutral)
   • Affected Assets (tickers, sectors)
   • Confidence Score (0-100)
         ↓
   yfinance fetches price data
         ↓
   Plotly renders charts
         ↓
   Streamlit displays dashboard
```

### Example Output

**Input Article:**
> "OPEC signals additional production cuts amid global slowdown"

**AI Analysis:**
```
Summary:
OPEC announced plans to maintain production cuts to stabilize oil prices 
amid concerns about global economic growth.

Market Impact:
Bullish for oil and energy stocks; Bearish for airlines and transportation.

Affected Assets:
XOM, CVX, USO, DAL, AAL, UAL

Confidence:
78%
```

**Dashboard Display:**
- Live market snapshot with 5 major assets
- Oil price chart (1-month history)
- Sentiment badges (Bullish/Bearish/Neutral)
- Direct article link

## File Structure

```
ai-market-intelligence/
├── app.py                 # Main Streamlit dashboard
├── news.py               # NewsAPI integration
├── market_data.py        # yfinance data fetching
├── ai_analysis.py        # OpenAI integration
├── requirements.txt      # Python dependencies
├── .env                  # API keys (not committed)
├── .env.example          # Template for .env
└── README.md             # This file
```

## API Keys Setup

### Finnhub
1. Go to [finnhub.io](https://finnhub.io)
2. Sign up for a free account
3. Get your API token from the dashboard
4. Add credit/billing for higher rate limits (optional)
5. Copy your API key to `.env`

**Free Tier Limits:**
- ✅ 60 API calls/minute
- ✅ 30,000 calls/month  
- ✅ Real-time financial data
- ✅ Perfect for development

### OpenAI
1. Go to [openai.com/api](https://openai.com/api)
2. Create API keys in your account dashboard
3. Add credit/billing
4. Copy your API key to `.env`
5. Note: Using GPT-4o-mini keeps costs low (~$0.02 per analysis)

## Deployment

### Option 1: Streamlit Community Cloud (Fastest)
1. Push code to GitHub (public repo)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Click "New app" → Select your repo
4. Add secrets (NEWS_API_KEY, OPENAI_API_KEY) in Settings
5. Deploy instantly

### Option 2: Railway
1. Push code to GitHub
2. Connect GitHub account to Railway
3. Create new project → Select repo
4. Add environment variables
5. Deploy and get public URL

### Option 3: Local/Self-hosted
```bash
streamlit run app.py --server.port 8501
```

## Limitations & Design Decisions

### Intentional Constraints
- **Not a price predictor:** This is a news-to-impact translator, not a trading model
- **Macro-focused:** Analyzes broad market events, not individual stock analysis
- **No real-time alerts:** Articles are fetched on-demand; no push notifications
- **No backtesting:** No historical signal accuracy analysis
- **Limited news sources:** NewsAPI-dependent (consider adding Finnhub or MarketAux for alternatives)

### Future Enhancements (v2)
- [ ] Multiple AI models comparison (Gemini, Claude)
- [ ] Extended timeline charts (1-year, 5-year)
- [ ] Correlation analysis between events and price movements
- [ ] User dashboard with saved analyses
- [ ] Email alerts for high-confidence predictions
- [ ] Event categorization (Geopolitics, Central Banks, Earnings, etc.)
- [ ] Historical backtest: "Did this signal pan out?"
- [ ] Alternative news sources (Finnhub, MarketAux, Twitter API)
- [ ] Sector rotation heatmaps
- [ ] Volatility gauges (VIX, Put/call ratios)

## Resume Bullet

> Built and deployed MacroLens, an AI-powered market intelligence dashboard that aggregates financial news, summarizes macro events with NLP, predicts likely effects on equities/commodities/currencies, and visualizes asset movements with interactive Plotly charts. Stack: Python, Streamlit, GPT-4o, yfinance, deployed on Streamlit Cloud.

**Skills Demonstrated:**
- Financial data pipelines
- AI/NLP integration (OpenAI API)
- Real-time dashboard design (Streamlit)
- Data visualization (Plotly)
- Full-stack rapid prototyping
- Cloud deployment

## Disclaimer

**Important:** This tool is for **educational and informational purposes only**. It is:
- ❌ **NOT** a trading system or financial advisor
- ❌ **NOT** a guarantee of market movements
- ❌ **NOT** investment advice

Use it to understand market context and event impact, not as a basis for trades. Always do your own research and consult a financial advisor before making investment decisions.

## Contributing

Contributions welcome! Feel free to open issues or PRs for:
- New data sources
- UI/UX improvements
- Performance optimizations
- Bug fixes

## License

MIT License - Feel free to use, modify, and distribute.

## Support

For issues or questions:
1. Check GitHub issues
2. Review API documentation (NewsAPI, OpenAI, yfinance)
3. Verify API keys in `.env`
4. Check network connectivity

## Author

Built for speed and impact. 🚀

---

**Last Updated:** March 2026
**Status:** MVP Production Ready
