DB Design - 

Create Table TaskLists (taskId int Primary Key , title varchar, description varchar)
Create Table TaskItems (itemId int Primary Key, title varchar, taskListId int Foreign Key references TaskLists(taskId))


DRIVER_NAME = SQL Server
SERVER_NAME =  get it from command Select @@SERVERNAME in MS SQL Server Management Studio
DATABASE_NAME = master



pip install openai
pip install pypyodbc
pip install requests