from google.cloud import bigquery

def insert(payload):
    client = bigquery.Client()
    datasetName = 'acessibility_checks'
    dataset = client.dataset(datasetName)
    tableName = 'lighthouse'
    table = dataset.table(tableName)
    table_nm = client.get_table(table)
    client.insert_rows(table_nm, payload)