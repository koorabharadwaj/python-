a = int(input("Enter a number: "))
num = a
rev = 0
while a!=0:
    rem = a%10
    rev = rev*10 + rem
    a = a//10
if rev == num:
    print(f'{num} is a palindrome')
else:
    print(f'{num} is not a palindrome')