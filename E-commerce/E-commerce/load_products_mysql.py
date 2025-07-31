import pandas as pd
import mysql.connector

# Load CSV
df = pd.read_csv('products.csv')

# Connect to MySQL Database
conn = mysql.connector.connect(
    host='localhost',        # change if using remote
    user='your_username',    # replace with your MySQL username
    password='your_password',# replace with your password
    database='your_database' # make sure database exists
)
cursor = conn.cursor()

# Drop table if exists (for clean rerun)
cursor.execute("DROP TABLE IF EXISTS products")

# Create products table
create_table_query = '''
CREATE TABLE products (
    id INT PRIMARY KEY,
    cost FLOAT,
    category VARCHAR(100),
    name TEXT,
    brand VARCHAR(100),
    retail_price FLOAT,
    department VARCHAR(100),
    sku VARCHAR(255) UNIQUE,
    distribution_center_id INT
)
'''
cursor.execute(create_table_query)

# Insert data using executemany for performance
insert_query = '''
INSERT INTO products (id, cost, category, name, brand, retail_price, department, sku, distribution_center_id)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
'''

data_to_insert = [tuple(row) for row in df.itertuples(index=False)]
cursor.executemany(insert_query, data_to_insert)

# Commit changes
conn.commit()

# Verify data with a sample query
cursor.execute("SELECT * FROM products LIMIT 5")
for row in cursor.fetchall():
    print(row)

# Close connections
cursor.close()
conn.close()
