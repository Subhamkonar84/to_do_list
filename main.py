from todo import *

try:
    file=open("choice.txt",'r')
    point=int(file.read())
    file.close()
    file=open("choice.txt",'w')
    while(1==1):
        print("\n1.add a task \n2.delete from the list \n3.mark that list as done \n4.display \n5.exit")
        choice = int(input("\nenter your choice from the above options====="))
        
        if(choice ==1):
            point = insert_task(point)
            file.write(str(point))
        
        elif(choice==2):
            point = delete_task(point)
            file.write(str(point))
        
        elif(choice==3):
            done_task()
            
        elif(choice==4):
            display_task()
    
        elif(choice==5):
            file.close()
            exit()
        else:
            print("\nchoose a correct option that is present in the above option")

except Exception as err:
    connection.rollback()
    print(f"Error: {err}")
