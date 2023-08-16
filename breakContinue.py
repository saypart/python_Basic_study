count = 0

while True:
    count += 1
    if count == 5:
        continue
    print(f"{count}번째")
    if count > 10:
        break    
