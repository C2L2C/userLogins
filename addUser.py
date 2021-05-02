import sqlite3,hashlib,getpass
from password_strength import PasswordPolicy

def userCheck(username):
    result= cur.execute("SELECT EXISTS(SELECT 1 FROM users WHERE username=?)",(username,)).fetchone()[0]
    return result

def passwordPolicyCheck(password):

    policy = PasswordPolicy.from_names(
        length=8,  
        uppercase=2,
        numbers=2,  
        special=2,  
        nonletters=2,
        entropybits= 30,  
    )

    Result = policy.test(password) 
    return Result

con = sqlite3.connect('file:./db/ppab6.db?mode=rw', uri=True)
cur = con.cursor()

username=input("Please enter your username: ")
userExists = userCheck(username)
while userExists:
    username = input("The username you entered is already in use! Please type in another username. ")
    userExists = userCheck(username)
else:
    password=getpass.getpass(prompt="Please enter your password: ")
    passwordPolicyCheckResult = passwordPolicyCheck(password)
    while passwordPolicyCheckResult != []:
        password=getpass.getpass(prompt=f"Your password does not satisfy the password policy criteria. Please create a password as per the following criteria: {passwordPolicyCheckResult}")
        passwordPolicyCheckResult = passwordPolicyCheck(password)
    else:    
        hashedPassword=hashlib.sha256(password.encode()).hexdigest()
        cur.execute('''INSERT INTO users VALUES (?,?)''',(username,hashedPassword))
        con.commit()
        print(f"Your user has been created successfully {username}!")
        con.close()