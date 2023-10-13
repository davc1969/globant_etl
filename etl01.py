import pandas as pd

#Reading NYC collisions databases
# Collisions:
ny_coll_c = pd.read_csv("https://data.cityofnewyork.us/resource/h9gi-nx95.csv")
nyc_col = ny_coll_c[['collision_id', 'crash_date', 'location', 'contributing_factor_vehicle_1', 'contributing_factor_vehicle_2', 'number_of_persons_injured', 'number_of_persons_killed', 'vehicle_type_code1']]

#Persons involved in collisions
ny_coll_p = pd.read_csv("https://data.cityofnewyork.us/resource/f55k-p6yu.csv")
nyc_per = ny_coll_p[['unique_id', 'collision_id', 'person_type', 'person_age', 'person_sex', 'contributing_factor_1']]

#Saving filtered databases to BigQuery