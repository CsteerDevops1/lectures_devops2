#!/usr/bin/env python3
"""
Файловая база данных sqlite3
"""
import sqlite3

conn = sqlite3.connect("example.sqlite3")

c = conn.cursor()

# Create table
c.execute("""create table stocks
    (date text, trans text, symbol text, qty real, price real)""")

# Insert a row of data
c.execute("""insert into stocks
    values ("2006-01-05","BUY","RHAT",100,35.14)""")

# Save (commit) the changes
conn.commit()

for t in [
    ("2006-03-28", "BUY", "IBM", 1000, 45.00),
    ("2006-04-05", "BUY", "MSOFT", 1000, 72.00),
    ("2006-04-06", "SELL", "IBM", 500, 53.00),
]:
    c.execute("insert into stocks values (?,?,?,?,?)", t)

c.execute("select * from stocks order by price")
for row in c:
    print(row)

# We can also close the cursor if we are done with it
c.close()
