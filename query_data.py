from connection import databasename
import sqlite3



def itemfetch_data():
    conn=sqlite3.connect(databasename)
    cur=conn.cursor()
    cur.execute("SELECT * FROM items")
    rows=cur.fetchall()
    conn.close()
    
    return rows



def cus_data():
    conn=sqlite3.connect(databasename)
    cur=conn.cursor()
    cur.execute("SELECT * FROM customers")
    rows=cur.fetchall()
    conn.close()
    
    return rows