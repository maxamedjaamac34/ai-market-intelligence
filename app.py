import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from news import get_financial_news
from market_data import get_price_history, get_default_market_snapshot, DEFAULT_TICKERS
from ai_analysis import analyze_article

# Page config
st.set_page_config(
    page_title="MacroLens - AI Market Intelligence",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for styling
st.markdown("""
    <style>
        /* Light mode styles */
        @media (prefers-color-scheme: light) {
            .stApp {
                background-color: #f8f9fa;
            }
            
            .article-card {
                background-color: #ffffff;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            
            .stDataFrame {
                background-color: #ffffff;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }
            
            .css-1d391kg {
                background-color: #ffffff;
                border-right: 1px solid #e9ecef;
            }
        }
        
        /* Dark mode styles */
        @media (prefers-color-scheme: dark) {
            .stApp {
                background-color: #0e1117;
            }
            
            .article-card {
                background-color: #1a1c23;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                border: 1px solid #30363d;
            }
            
            .stDataFrame {
                background-color: #1a1c23;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.3);
                border: 1px solid #30363d;
            }
            
            .css-1d391kg {
                background-color: #1a1c23;
                border-right: 1px solid #30363d;
            }
            
            /* Text colors for dark mode */
            h1, h2, h3, h4, h5, h6 {
                color: #ffffff !important;
            }
            
            .stMarkdown p, .stText, .stCaption {
                color: #ffffff !important;
            }
            
            /* Footer text */
            .stMarkdown a {
                color: #58a6ff !important;
            }
        }
        
        /* Universal styles */
        h1 {
            color: #1f77b4;
            text-align: center;
            padding-bottom: 10px;
            border-bottom: 3px solid #1f77b4;
        }
        
        /* Article card styling */
        .article-card {
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #1f77b4;
            margin: 10px 0;
        }
        
        /* Sentiment badges */
        .sentiment-bullish {
            background-color: #d4edda;
            color: #155724;
            padding: 8px 12px;
            border-radius: 5px;
            font-weight: bold;
            display: inline-block;
            margin: 5px 5px 5px 0;
        }
        
        .sentiment-bearish {
            background-color: #f8d7da;
            color: #721c24;
            padding: 8px 12px;
            border-radius: 5px;
            font-weight: bold;
            display: inline-block;
            margin: 5px 5px 5px 0;
        }
        
        .sentiment-neutral {
            background-color: #e2e3e5;
            color: #383d41;
            padding: 8px 12px;
            border-radius: 5px;
            font-weight: bold;
            display: inline-block;
            margin: 5px 5px 5px 0;
        }
        
        /* Dark mode sentiment badges */
        @media (prefers-color-scheme: dark) {
            .sentiment-bullish {
                background-color: #238636;
                color: #ffffff;
            }
            
            .sentiment-bearish {
                background-color: #da3633;
                color: #ffffff;
            }
            
            .sentiment-neutral {
                background-color: #656c76;
                color: #ffffff;
            }
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🔍 MacroLens")
st.markdown("<p style='text-align: center; font-size: 16px; color: #555;'>AI-Powered Market Intelligence Dashboard</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 12px; color: #aaa;'>Financial news • AI analysis • Market predictions • Interactive charts</p>", unsafe_allow_html=True)

# Quick Start Guide
with st.expander("🚀 Quick Start Guide - How to Use MacroLens", expanded=False):
    st.markdown("""
    ### 📖 **Getting Started**
    
    **MacroLens** helps you stay informed about market-moving events with AI-powered analysis. Here's how to use the main features:
    
    ### 📰 **1. Browse Financial News**
    - **Refresh News**: Click the "🔄 Refresh News" button in the sidebar to load the latest financial articles from Finnhub
    - **Customize Search**: Use the "News Query" field to search for specific categories (e.g., "forex", "crypto", "general")
    - **Article Count**: Adjust the slider to fetch 5-20 articles at once
    
    ### 🤖 **2. Get AI Market Analysis**
    - **Select Article**: Choose any article from the dropdown list
    - **Analyze**: Click "🤖 Analyze with AI" to get AI-powered insights
    - **View Results**: The AI provides:
      - 📝 **Summary**: 2-3 sentence overview
      - 📊 **Market Impact**: Bullish/Bearish/Neutral assessment
      - 🎯 **Affected Assets**: Tickers, sectors, or commodities impacted
      - 📈 **Confidence Score**: AI's certainty level (0-100%)
    
    ### 📊 **3. Monitor Market Data**
    - **Market Snapshot**: View real-time prices and daily changes for major assets
    - **Color Coding**: 
      - 🟢 **Green**: Positive daily change
      - 🔴 **Red**: Negative daily change
      - ⚪ **Gray**: No change
    
    ### 📈 **4. Interactive Charts**
    - **Select Asset**: Use the "Chart Asset" dropdown to choose what to visualize
    - **Available Assets**: S&P 500, Nasdaq, Gold, Oil, EUR/USD, BTC-USD, and more
    - **Time Period**: Charts show 1-month price history
    - **Hover Details**: Mouse over the chart for exact prices and dates
    
    ### 💡 **Pro Tips**
    - 🔄 **Auto-refresh**: News stays loaded until you refresh manually
    - 🎯 **AI Analysis**: Each analysis costs ~$0.02 (GPT-4o-mini)
    - 📱 **Responsive**: Works on desktop and mobile browsers
    - 🌙 **Dark Mode**: Automatically adapts to your system theme
    
    ### ⚠️ **Important Notes**
    - This is **market intelligence**, not financial advice
    - Always verify information from original sources
    - Finnhub free tier: 60 calls/minute, 30,000/month
    
    **Ready to explore? Start by clicking "Refresh News"!** 🎯
    """)

# Sidebar controls
with st.sidebar:
    st.header("⚙️ Controls")
    st.markdown("---")
    
    query = st.text_input(
        "📰 News Query",
        value="general",
        placeholder="Enter categories like: general, forex, crypto, merger...",
        help="Enter news category (general, forex, crypto, merger) or leave empty for general news"
    )
    
    page_size = st.slider(
        "📊 Number of Articles",
        min_value=5,
        max_value=20,
        value=10,
        help="How many articles to fetch"
    )
    
    selected_asset_label = st.selectbox(
        "📈 Chart Asset",
        list(DEFAULT_TICKERS.keys()),
        help="Select which asset to display in the chart"
    )
    
    st.markdown("---")
    run_news = st.button("🔄 Refresh News", use_container_width=True)

# Initialize or fetch articles
if run_news or "articles" not in st.session_state:
    try:
        # Ensure query is never empty
        if not query or query.strip() == "":
            query = "stocks OR oil OR forex OR markets"
        
        st.session_state.articles = get_financial_news(query=query.strip(), page_size=page_size)
    except Exception as e:
        st.error(f"❌ Failed to load news: {e}")
        st.session_state.articles = []

articles = st.session_state.get("articles", [])

# Main content layout
col1, col2 = st.columns([1.2, 0.8])

# LEFT COLUMN: News & Analysis
with col1:
    st.header("📰 Latest Financial News")
    
    if not articles:
        st.info("📭 No articles found. Try different keywords!")
    else:
        article_titles = [
            f"{i+1}. {a.get('title', 'Untitled')[:60]}..." for i, a in enumerate(articles)
        ]
        selected_index = st.selectbox(
            "Select an article",
            range(len(article_titles)),
            format_func=lambda i: article_titles[i],
            label_visibility="collapsed"
        )
        
        article = articles[selected_index]
        
        # Article details in a card-like container
        st.markdown(f"### {article.get('title', 'Untitled')}")
        st.markdown(f"*{article.get('description', 'No description available.')}*")
        
        col_source, col_date = st.columns(2)
        with col_source:
            st.caption(f"📌 **Source:** {article.get('source', {}).get('name', 'Unknown')}")
        with col_date:
            published_date = article.get('publishedAt', 'Unknown')
            if published_date != 'Unknown' and len(published_date) >= 10:
                # Format as YYYY-MM-DD
                display_date = published_date[:10]
            else:
                display_date = 'Unknown'
            st.caption(f"🕐 **Published:** {display_date}")
        
        if article.get("url"):
            st.markdown(f"[📖 Read full article →]({article['url']})")
        
        st.markdown("---")
        
        # Analysis button
        if st.button("🤖 Analyze with AI", use_container_width=True):
            with st.spinner("⏳ Generating market insight..."):
                try:
                    result = analyze_article(
                        article.get("title", ""),
                        article.get("description", ""),
                        article.get("source", {}).get("name", "")
                    )
                    st.session_state["analysis_result"] = result
                except Exception as e:
                    st.error(f"❌ AI analysis failed: {e}")
        
        # Display analysis result
        if "analysis_result" in st.session_state:
            st.subheader("💡 AI Market Insight")
            
            analysis = st.session_state["analysis_result"]
            
            # Parse and display structured results
            st.markdown(analysis)
            
            # Extract sentiment for badge display (if format is predictable)
            if "Bullish" in analysis:
                st.markdown("<span class='sentiment-bullish'>📈 BULLISH</span>", unsafe_allow_html=True)
            elif "Bearish" in analysis:
                st.markdown("<span class='sentiment-bearish'>📉 BEARISH</span>", unsafe_allow_html=True)
            elif "Neutral" in analysis:
                st.markdown("<span class='sentiment-neutral'>➡️ NEUTRAL</span>", unsafe_allow_html=True)

# RIGHT COLUMN: Market Snapshot
with col2:
    st.header("📊 Market Snapshot")
    
    snapshot = get_default_market_snapshot()
    if not snapshot.empty:
        # Format the dataframe for display
        display_df = snapshot.copy()
        display_df["Latest"] = display_df["Latest"].apply(lambda x: f"${x:.2f}")
        display_df["Daily % Change"] = display_df["Daily % Change"].apply(lambda x: f"{x:+.2f}%")
        
        # Add color coding for the Daily % Change column
        def color_change(val):
            try:
                # Convert string to float for comparison
                numeric_val = float(val.strip('%').strip('+'))
                if numeric_val > 0:
                    return [''] * (len(display_df.columns) - 1) + ['color: green; font-weight: bold;']
                elif numeric_val < 0:
                    return [''] * (len(display_df.columns) - 1) + ['color: red; font-weight: bold;']
                else:
                    return [''] * (len(display_df.columns) - 1) + ['color: gray;']
            except (ValueError, AttributeError):
                return [''] * len(display_df.columns)
        
        # Apply styling
        styled_df = display_df.style.apply(
            lambda row: color_change(row['Daily % Change']),
            axis=1
        )
        
        st.dataframe(styled_df, use_container_width=True, hide_index=True)
    else:
        st.info("📭 No market data available.")

# Full-width chart section
st.markdown("---")
st.header("📈 Interactive Market Chart")

ticker = DEFAULT_TICKERS[selected_asset_label]
price_df = get_price_history(ticker)

if not price_df.empty:
    # Create an enhanced chart with better styling
    fig = px.line(
        price_df,
        x="Date",
        y="Close",
        title=f"{selected_asset_label} ({ticker}) - 1 Month Price History",
        labels={"Close": "Price ($)", "Date": "Date"},
        template="plotly_white"
    )
    
    fig.update_traces(line=dict(color="#1f77b4", width=2))
    fig.update_layout(
        height=400,
        hovermode="x unified",
        font=dict(size=11),
        margin=dict(l=50, r=50, t=60, b=50),
    )
    
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning(f"⚠️ No chart data available for {selected_asset_label}")

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    st.markdown("### 📧 Contact")
    st.markdown("**Creator:** Mohamed Ahmed")
    st.markdown("[📧 Email](mailto:mohamedahmed@bennington.edu)")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/mohamed-ahmed-4794b6158/)")
    st.markdown("[🐙 GitHub](https://github.com/maxamedjaamac34)")

with col2:
    st.markdown("### 🎯 Mission")
    st.markdown("""
    **MacroLens** democratizes market intelligence by combining:
    
    📰 **Real-time news aggregation** from trusted sources  
    🤖 **AI-powered analysis** using GPT-4o for market insights  
    📊 **Interactive visualizations** for better decision-making  
    🚀 **Open-source accessibility** for traders and analysts
    
    Built to help professionals stay ahead of market-moving events without the noise.
    """)

with col3:
    st.markdown("### ⚠️ Disclaimer")
    st.markdown("""
    **Not financial advice.**  
    This tool provides market intelligence and event interpretation only.  
    Always conduct your own research and consult financial professionals.
    """)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; font-size: 11px; color: #aaa;'>"
    "MacroLens v1.0 • Built with Streamlit, OpenAI, and yfinance • "
    "<a href='https://github.com/maxamedjaamac34/ai-market-intelligence' target='_blank'>View Source</a>"
    "</p>",
    unsafe_allow_html=True
)
