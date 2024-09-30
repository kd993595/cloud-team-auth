# Run this file to setup sqlite database

import sqlite3

conn = sqlite3.connect('authtest.db')
curr = conn.cursor()

curr.execute('''CREATE TABLE USER_AUTH
         (USERID         INTEGER PRIMARY KEY,
         USERNAME        VARCHAR(32)     NOT NULL,
         EMAIL           VARCHAR(32)     NOT NULL,
         PASSWORD        BINARY(60));''')
curr.execute("CREATE UNIQUE INDEX idx_auth_username ON USER_AUTH (USERNAME);")

# curr.execute("INSERT INTO USER_AUTH (USERNAME,EMAIL,PASSWORD) VALUES (?,?,?)",
#              ('Allen', 'some@email', b'$2b$12$TGan3NbRLLQywI12WXwaM.wFE89XZsRa53ob6DrXOCVBZ832Z3j1i'));

# curr.execute("INSERT INTO USER_AUTH (USERNAME,EMAIL,PASSWORD) VALUES (?,?,?)",
#              ('Bob', 'fake@email', b'$2b$12$xhKhmVc4NykktrHrR2F/BO8VRFdc1SRJKkIl2cjZNb8WQpOn6U2cm'));

# conn.commit()

# records = curr.execute("SELECT * from USER_AUTH where USERID >= ?",(1,))
# print(records.fetchone())
# for row in records:
#     print(row[0])

conn.close()