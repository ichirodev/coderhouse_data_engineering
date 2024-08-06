from modules.extract import extract as _extract
from modules.transform import transform as _transform
from modules.load import load as _load
from dotenv import load_dotenv
import argparse

def main():
	load_dotenv()
	out_data_stg_json = "out/stg_news.json"
	out_data_csv = "out/news.csv"
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--clean-results-table", action="store_true")
	args = parser.parse_args()
	clean_results_table = args.clean_results_table

	topic = "Cryptocurrency"
	start_date = "2024-08-01T00:00:00.000"
	end_date = "2024-08-01T23:59:59.999"

	_extract(topic, start_date, end_date, out_data_stg_json)
	_transform(out_data_stg_json, out_data_csv)
	_load(out_data_csv, clean_results_table)


if __name__ == "__main__":
	main()
