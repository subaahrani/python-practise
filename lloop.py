# Write your code here :-)
print (list(range(1,5)))
for item in list(range(1,5)):
    print(item)


number=23
running=True
while running:
    guess=int(input("enter an integer:"))
    if guess==number:
        print("congratulations, you guessedit.")
        running=False
    elif guess<number:
        print("NO,it is a little higher than that.")
    else:
        print("No,it is a little lower than that.")
    print("Done")


