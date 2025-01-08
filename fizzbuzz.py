#creating a new fizzbuzz program

#initialise the counter
x = 0
#while x is less than 50
while x < 50:
#take mod of x
#if x is divisible by 3 print fizz
#if x is divisibile by 5 print buzz
#if x is divisible by 3 and 5 print fizzbuzz
    if x % 3 == 0:
        print("fizz")
    if x % 5 == 0:
        print("buzz")
    if x % 3 == 0 and x % 5 == 0: 
        print("fizzbuzz")
    x+=1
    print(x)

    