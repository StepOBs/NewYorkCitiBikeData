import pandas as pd
import sqlite3
conn = sqlite3.connect('bike_data.db')
conn.text_factory = str

def get_stations():
    db_file = 'bikes_2014_09'
    df = pd.read_sql_query("SELECT * from " + db_file, conn)
    start_lats = pd.Series(df['start_station_name']).unique()
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS stations')
    cur.execute("CREATE TABLE stations(name)")

    for i in start_lats:
