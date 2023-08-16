user_data ={"name" : "상현","age" : 20, "email":"saypart@gmail.com"}


for data in user_data:
    print(f"{data} : {user_data[data]}")

print("\n \n.items 사용")
for data in user_data.items():
    print(f"{data[0]} : {data[1]}")