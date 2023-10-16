import pandas as pd
from google.cloud import storage
from google.cloud import bigquery

BUCKET_NAME = 'c4ds'
PROJECT_NAME = 'etl01-globant'
DATASET_NAME = 'ny_collisions'
TABLE1_NAME = 'example_data'

global nyc_col
global nyc_per

def readDatabases():
    #Reading NYC collisions databases
   # Collisions:
    ny_coll_c = pd.read_csv("https://data.cityofnewyork.us/resource/h9gi-nx95.csv")
    nyc_col = ny_coll_c.iloc[:, [23, 0, 1, 6, 18, 19, 10, 11, 24]]

    #Persons involved in collisions
    ny_coll_p = pd.read_csv("https://data.cityofnewyork.us/resource/f55k-p6yu.csv")
    nyc_per = ny_coll_p[['unique_id', 'collision_id', 'person_type', 'person_age', 'person_sex', 'contributing_factor_1']]

    print("databases read")
    return nyc_col, nyc_per


def writeLocalDatabases(db, filename):
    db.to_csv(filename, sep=',', index=False, encoding='utf-8', quoting = 3, quotechar = '"', escapechar='\\')

    print("database written locally")

#Saving filtered databases to BigQuery

def writeDFtoBigQuery(df, table):
    table_id = f"{PROJECT_NAME}.{DATASET_NAME}.{table}"
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.autodetect = True
    job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
    job.result()
    tableOutput = client.get_table(table_id)  # Make an API request.
    print("Loaded {} rows and {} columns to {}".format(tableOutput.num_rows, len(tableOutput.schema), table_id)
)

def filterByYear(df):
    #To be implemented
    return df


nyc_col, nyc_per = readDatabases()
nyc_col = filterByYear(nyc_col)
#writeLocalDatabases(nyc_col, "nyc_col01.csv")
#writeLocalDatabases(nyc_per, "nyc_per01.csv")
writeDFtoBigQuery(nyc_per, "persons1")
writeDFtoBigQuery(nyc_col, "collisions1")

print("finished")
