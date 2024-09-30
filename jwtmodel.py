"""

### DO NOT MODIFY THIS FILE (unless you are me in which case don't forget to update in the other repos)
modified: 9/30/24

"""
import jwt

# Get this call from env
secret_key = "SUPERSECRETEKEY"

class InvalidUserException(Exception):
    def __init__(self, message):
        super().__init__(message)

class JWTUser:
    def __init__(self,token:str) -> None|InvalidUserException:
        '''creates the user from a jwt token, invalid user raises InvalidUserException'''
        self.token = token
        header_data = jwt.get_unverified_header(token)
        try:
            decoded = jwt.decode(token,key=secret_key,algorithms=[header_data['alg'],])
        except jwt.exceptions.InvalidTokenError:
            raise InvalidUserException("invalid jwt token given")
        
        self.name = decoded["sub"]
        self.role = decoded["role"]
    
    def __str__(self) -> str:
        return f"username = {self.name}, role = {self.role}"

    @classmethod
    def constructToken(JWTUser, username:str,role:str):
        '''DO NOT CALL (unless from auth)'''
        payload = {"sub":username,"role":role}
        tok = jwt.encode(payload=payload,key=secret_key)
        return JWTUser(tok)
    
if __name__ == "__main__":
    # mytoken = JWTUser.constructToken("kevin","user")
    # print(mytoken.token)

    try:
        newuser = JWTUser("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJrZXZpbiIsInJvbGUiOiJ1c2VyIn0.LxYkClSbrMmNwl3FoDgMGuWcTfg2pgweZ6_Xmp8eCeI")
        print(newuser.name)
    except jwt.exceptions.InvalidTokenError:
        print("invalid token")
    except Exception as e:
        print(e)
