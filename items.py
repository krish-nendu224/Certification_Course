items =['apple','mango','banana','strawberry']
print(items)
print(items[0])
print(items[0:3])
items.append('kiwi')
items.append('cherry')

print(items)

if 'kiwi' in items:
    print("Present in items")
else:
    print("not present in items")


items.remove('apple')
print(items) 



for i,itt in enumerate(items,start =2):
    print(i,itt)


for i in items:
    print(i)    


while True:
    print("\n1) Add 2)View 3)Exit")
    choice =input("Enter choice:")  

    if choice =="1":
        it = input("Enter item:").strip()
        if it:
            items.append(it)
            print("items in list:",it)
        else:
            ("can't add") 
            
               


