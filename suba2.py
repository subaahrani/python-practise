# Write your code here :-)
import sys
input_file=open("suba1.py","r")
all_items=input_file.readlines( )
price_list={ }
for item in all_items:
    item_name=item.split(" ,")[0].strip()
    item_price=item.split(",")[1].strip()
    price_list[item_name]=item_price.strip( )
print(price_list)

