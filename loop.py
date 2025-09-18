# item=[]
# key=input("enter a name:")
# value=input("enter a value:")
# dict={key:value}
# item.append(dict)
# print("item with price",item)


# item=[]
# key=input("enter a name:")
# value=input("enter a value:")
# qty=input("enter the quantity")

# dict={'key':key,
#       'value':value,
#       'qty':qty
#       }
# item.append(dict)
# print("item with price",item)

# item=[]
# n=int(input("enter the number of items"))
# for i in range(n):
#     product=input("enter the product:")
#     price=float(input("enter a price"))
#     qty=input("enter qty:")
#     if price >50:
#         discount=price *0.1
#         price=discount
    # dict={
    #     'product':product,
    #     'price':price,
    #     'qty':qty
    # }
    
    # item.append({"product":product,"price":price,"qty":qty})
    # print(item)


item=[]
n=int(input("enter the number of items:"))
for i in range(n):
    product=input("enter the product:")
    price=float(input("enter a price"))
    qty=input("enter qty:")
    if price >50:
        discount=price *0.1
        price=discount
    dict={
        'product':product,
        'price':price,
        'qty':qty
    }
    
    item.append(dict)
    print(item)


