n=int(input('Enter a number:'))
width = n*2
count = 1
for i in range (1, n+1):
    print(("*"*count).center(width))
    count+=2

print("| |".center(width))
