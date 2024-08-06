import json
import pandas as pd


def transform(file_in, file_out):
	f = open(file_in, "r")
	data_text = f.read()
	data_json = json.loads(data_text)
	articles = data_json["articles"]

	df = pd.DataFrame(articles)

	df.rename(columns={"publishedAt": "publish_datetime"}, inplace=True)
	df['source'] = df['source'].apply(lambda x: x['name'])

	df = df[['source', 'author', 'title', 'url', 'publish_datetime']]

	df.to_csv(file_out, index=False)
	print("Transform: Success!")
