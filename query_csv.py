from connection import databasename
import sqlite3


def total_sales(self):
    conn = sqlite3.connect(databasename)
    cur = conn.cursor()
    cur.execute("SELECT SUM(total) FROM sales WHERE order_status='completed'")
    total = cur.fetchone()[0]
    conn.close()
    return total
    