list=[1,2,3,3,4,5,65,76]
def add():
    new=int(input("what you want to add: "))
    list.append(new)
def update():
    j=0
    for i in list:
        j+=1
        print (f"{i} - {j}")
    choice= int(input("choose number of element you want to change "))
    change= int(input("write new number: "))
    list[choice-1]=change
    print(list)
def delete():
    j=0
    for i in list:
        j+=1
        print (f"{i} - {j}")
    choice= int(input("choose the number you want to delete "))
    list.remove(list[choice-1])
    print(list)
def main():
    while True:
        selection=int(input("if you want to add write - 1\n" +
                        "if you want pudate write - 2\n" +
                        "if you want to remove write - 3\n" +
                        "if you want to see list write - 4\n" +
                        "if you want to stop write - 5 "))
        if selection==1:
            add()
        elif selection==2:
            update()
        elif selection==3:
            delete()
        elif selection==4:
            for i in list:
                print(i)
        elif selection==5:
            break
main()
