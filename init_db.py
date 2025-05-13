import sqlite3

conn = sqlite3.connect('sensor.db')
c = conn.cursor()
c.execute('''
CREATE TABLE sensor_readings (
    id INTEGER PRIMARY KEY,
    asset_type TEXT,
    stress INTEGER,
    temp_start INTEGER,
    temp_end INTEGER
)
''')
c.executemany('INSERT INTO sensor_readings (asset_type, stress, temp_start, temp_end) VALUES (?, ?, ?, ?)', [
    ('bridge', 80, 70, 75),
    ('bridge', 60, 65, 65),
    ('building', 0, 68, 75),
    ('building', 0, 70, 70),
])
conn.commit()
conn.close()
