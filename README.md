fantastic4-ToDoList
===================

A DIM Collaborative ToDoList
============================

download README.doc for installation manual




Installation manual for Fantastic4 ToDoList

System Prerequisite:

• Python 2.7 (with python path already set)

•	Setuptools 2.2

•	Virtualenv 1.11.4


Content:

1.	Downloading ToDoList project from GitHub

2.	Setup virtual environment

3.	Sync database,  populate data and run server





Downloading ToDoList project from GitHub

•	Go to https://github.com/yeekeng/fantastic4-ToDoList

•	Download the project as a zip file by clicking on the ‘Download Zip’ button

•	Save it onto the desktop, you should see ‘fantastic4-ToDoList-master.zip’ when the download is completed.

•	Right-click on ‘fantastic4-ToDoList-master.zip’ and choose ‘Extract Here’.

•	If everything is done correctly, ‘fantastic4-ToDoList-master’ folder should be seen on the desktop




Setup Virtual Environment

•	Start a new Command Prompt(cmd)

•	Using  cmd, go into the directory ‘fantastic4-ToDoList-master/ToDoList_project’

•	By now you should be in the directory ToDoList_project, you can confirm this by running a ls command. The following files will be listed

o	ToDoList_project

o	manage.py             

o	readme_yk.txt     

o	static    

o	to_do_list

o	populate_todolist.py  

o	requirements.txt  

o	templates

•	when this is confirmed, create a virtual environment by running the command 
virtualenv env 

•	when setup is completed, go into the directory env/Scripts 

•	install django 1.6.2 by running the command pip install django==1.6.2 
(alternative installation is by installing through requirements file)

•	when installation of django is done, run activate.bat by running the command activate

•	This will activate the environment to run ToDoList project. If this is done correctly, the cmd should display <env>.
Sync database, populate data and run server

•	Go back to the directory ToDoList_project. 

•	Create a database for ToDolist by running the command python manage.py syncdb

•	The cmd will prompt you to create a superuser, it is recommend that you follow the screen and create a superuser, so that you can login to the admin site to mange the TodoList system.

•	After this is done, go into python shell by running the command python manage.py shell

•	you should see that the cmd has change to >>> 

•	type in import populate_todolist

•	this will create the necessary users and group for testing.

•	Exit the shell by running the command exit() and this will bring you back to the directory.

•	Start the server by running the command python manage.py runserver


When the server is started, visit the ToDoList page by going to http://127.0.0.1:8000 or the address as stated at the cmd when the server is started.


Test user account can be access by:


Username: user1

Password: user1


A Deployed version can be access at http://yeekeng.pythonanywhere.com/ 




