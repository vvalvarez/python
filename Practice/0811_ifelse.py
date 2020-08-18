minced_meat=True
bread = False
lettuce = True
pepper = True
store = True

if minced_meat and bread and (lettuce or pepper ) and store:
    print("Bon Appetite")
else:
    print("Go to the store")



value = int(input("Enter a number: "))
if value >0:
    print("Positive")
elif value <0:
    print("Negative")
else:
    print("O value is unacceptable")