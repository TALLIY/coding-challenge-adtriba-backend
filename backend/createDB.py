import sqlite3
import csv

# Open a connection to a new SQLite database file
conn = sqlite3.connect('sphere-sample-data.db')

# Create a cursor object to execute SQL statements
cur = conn.cursor()

# Create a new table in the database
cur.execute('''CREATE TABLE IF NOT EXISTS sphere_sample_data (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date DATE, 
               source TEXT, 
               attributed_conversions FLOAT, 
               attributed_revenue FLOAT, 
               type TEXT, 
               spends FLOAT, 
               partition_id TEXT, 
               optimisation_target TEXT )''')

# Read the CSV file and insert its contents into the database
with open('sphere-sample-data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        cur.execute(
    "INSERT INTO sphere_sample_data (date, source, attributed_conversions, attributed_revenue, type, spends, partition_id, optimisation_target) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", row[0:])



# Commit the changes to the database and close the connection
conn.commit()
conn.close()
