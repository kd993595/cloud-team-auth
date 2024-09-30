import bcrypt


# Declaring pepper
pepper = b"some-pepper"

# Declaring our password
password = b'password'


# Adding the salt to password
salt = bcrypt.gensalt()
# Hashing the password
hashed = bcrypt.hashpw(password+pepper, salt)

print(f"length pass: {len(password)}")
print(f"length hash: {len(hashed)}")

# printing the salt
print("Salt :")
print(salt)

# printing the hashed
print("Hashed :")
print(hashed)

newhash = bcrypt.hashpw((b'newpassword')+pepper,hashed)
print(newhash == hashed)