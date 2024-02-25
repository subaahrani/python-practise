# Write your code here :-)
menu={"idly":2.50,
      "dosai":10.00,
      "coffee":5.00,
      "ice_creeam":5.00,
      100:"hundred"}

print (menu["idly"])
print( menu[100])

poem="""Programming is fun
When the workis done"""
f=open("poem.txt","w")
f.write(poem)
f.close()



f=open("poem.txt","r")
for line in f.readlines():
    print(line)
f.close()

f=open("poem.txt","r")
print(f.readlines())
all_content=f.readlines()
for line in all_content:
    print(line)
