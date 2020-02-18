# AirBnB_clone

## Description
This proyect is the console to make a clone of AirBnb. In this proyect we was create the classes that we will use in the next proyects and create a console to manage this clases, save these classes in a file a reloads the classes to the console.

## Command Interpreter Description
The console is the main function in this proyect, you can execute it with the next command:
```
./console.py
```
Once you are in the console these are the commands with the console works:
### Commands
#### create
This command will create us a new instance if this is allowed and return the id of this instance.
**Example:**
```
(hbnb) create BaseModel
ee49c413-023a-4b49-bd28-f2936c95460d
(hbnb)
```
#### show
This command show us the the dictionary of all attributes of an instance with him id and him class name. ***Example:***
```
(hbnb) show BaseModel ee49c413-023a-4b49-bd28-f2936c95460d
[BaseModel] (ee49c413-023a-4b49-bd28-f2936c95460d) {'id': 'ee49c413-023a-4b49-bd28-f2936c95460d', 'created_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251939), 'updated_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251972)}
(hbnb)
```
#### all
This command show us all the instances created. We can filtring this command passing the name of a class that we want find. With this method we can find each instance with the same class name. ***Example:***
```
(hbnb) all
["[BaseModel] (680f12dd-e238-476f-8f08-3a1d7358c22e) {'id': '680f12dd-e238-476f-8f08-3a1d7358c22e', 'created_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251939), 'updated_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251972)}", "[User] (ef10aa9f-f388-48bc-b0bf-25283bc01ffc) {'id': 'ef10aa9f-f388-48bc-b0bf-25283bc01ffc', 'created_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778004), 'updated_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778030)}"]
(hbnb)all BaseModel
["[BaseModel] (680f12dd-e238-476f-8f08-3a1d7358c22e) {'id': '680f12dd-e238-476f-8f08-3a1d7358c22e', 'created_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251939), 'updated_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251972)}"]
(hbnb) all User
["[User] (ef10aa9f-f388-48bc-b0bf-25283bc01ffc) {'id': 'ef10aa9f-f388-48bc-b0bf-25283bc01ffc', 'created_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778004), 'updated_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778030)}"]
(hbnb)
```
#### update
This command, like a him name update the attributes of a instance. For do thi, the command needs the class name of the instance that we will update, him id and the key and value that will set them in the object. If we pass more attributes this extra attributes will be ignore. ***Example:***
```
(hbnb) show BaseModel 680f12dd-e238-476f-8f08-3a1d7358c22e
[BaseModel] (680f12dd-e238-476f-8f08-3a1d7358c22e) {'id': '680f12dd-e238-476f-8f08-3a1d7358c22e', 'created_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251939), 'updated_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251972)}
(hbnb)update BaseModel 680f12dd-e238-476f-8f08-3a1d7358c22e first_name "Betty"
(hbnb) show BaseModel 680f12dd-e238-476f-8f08-3a1d7358c22e
[BaseModel] (680f12dd-e238-476f-8f08-3a1d7358c22e) {'id': '680f12dd-e238-476f-8f08-3a1d7358c22e', 'created_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251939), 'updated_at': datetime.datetime(2020, 2, 18, 16, 18, 44, 868841), 'first_name': 'Betty'}
(hbnb)update BaseModel 680f12dd-e238-476f-8f08-3a1d7358c22e email "prouve@holbertonschool.com" no_set "NO_SET"
(hbnb) show BaseModel 680f12dd-e238-476f-8f08-3a1d7358c22e
[BaseModel] (680f12dd-e238-476f-8f08-3a1d7358c22e) {'id': '680f12dd-e238-476f-8f08-3a1d7358c22e', 'created_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251939), 'updated_at': datetime.datetime(2020, 2, 18, 16, 20, 29, 136358), 'first_name': 'Betty', 'email': 'prouve@holbertonschool.com'}
(hbnb)
```
#### destroy
This command delete the instance that the user specificate if this instance exist. For delete a instance we need the class name of the instance and him id. The syntax is similar to show command. ***Example:***
```
(hbnb) show BaseModel 680f12dd-e238-476f-8f08-3a1d7358c22e
[BaseModel] (680f12dd-e238-476f-8f08-3a1d7358c22e) {'id': '680f12dd-e238-476f-8f08-3a1d7358c22e', 'created_at': datetime.datetime(2020, 2, 18, 16, 5, 18, 251939), 'updated_at': datetime.datetime(2020, 2, 18, 16, 20, 29, 136358), 'first_name': 'Betty', 'email': 'prouve@holbertonschool.com'}
(hbnb) destroy BaseModel 680f12dd-e238-476f-8f08-3a1d7358c22e
(hbnb) show BaseModel 680f12dd-e238-476f-8f08-3a1d7358c22e
** no instance found **
(hbnb)
```
#### count
This command return how many instance of the class exist. ***Example:***
```
(hbnb) all
["[User] (ef10aa9f-f388-48bc-b0bf-25283bc01ffc) {'id': 'ef10aa9f-f388-48bc-b0bf-25283bc01ffc', 'created_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778004), 'updated_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778030)}", "[User] (29f6e3f3-ac91-4bc5-831f-28a69e50a249) {'id': '29f6e3f3-ac91-4bc5-831f-28a69e50a249', 'created_at': datetime.datetime(2020, 2, 18, 16, 27, 30, 26059), 'updated_at': datetime.datetime(2020, 2, 18, 16, 27, 30, 26087)}", "[BaseModel] (7fe27032-6d35-47c4-890f-6b3aa0ae6f3c) {'id': '7fe27032-6d35-47c4-890f-6b3aa0ae6f3c', 'created_at': datetime.datetime(2020, 2, 18, 16, 27, 41, 583126), 'updated_at': datetime.datetime(2020, 2, 18, 16, 27, 41, 583153)}"]
(hbnb) count User
2
(hbnb) count BaseModel
1
(hbnb)
```

### More infomation
This console can manage syntax like a OOP with him commands. This is the syntax: ***<ClassName>.<Command>(). Let me show a ***Example:***
```
(hbnb) User.all()
["[User] (ef10aa9f-f388-48bc-b0bf-25283bc01ffc) {'id': 'ef10aa9f-f388-48bc-b0bf-25283bc01ffc', 'created_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778004), 'updated_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778030)}"], ["[User] (29f6e3f3-ac91-4bc5-831f-28a69e50a249) {'id': '29f6e3f3-ac91-4bc5-831f-28a69e50a249', 'created_at': datetime.datetime(2020, 2, 18, 16, 27, 30, 26059), 'updated_at': datetime.datetime(2020, 2, 18, 16, 27, 30, 26087)}"]
(hbnb) User.count()
2
(hbnb) User.show("ef10aa9f-f388-48bc-b0bf-25283bc01ffc")
[User] (ef10aa9f-f388-48bc-b0bf-25283bc01ffc) {'id': 'ef10aa9f-f388-48bc-b0bf-25283bc01ffc', 'created_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778004), 'updated_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778030)}
(hbnb) User.update("ef10aa9f-f388-48bc-b0bf-25283bc01ffc", "first_name", "Betty")
(hbnb) User.show("ef10aa9f-f388-48bc-b0bf-25283bc01ffc")
[User] (ef10aa9f-f388-48bc-b0bf-25283bc01ffc) {'id': 'ef10aa9f-f388-48bc-b0bf-25283bc01ffc', 'created_at': datetime.datetime(2020, 2, 18, 16, 11, 26, 778004), 'updated_at': datetime.datetime(2020, 2, 18, 16, 31, 46, 136633), 'first_name': 'Betty'}
(hbnb)
```
