import json
import pandas as pd
from datetime import datetime

expiry_date = "2024-11-28"

def extract_field(option_data, field):
    return option_data.get(field, None) if isinstance(option_data, dict) else None

def parse_option_chain_data(symbol, expiry_date):
    try:
        # Load JSON data
        with open(f"{symbol}_data.json", "r") as f:
            raw_data = json.load(f)
        
        # Validate if 'records' and 'data' keys exist
        if 'records' not in raw_data or 'data' not in raw_data['records']:
            raise KeyError(f"'records' or 'data' key not found in JSON for {symbol}")

        df = pd.DataFrame(raw_data['records']['data'])

        # Create filtered DataFrame
        filtered_df = pd.DataFrame({
            'Strike Price': df['strikePrice'],
            'Call Open Interest': df['CE'].apply(lambda x: extract_field(x, 'openInterest')),
            'Put Open Interest': df['PE'].apply(lambda x: extract_field(x, 'openInterest')),
            'Call LTP': df['CE'].apply(lambda x: extract_field(x, 'lastPrice')),
            'Put LTP': df['PE'].apply(lambda x: extract_field(x, 'lastPrice')),
            'Call Change in OI': df['CE'].apply(lambda x: extract_field(x, 'changeinOpenInterest')),
            'Put Change in OI': df['PE'].apply(lambda x: extract_field(x, 'changeinOpenInterest')),
            'Call Volume': df['CE'].apply(lambda x: extract_field(x, 'volume')),
            'Put Volume': df['PE'].apply(lambda x: extract_field(x, 'volume')),
            'Call Bid Qty': df['CE'].apply(lambda x: extract_field(x, 'bidQty')),
            'Put Bid Qty': df['PE'].apply(lambda x: extract_field(x, 'bidQty')),
            'Call Bid': df['CE'].apply(lambda x: extract_field(x, 'bid')),
            'Put Bid': df['PE'].apply(lambda x: extract_field(x, 'bid')),
            'Call Ask': df['CE'].apply(lambda x: extract_field(x, 'ask')),
            'Put Ask': df['PE'].apply(lambda x: extract_field(x, 'ask')),
            'Call Ask Qty': df['CE'].apply(lambda x: extract_field(x, 'askQty')),
            'Put Ask Qty': df['PE'].apply(lambda x: extract_field(x, 'askQty')),
            'Expiry Date': pd.to_datetime(df['expiryDate'], errors='coerce').dt.date
        })

        # Filter based on expiry date
        filtered_df = filtered_df[filtered_df['Expiry Date'] == pd.to_datetime(expiry_date).date()]
        return filtered_df

    except FileNotFoundError:
        print(f"File {symbol}_data.json not found. Please ensure the file exists.")
        return pd.DataFrame()
    except KeyError as e:
        print(f"Key error in {symbol}_data.json: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"An error occurred while processing {symbol}: {e}")
        return pd.DataFrame()

# Process data for NIFTY
nifty_df = parse_option_chain_data("NIFTY", expiry_date)
if not nifty_df.empty:
    nifty_df.to_csv("NIFTY_parsed.csv", index=False)
    print("NIFTY Option Chain Data for Expiry Date:", expiry_date)
    print(nifty_df)
else:
    print("No data processed for NIFTY.")

# Process data for HDFCBANK
hdfc_df = parse_option_chain_data("HDFCBANK", expiry_date)
if not hdfc_df.empty:
    hdfc_df.to_csv("HDFCBANK_parsed.csv", index=False)
    print("\nHDFCBANK Option Chain Data for Expiry Date:", expiry_date)
    print(hdfc_df)
else:
    print("No data processed for HDFCBANK.")