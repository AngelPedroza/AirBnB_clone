#!/usr/bin/python3
import cmd
from models import storage
from models.engine import file_storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """Console for AirBNB clone"""
    prompt = '(hbnb) '

    #Command to help and exit to the console

    def precmd(self, line):
        new_line = line.replace(".", " ").replace("(","").replace(")","")
       # new_line = new_line.split()
        print(line)
        return new_line

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF execution to exit the program
        """
        return True

    def do_create(self, line):
        """Verificate if line is a AirBnb class"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            bolean = False
            if line in storage.DC:
                bolean = True

            if bolean == False:
                print("** class doesn't exist **")
                return
            if bolean == True:
                new_obj_id = eval(line + "()")
                new_obj_id.save()
                print(new_obj_id.id)

    def do_show(self, line):
        """ command show """
        if line is None or line == "":
             print("** class name missing **")
        else:
            st = line.split(" ")
            length = len(st)
            if st[0] not in storage.DC:
                print("** class doesn't exist **")
            if length < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(st[0], st[1])
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, line):
        """ Function that destroy the instance """
        if line is None or line == "":
             print("** class name missing **")
        else:
            st = line.split(" ")
            length = len(st)
            if st[0] not in storage.DC:
                print("** class doesn't exist **")
            if length < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(st[0], st[1])
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, line):
        """ Print all instances in string representation """
        if line == "":
            print([str(value) for key, value in storage.all().items()])

        else:
            st = line.split(" ")
            if st[0] not in storage.DC:
                print("** class doesn't exist **")
            else:
                counter = 1
                for key, value in storage.all().items():
                    if st[0] in value.__class__.__name__:
                        counter += 1

                i = 1
                for key, value in storage.all().items():
                    if st[0] in value.__class__.__name__:
                        i += 1
                        if i == counter:
                            print([str(value)])
                        else:
                            print([str(value)], end=", ")

    def do_update(self, line):
        """ Updates instance """
        st = line.split(" ")
        length = len(st)

        if line is None or line == "":
            print("** class name missing **")
        elif length < 2:
            print("** instance id missing **")
        elif length == 2:
            print("** attribute name missing **")
        elif length == 3:
            print("** value missing **")
        elif st[0] not in storage.DC:
            print("** class doesn't exist **")
        else:
            k = "{}.{}".format(st[0], st[1])
            boolean = False
            objs = FileStorage.all(self)

            for key, value in storage.all().items():
                if key == k:
                    boolean = True
                    new_value = objs.get(key)
                    valor = st[3]

                    if valor[1:] == "\"":
                        valor = valor[1:-1]

                    setattr(value, st[2], type(getattr(value, st[2], "NO ATTR"))(valor))
                    value.save()
            if boolean == False:
                print("** no instance found **")

    def emptyline(self):
        pass

p = HBNBCommand()
p.cmdloop()
