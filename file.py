# Write your code here :-)
f=open("poem.txt","r")
all_content=f.readlines()
print(all_content)
for line in all_content:
    splitted_line=line.split(" ")
    word_count=len(splitted_line)
    print(word_count)


price_list=[3,4,5,6,7,9]
sum(price_list)
total=[]
for item in price_list:
    total.append(item)
print(sum(total))
total=0
for item in price_list:
    total=total+item
    print(total)
