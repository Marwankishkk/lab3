import re
import uuid
class User:
    users=list()
    def __init__(self,name,email,password,phone):
        self.name=name
        self._password=password
        self._phone=phone
        self.email=email
        self.id=uuid.uuid4()
        self.save_user("UserDataBase")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        if  re.match('\w+@\w+',email):
            self._email=email
        else:
            print("Please write valid email")
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self,phone):
        if re.match(r'^(\+20|0)?(10|11|12|15|16|17|18|19)[0-9]{8}$', str(phone)):
            self._phone = phone
        else:
            print("invalid phone number")
    def save_user(self,filename):
        user=dict()
        user["name"]=self.name
        user["email"]=self.email
        user["phone"]=self.phone
        user["Password"]=self._password
        user["id"]=self.id
        self.users.append(user)

        with open(filename,'w') as file:
            for item in self.users:
                file.write(str(item) + "\n")


def validateacc():
    name = input("Please enter your account name ")
    password = input("pass ")
    for x in User.users:
        if x["name"] == name and x["Password"] == password:
            print("ok")
            break
def signup():
    name = input("Enter your name ")
    print("Please enter mail")
    while True:
        email = input()
        if re.match('\w+@\w+', email):
            break
        else:
            print("Please enter valid email")

    print("Please enter your phone")
    while True:
        phone = input()
        if re.match(r'^(\+20|0)?(10|11|12|15|16|17|18|19)[0-9]{8}$', str(phone)):
            break
        else:
            print("Please enter valid phone")
    password = input("Please enter your password")
    return name,email,password,phone


