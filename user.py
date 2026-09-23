import datetime as dt
import hashlib

from dateutil import parser  # pip install python-dateutil


class User:
    # Part 1: the initializer / constructor
    def __init__(self, username=None, password=None, email=None, birthday=None):
        self._username = username
        self.password = self._encrypt_password(password)
        self.email = email
        self.birthday = birthday

    # Part 2: overriding built-in methods
    def __str__(self):
        age = self.get_age()
        return (f"Username: {self.username}\nPassword: {self.password}"
                f"\nEmail: {self.email}\nAge: {age}")

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"

    def __eq__(self, other):
        return self.username == other.username

    # Part 3: user-defined methods
    def _encrypt_password(self, password):
        password = password.encode("utf-8")
        return hashlib.sha256(password).hexdigest()

    def check_password(self, password):
        password = self._encrypt_password(password)
        return password == self.password

    def get_age(self):
        b_day = parser.parse(self.birthday)
        return int((dt.datetime.now() - b_day).days // 365)

    # Part 4: @property getter and setter
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if not username:
            raise Exception("Username cannot be empty")
        self._username = username


if __name__ == "__main__":
    # Part 1
    user = User("John", "password", "john@some.com", "12/25/1999")
    print(user.username)
    print(user.password)
    print()

    # Part 2
    print(user)
    print()
    print(repr(user))
    print()
    user2 = User("John", "password", "john@some.com", "12/25/1999")
    print(user == user2)
    print()

    # Part 3
    print(user.check_password("1234"))
    print(user.check_password("password"))
    print()

    # Part 4
    user.username = "Jonathan"
    print(user.username)
    try:
        user.username = ""
    except Exception as e:
        print(e)