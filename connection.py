import sqlite3

databasename='pji.db'
conn=sqlite3.connect(databasename)
c=conn.cursor()

# create database
conn.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    
    ) ''')

# PRICE IS BOOLEAN
conn.execute('''CREATE TABLE IF NOT EXISTS items ( 
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             category TEXT NOT NULL,
             price TEXT NOT NULL,
             bought_price TEXT NOT NULL,
             qty TEXT NOT NULL,
             qrcode TEXT NULL,
             voltage TEXT NOT NULL,
             created_at DATETIME DEFAULT CURRENT_TIMESTAMP
             
             
             )''')


conn.execute('''CREATE TABLE IF NOT EXISTS workers ( 
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             email TEXT NOT NULL,
             id_type TEXT NOT NULL,
             id_number TEXT NOT NULL,
             number TEXT NOT NULL,
             position TEXT NOT NULL,
             address TEXT NOT NULL,
            
             created_at DATETIME DEFAULT CURRENT_TIMESTAMP
             
             
             )''')
# order status defualt is done
conn.execute('''CREATE TABLE IF NOT EXISTS sales ( 
             id INTEGER PRIMARY KEY,
             order_id INTEGER NOT NULL,
             name TEXT NOT NULL,
             price TEXT NOT NULL,
             total_price TEXT NOT NULL,
             qty TEXT NOT NULL,
             voltage TEXT NOT NULL,
             order_status TEXT NOT NULL,
             created_at DATETIME DEFAULT CURRENT_TIMESTAMP
             
             
             )''')



conn.execute('''CREATE TABLE IF NOT EXISTS customers ( 
             id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             number TEXT NOT NULL,
             created_at DATETIME DEFAULT CURRENT_TIMESTAMP
             
             
             )''')

conn.execute('''CREATE TABLE IF NOT EXISTS expenses ( 
             id INTEGER PRIMARY KEY,
             giver TEXT NOT NULL,
             reciver TEXT NOT NULL,
             purpose TEXT NOT NULL,
             amount TEXT NOT NULL,
             created_at DATETIME DEFAULT CURRENT_TIMESTAMP
             
             
             )''')


conn.commit()
conn.close()