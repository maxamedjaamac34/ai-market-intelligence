import yfinance as yf
import pandas as pd

DEFAULT_TICKERS = {
    "S&P 500": "^GSPC",
    "Nasdaq": "^IXIC",
    "Gold": "GC=F",
    "Oil": "CL=F",
    "EUR/USD": "EURUSD=X",
    "BTC-USD": "BTC-USD",
    "XOM": "XOM",
    "CVX": "CVX",
    "DAL": "DAL",
}

def get_price_history(ticker, period="1mo", interval="1d"):
    df = yf.download(ticker, period=period, interval=interval, auto_adjust=True, progress=False)
    if df.empty:
        return pd.DataFrame()
    df = df.reset_index()
    
    # Handle MultiIndex columns (when yfinance returns tuple column names)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [col[0] if col[1] == '' else col[0] for col in df.columns]
    
    # Keep only Date and Close columns
    if 'Date' in df.columns and 'Close' in df.columns:
        df = df[['Date', 'Close']]
    
    return df

def get_default_market_snapshot():
    rows = []
    for label, ticker in DEFAULT_TICKERS.items():
        try:
            df = yf.download(ticker, period="5d", interval="1d", auto_adjust=True, progress=False)
            if not df.empty:
                latest = float(df["Close"].iloc[-1])
                prev = float(df["Close"].iloc[-2]) if len(df) > 1 else latest
                change_pct = ((latest - prev) / prev) * 100 if prev else 0
                rows.append({
                    "Asset": label,
                    "Ticker": ticker,
                    "Latest": round(latest, 2),
                    "Daily % Change": round(change_pct, 2),
                })
        except Exception:
            continue
    return pd.DataFrame(rows)
