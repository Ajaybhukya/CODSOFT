def addingtask():
    task.append(input("enter your task to added:"))
    print("task added sucessfully")
def viewtasks():
    if not task:
        print("no tasks are found")
    else:
        for index,i in enumerate(task,start=1):
            print(f"{index}.{i}")
def markedtocomplete():
    pos=int(input("enter a position to complete"))
    if 1<=pos<=len(task):
           task[pos-1]="completed"
           print("task is marked")
    else:
        print("invalid position")
def delete () :
    pos=int(input("enter a position"))
    if 1<=pos<=len(task):
        del task[pos-1]
        print("task deleted successfully")
    else:
        print("invalid position")
task=[]
while True:
 print("Menu")
 print("1.add task:")
 print("2.view task:")
 print("3.mark as completed:")
 print("4. delete:")
 print("5. exit")
 ch=int(input("enter your choice:"))
 if ch==1:
     addingtask()
 elif ch==2:
     viewtasks()
 elif ch==3:
    markedtocomplete()
 elif ch==4:
     delete()
 elif ch==5:
      print("Thank you")
      exit()
 else:
      print("Invalid re enter")