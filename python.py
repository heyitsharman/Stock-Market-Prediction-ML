# Install (only needed in Jupyter / Colab)
# !pip install yfinance pandas

import yfinance as yf
import pandas as pd


def get_stock_data(symbol):
    """Get EXACT stock data using yfinance"""

    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info

        company_name = info.get('longName', symbol)
        current_price = info.get('currentPrice')
        previous_close = info.get('previousClose')

        if current_price and previous_close:
            change = current_price - previous_close
            pct_change = (change / previous_close) * 100
            daily_change = f"{change:+.2f} ({pct_change:+.2f}%)"
        else:
            daily_change = "N/A"

        return {
            'Company Name': company_name,
            'Current Price': f"₹{current_price:,.2f}" if current_price else "N/A",
            'Daily Change': daily_change
        }

    except Exception as e:
        print("Error:", e)
        return None


# ================= MAIN PROGRAM =================

print("STOCK PRICE ANALYZER")
print("=" * 40)

while True:

    symbol = input("\nEnter stock (or 'quit'): ").strip().upper()

    if symbol.lower() == 'quit':
        print("Exiting... Goodbye!")
        break

    print(f"Fetching {symbol}...")

    data = get_stock_data(symbol)

    if data:

        print("\nSTOCK DATA:")
        print(f"Symbol : {symbol}")
        print(f"Company: {data['Company Name']}")
        print(f"Price  : {data['Current Price']}")
        print(f"Change : {data['Daily Change']}")
        print()

        # Save to CSV
        df = pd.DataFrame([data])
        df['Symbol'] = symbol

        filename = f"{symbol}.csv"
        df.to_csv(filename, index=False)

        print(f"Saved: {filename}")

    else:
        print("No data found.")

    print("-" * 40)