""""
i = 0
while i < 3:
    print("miau")
    i += 1
"""
"""
for i in range(3):
    print("miau")
"""
"""
print("miau\n" * 3 , end="")
"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's number? "))
        if n>0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()


