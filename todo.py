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



def insert_task(point):
    try:
        task = input("\nENTER YOUR TASK TO ENTER INTO THE LIST======")
        query = "INSERT INTO todo (num,tasks, status) VALUES (%s, %s, %s);"
        para = (point+1,task,False,)
        cursor.execute(query,para)
        return point+1

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def delete_task(point):
    try:
        dell = int(input("\nselect the task you want to delete====="))
        query = "DELETE FROM todo WHERE num=%s"
        cursor.execute(query,(dell,))
        query = "UPDATE todo SET num = num - 1 WHERE num > %s"
        cursor.execute(query,(dell,))
        return point-1

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def done_task():
    try:
        select = int(input("\nselect one task that you have completed====="))
        query = "UPDATE todo SET status =%s WHERE num=%s"
        cursor.execute(query,(True,select,))


    except mysql.connector.Error as err:
        print(f"Error: {err}")

def display_task():
    try:
        query = "SELECT * FROM todo;"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("\n")
        for row in rows:
            print(row)


    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

