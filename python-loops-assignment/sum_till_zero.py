total = 0

n = int(input("Enter a number (0 to stop): "))
while n != 0:
    total += n
    n = int(input("Enter a number (0 to stop): "))
    
print(f"Total: {total}")