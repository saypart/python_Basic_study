#https://docs.python.org/ko/3/library/index.html
import time
import random
import datetime
import os



list = [1,2,3,4,5,6,7,8,9]

today = datetime.date.today()
print(today.month)
print(today.day)
print("\n\n")

print(os.getcwd())
print(os.listdir())

for i in range(1,11):
    time.sleep(1)
    x = random.random()
    y = random.randint(1,10)
    random.shuffle(list)
    print(f"random : {x}")
    print(f"randint(1,10) : {y}")
    print(f"shuffle :{list}")
    print(f"choice :{random.choice(list)}")
    print(f"sample :{random.sample(list,3)}")
    print(f"{i}초")