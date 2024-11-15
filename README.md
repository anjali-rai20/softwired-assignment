# Option Chain Data Fetcher

This project fetches option chain data for specified symbols from the NSE India API, processes it, and generates various insights and visualizations based on the option chain data. The data is saved in JSON format and parsed into CSV for further analysis.

## Requirements

Before running the code, ensure you have the following dependencies installed:

- `requests`: For making HTTP requests to fetch data.
- `pandas`: For data manipulation and parsing.
- `matplotlib`: For generating plots and visualizations.
- `json`: For parsing JSON data.

You can install the required libraries using `pip`:

```bash
pip install requests pandas matplotlib
```

## How to Run

#### Step 1: Fetch Option Chain Data

The script automatically fetches option chain data for specified symbols like NIFTY and HDFCBANK from the NSE India API. Data is saved in JSON files.
	•	The script continuously fetches data for the specified symbols in a loop.
	•	The data is saved in the format {symbol}_data.json.

#### Step 2: Parse Data and Filter

The script processes the saved JSON files and filters the option chain data for the specified expiry date. The parsed data is saved into CSV files for easy analysis.

#### Step 3: Visualize Data

The script generates the following plots based on the processed data:
	•	Strike Price vs Open Interest: Shows the open interest for both Call and Put options.
	•	Implied Volatility and Change in Open Interest vs Strike Price: Plots the change in open interest and implied volatility for both Call and Put options.

Running the Script

1.	First, run the script to start fetching the data
    
    ```python
        python fetch_data.py
    ```
2.	After the data is fetched, it will be saved in JSON format and processed. The final output will be stored in CSV files such as NIFTY_parsed.csv and HDFCBANK_parsed.csv.

3.	The visualizations will automatically pop up once the data is processed.

Example Output Files
 - NIFTY_parsed.csv: Contains the parsed and filtered option chain data for NIFTY.
 - HDFCBANK_parsed.csv: Contains the parsed and filtered option chain data for HDFCBANK.
