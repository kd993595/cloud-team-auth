import bcrypt
from jwtmodel import JWTUser, InvalidUserException

import sqlite3


# Get this call from env
pepper = b"secret-pepper"

class AuthModel:
    def __init__(self,conn:sqlite3.Connection) -> None:
        self.conn = conn
    
    def insertUser(self, username:str, email:str,password:str):
        if len(username) < 3 or len(username)>32:
            raise ValueError
        if len(email)<3 or len(email)>32 or len(password)<8:
            raise ValueError
        salt = bcrypt.gensalt()
        password = str.encode(password)
        hashStr = bcrypt.hashpw(password+pepper,salt)

        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO USER_AUTH (USERNAME,EMAIL,PASSWORD) VALUES (?,?,?)",(username, email, hashStr)) #may raise error
        self.conn.commit()
            

    def selectUser(self,username:str,password:str):
        '''Does not return error only returns none when invalid user'''
        cursor = self.conn.cursor()
        records = cursor.execute("SELECT * from USER_AUTH where USERNAME = ?",(username,))
        maybeUser = records.fetchone()
        if maybeUser is None:
            return None
        savedPass = maybeUser[3]

        password = str.encode(password)
        hashStr = bcrypt.hashpw(password+pepper,savedPass)
        if hashStr != savedPass:
            return None
        return JWTUser.constructToken(username=maybeUser[1],role="user")

if __name__=='__main__':
    conn = sqlite3.connect('./authtest.db')
    newAuth = AuthModel(conn)

    # try:
    #     newAuth.insertUser("kevin","some@email.com","securepassword")
    #     newAuth.insertUser("tim","fake@email.com","fakepassword")
    #     newAuth.insertUser("bob","test@email.com","somepassword")
    # except Exception as e:
    #     print(e)

    maybeUser = newAuth.selectUser("tim","fakepassword")
    print(maybeUser)




    