from modules.extract import extract as _extract
from modules.transform import transform as _transform
from modules.load import load as _load
from dotenv import load_dotenv
import re
import argparse

def is_date_iso_8601(date_str):
	ISO_8601_DATE_PATTERN = r'^\d{4}-\d{2}-\d{2}$'
	if re.match(ISO_8601_DATE_PATTERN, date_str):
		return True
	return False

def main():
	load_dotenv()
	out_data_stg_json = "out/stg_news.json"
	out_data_csv = "out/news.csv"
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--clean-results-table", action="store_true")
	parser.add_argument("--date", type=str)
	args = parser.parse_args()
	clean_results_table = args.clean_results_table

	topic = "Cryptocurrency"

	date: str = args.date
	start_date = f"{date}T00:00:00.000"
	end_date = f"{date}T23:59:59.999"

	if not date:
		raise ValueError("Date not entered, use the flag --date=<ISO_8061_DATE>")

	if not is_date_iso_8601(date):
		raise ValueError(f"Date entered '{date}' is not on format ISO 8601")

	_extract(topic, start_date, end_date, out_data_stg_json)
	_transform(out_data_stg_json, out_data_csv)
	_load(out_data_csv, clean_results_table)


if __name__ == "__main__":
	main()
