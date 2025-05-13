import sqlite3
import time

def get_sensor_data(asset_type):
    start_time = time.time()
    conn = sqlite3.connect('sensor.db')
    c = conn.cursor()
    c.execute("SELECT * FROM sensor_readings WHERE asset_type=?", (asset_type,))
    rows = c.fetchall()
    conn.close()
    duration = time.time() - start_time
    print(f"Query time for {asset_type}: {duration:.5f} seconds")
    return rows