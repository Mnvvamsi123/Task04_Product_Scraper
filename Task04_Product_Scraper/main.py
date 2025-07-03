import pandas as pd
from utils.scraper import get_product_data

def main():
    url = "https://books.toscrape.com/"
    data = get_product_data(url)
    df = pd.DataFrame(data)

    output_path = "output/products.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Data saved successfully to: {output_path}")

if __name__ == "__main__":
    main()
