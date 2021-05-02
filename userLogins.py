import hashlib,sqlite3

con = sqlite3.connect('file:./db/ppab6.db?mode=rw', uri=True)
cur = con.cursor()

username = input("Please enter your username: ")
password = input("Please enter your password: ")

def is_valid_credentials(username,password):
    isUsernameValid= cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username=?)",(username,)).fetchone()[0]
    retreivedPassword = cur.execute("SELECT password_hash FROM users WHERE username=?",(username,)).fetchone()[0]
    hashedPassword = hashlib.sha256(password.encode()).hexdigest()

    if isUsernameValid and retreivedPassword==hashedPassword:
        return True
    else:
        return False

is_valid_credentials(username,password)