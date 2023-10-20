from todo import *

try:
    while(1==1):
        print("\n1.ADD A TASK TO BE ADDED \n2.DELETE THE TASK FROM THE LIST \n3.MARK A TASK AS DONE \n4.MARK A TASK AS NOT DONE\n5.DISPLAY ALL TASK \n6.EXIT THIS APPLICATION")
        choice = int(input("\nENTER THE CHOICE FROM THE ABOVE OPTIONS PROVIDED====="))
        
        if(choice ==1):
            task = input("\nENTER YOUR TASK TO ADD=====")
            point = insert_task(task,getpoint())
            saveup(getpoint())
        
        elif(choice==2):
            pointt=int(input("\nENTER THE TASK NUMBER====="))
            point = delete_task(pointt,getpoint)
            savedown(getpoint())
        
        elif(choice==3):
            select = int(input("\nENTER A LINE YOU WANT TO MARK AS DONE====="))
            done_task(select)

        elif(choice==4):
            select = int(input("\nENTER A LINE YOU WANT TO MARK AS NOT DONE====="))
            undoo_task(select)
            
        elif(choice==5):
            c = display_task()
            print("NO         TASK                        STATUS")
            for i in c:
                if(i[2]==0):
                    c=str(i[0])+"         "+i[1].upper()+"          "+"NOTE DONE"
                if(i[2]==1):
                    c=str(i[0])+"         "+i[1].upper()+"          "+"DONE"
                print(c)
    
        elif(choice==6):
            exit()
        else:
            print("\nCHOOSE AN OPTION THAT IS THERE IN THE OPTION LIST*****TRY AGAIN*****...............")

except Exception as err:
    print(f"Error: {err}")
