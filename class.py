class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hello(self):
        print("hello")

user_1 = User("상현",11)
user_2 = User("현상",20)

user_1.hello()
user_2.hello()


print(user_1.name)
print(user_1.age)

print(user_2.name)
print(user_2.age)

print(type(user_1))