from text_utils import analyze_text, count_words
from api_client import fetch_eod_appl_quote

LAST_DAY_OF_YEAR = "2025-12-05T00:00:00+0000"

def display_quote_info(quote: dict):
    
    for item in quote["data"]:
        if(item.get("date") != LAST_DAY_OF_YEAR):
            continue
        symbol = item.get("symbol", "N/A")
        close_price = item.get("close", "N/A")
        exchange = item.get("exchange", "N/A")
        print(f"Symbol: {symbol}, Close Price: {close_price}, Exchange: {exchange}")


def main():

    try:
        quote = fetch_eod_appl_quote()

        display_quote_info(quote)

    except Exception as e:
        print(f"Error fetching APPLE quote: {e}")


if __name__ == "__main__":
    main()