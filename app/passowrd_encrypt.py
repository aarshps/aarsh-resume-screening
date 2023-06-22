import bcrypt

def generate_password_hash(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    return hashed_password

def check_password_match(actual_password, expected_hashed_password):
    return bcrypt.checkpw(actual_password.encode(), expected_hashed_password.encode())

password = 'mypassword'
expected_hashed_password = '$2b$12$RlDOvh7JNu/4UNx8JalGw.WA7vWrAeh9kvia9nMkFH7Y74zIfCIuW'

print(generate_password_hash(password))
print(check_password_match(password, expected_hashed_password))
