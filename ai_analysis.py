import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_TEMPLATE = """
You are a financial market analysis assistant.

Given this news article:
Title: {title}
Description: {description}
Source: {source}

Return a concise structured response in this exact format:

Summary:
<2-3 sentence summary>

Market Impact:
<Bullish/Bearish/Neutral and why>

Affected Assets:
<comma-separated list of tickers, sectors, commodities, currencies, or asset classes>

Confidence:
<0-100 integer>

Do not give investment advice. Focus on likely market interpretation.
"""

def analyze_article(title, description, source):
    prompt = PROMPT_TEMPLATE.format(
        title=title or "",
        description=description or "",
        source=source or ""
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a careful financial news analysis assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content
