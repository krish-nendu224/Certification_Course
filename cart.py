cart =[]
#add
cart.append("book")
cart.append("pen")
cart.append("pencil")
cart.append("diary")
#remove
cart.remove("book")

cart.append("book")
#update
cart[3] ="storybook"
print(cart)
#view all items 
for i,items in enumerate(cart):
    print(i,items)

#search using in
if "Pen" in cart:
    print("Pen is in the list")  
#else:

    #print("not present in the list")

#to find length of cart
print(len(cart))  

#slice
print(cart[1:3])

#to sort
print(sorted(cart))