from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

password = 'panatha13'

hashed_password = bcrypt.generate_password_hash(password=password)

print(hashed_password)

check = bcrypt.check_password_hash(hashed_password,'panatha13')
print(check)

#alternative
# from werkzeug.security import generate_password_hash,check_password_hash

# hashed = generate_password_hash('panatha13')
# check = check_password_hash(hashed,'panatha13')