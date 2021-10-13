from google.cloud.bigquery.job import query
import pandas as pd
from google.cloud import bigquery

# variables
gcp_project = 'etl-sql-python'
bq_dataset = 'test_data'

# connections
client = bigquery.Client(project=gcp_project)
dataset_ref = client.get_dataset(bq_dataset)

# results to dataframe function
def gcp2df(sql):
    query = client.query(sql)
    results = query.result()
    return results.to_dataframe()

query = """SELECT *
FROM `bigquery-public-data.stackoverflow.posts_questions`
LIMIT 100000
"""

stackoverflow_data = gcp2df(query)

stackoverflow_data.to_csv('stackoverflow_data_1.csv')