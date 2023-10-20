import mysql.connector

# Establishing a connection to the MySQL database
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="to_do"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()
query = "CREATE TABLE IF NOT EXISTS todo (num INT,tasks LONGTEXT,status TINYINT(1) DEFAULT 0);"
cursor.execute(query)

def getpoint():
    file=open("choice.txt",'r')
    point=int(file.read())
    file.close()
    return point

def saveup(point):
    file=open("choice.txt",'w')
    file.write(str(point+1))
    file.close()

def savedown(point):
    file=open("choice.txt",'w')
    file.write(str(point-1))
    file.close()

def insert_task(task,point):
    try:
        query = "INSERT INTO todo (num,tasks, status) VALUES (%s, %s, %s);"
        para = (point+1,task,False,)
        cursor.execute(query,para)
        return point+1

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_task(dell,point):
    try:
        query = "DELETE FROM todo WHERE num=%s"
        cursor.execute(query,(dell,))
        query = "UPDATE todo SET num = num - 1 WHERE num > %s"
        cursor.execute(query,(dell,))
        return point-1

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def done_task(select):
    try:
        #select = int(input("\nselect one task that you have completed====="))
        query = "UPDATE todo SET status =%s WHERE num=%s"
        cursor.execute(query,(True,select,))


    except mysql.connector.Error as err:
        print(f"Error: {err}")

def undoo_task(select):
    try:
        #select = int(input("\nselect one task that you have completed====="))
        query = "UPDATE todo SET status =%s WHERE num=%s"
        cursor.execute(query,(False,select,))


    except mysql.connector.Error as err:
        print(f"Error: {err}")

def display_task():
    try:
        query = "SELECT * FROM todo;"
        cursor.execute(query)
        rows = [list(row) for row in cursor.fetchall()]
        return rows


    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

