 # Write your code here :-)
price_list={"rice":6,"dall":8,"sugar":3,"salt":2,"snacks":1}
print(price_list)
for item in price_list:
    print(item + " = $ " + str(price_list[item]))
    grand_total_list=[ ]
    all_line_items=[ ]

cart=True
while cart:
    item=input("enter item name:")
    if item=="end":
        cart=False
    else:
       quantity=int(input("enter quantity :"))
       item_price=int(price_list[item])* int(quantity)
       grand_total_list.append(item_price)
       line_item=(item,":",price_list[item],"x", (quantity),"=",(item_price))
       print(all_line_items)
       print(grand_total_list)

