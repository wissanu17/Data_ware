import pandas as pd
from sqlalchemy import create_engine

# MySQL
engine = create_engine('mysql+pymysql://root:pote2546@localhost:3306/data_warehouse')

# Load from CSV
sales_df = pd.read_csv('sales.csv')
products_df = pd.read_csv('products.csv')
customers_df = pd.read_csv('customers.csv')
time_df = pd.read_csv('time.csv')

# check and transform data
# Map ProductName -> ProductID
product_map = products_df.set_index('ProductName')['ProductID'].to_dict()
sales_df['ProductID'] = sales_df['ProductName'].map(product_map)

# Map CustomerName -> CustomerID
customer_map = customers_df.set_index('CustomerName')['CustomerID'].to_dict()
sales_df['CustomerID'] = sales_df['CustomerName'].map(customer_map)

# Map Date -> TimeID
time_map = time_df.set_index('Date')['TimeID'].to_dict()
sales_df['TimeID'] = sales_df['Date'].map(time_map)

# Drop columns that are no longer needed
sales_df = sales_df.drop(columns=['ProductName', 'CustomerName', 'Date'])

# โหลดข้อมูลเข้า MySQL
# โหลด products
products_df.to_sql('products', engine, if_exists='append', index=False)

# โหลด customers
customers_df.to_sql('customers', engine, if_exists='append', index=False)

# โหลด time
time_df.to_sql('time', engine, if_exists='append', index=False)

# โหลด sales
sales_df.to_sql('sales', engine, if_exists='append', index=False)

print("ETL process completed successfully!")
