import sqlite3


conn = sqlite3.connect('.\\..\\database\\accounts.db')

c = conn.cursor()

c.execute("""CREATE TABLE accounts (
            Username text,
            Password text,
            ID integer,
            private_key text
            )""")