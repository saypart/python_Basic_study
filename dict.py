user = {"name":"상현","age":30,"email":"saypart@gmail.com"}
print(type(user))
print(user["name"])

user["job"] = "웹개발자"
print(user)

del user["age"]
print(user)


keys_list = user.keys()
print(keys_list)
print(type(keys_list))

value_list = user.values()
print(value_list)
print(type(value_list))

item_list = user.items()
print(item_list)
print(type(item_list))