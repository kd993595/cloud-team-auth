import uvicorn
from fastapi import FastAPI,Response, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

from jwtmodel import JWTUser,InvalidUserException
from authModel import AuthModel


class UserItem(BaseModel):
    username: str
    email: str
    password: str

class UserToken(BaseModel):
    username: str
    email: str


app = FastAPI()

origins = [
    "http://localhost:8080",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection
conn = sqlite3.connect('./authtest.db')
mainAuth = AuthModel(conn)

@app.get("/")
async def root():
    return {"message": "Hello Authentication"}

@app.get("/userAuth")
async def getToken(username:str, password:str):
    maybeUser = mainAuth.selectUser(username,password)
    if maybeUser is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"msg":"invalid token"})

    return JSONResponse(content={"token": maybeUser.token})

@app.post("/userAuth", response_model=UserToken,status_code=201)
async def createUser(user:UserItem, response: Response):
    try:
        mainAuth.insertUser(user.username,user.email,user.password)
    except ValueError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"msg":"invalid input"}
    except:
        response.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        return {"msg":"cannot create user"}

    return user


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7979)