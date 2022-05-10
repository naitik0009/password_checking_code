#password checking program
#`~!@#$%^&*()-_=+[]\{}|;':",./<>?

password = input("enter your password")
i=0
capital = False
sym = False
num = False
length = False
number = "1234567890"
# symbol = '`~!@#$%^&*()-_=+[]\{}|;':",./<>?'
symbol = ['`','~','!','@','#','$','%','^','&','*','(',')','-','_','=','+','[',']','\r','{','}','|',';',"'",':','"',',','.','/','<','>','?']
while i<len(password):
    # print(password[i])
    if not password[i].isupper() :
        print("")
    if password[i].isupper():
        # print("upper")
        capital = True
    if len(password) >= 9:
        length = True
    if any(x in password[i] for x in number):
        # print("not upper and int")
        num = True
        
    if any(x in password[i] for x in symbol):
        # print("not upper and not int this is symbol")
        sym = True
    
 

    
    i+=1
if num and sym and capital and length:
    print("password created")
if not num:
    print("please include number in your password")
if not sym:
    print("please include special character in your password")
if not length:
    print("please the password length should be greater than 8 length of 8")
if not capital:
    print("please include capital letter in your password")
