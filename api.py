from datetime import datetime
import sqlite3 as sql
conn = sql.connect('spent.db')
c = conn.cursor()
def init():
    # initialize a new table to store date
    c.execute('''CREATE TABLE IF NOT EXISTS expenses(
                amount REAL,
                category TEXT COLLATE NOCASE,
                message TEXT,
                date TEXT
               )''')
    conn.commit()
    conn.close()
def add(amount , category , message = ''):
    #add new items to database
    date = str(datetime.now().strftime('%Y - %m - %d | %H:%M'))
    c.execute('INSERT INTO expenses VALUES (:amount , :category , :message , :date)' , {'amount':amount , 'category':category , 'message':message , 'date':date})
    conn.commit()
    conn.close()
def show(category=None):
    #show thr all data in database
    if category:
        c.execute("SELECT * FROM expenses WHERE category = (:category)",{'category':category})
        result = c.fetchall()
        c.execute("SELECT sum(amount) FROM expenses WHERE category = (:category)" , {'category':category})
        total_amount = c.fetchone()[0]
    else:
        c.execute("SELECT * FROM expenses")
        result = c.fetchall()
        c.execute("SELECT sum(amount) FROM expenses")
        total_amount = c.fetchone()[0]
    return total_amount,result
    conn.commit()
    conn.close()
def delete():
    c.execute("DELETE FROM expenses")
    conn.commit()
    conn.close()


