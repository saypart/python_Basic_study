#https://docs.python.org/ko/3/library/functions.html
arr = ["a","z","A","Z"]

print(max(arr))
print(min(arr))
arr.sort()
print(arr)
arr.sort(reverse=True)
print(arr)


name = input("이름을 입력하세요")

print(name)
print(f"{len(name)}자리수")

