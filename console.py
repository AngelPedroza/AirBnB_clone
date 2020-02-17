#!/usr/bin/python3
import cmd
from models import storage
from models.engine import file_storage
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """Console for AirBNB clone"""
    prompt = '(hbnb) '

    #Command to help and exit to the console

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
            if bolean == True:
                print(line)
                new_obj_id = storage.create(line)
                print(new_obj_id)

    def do_show(self, line):
        """ command show """
        if line is None or line == "":
             print("** class name missing **")
        else:
            st = line.split(" ")
            length = len(st)
            if st[0] not in storage.str_class():
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
            if st[0] not in storage.str_class():
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
            if st[0] not in storage.str_class():
                print("** class doesn't exist **")
            else:
                for key, value in storage.all().items():
                    if st[0] == type(value).__name__:
                        print([str(value)])

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
        elif st[0] not in storage.str_class():
            print("** class doesn't exist **")
        else:
            k = "{}.{}".format(st[0], st[1])
            boolean = False
            objs = FileStorage.all(self)

            for key, value in storage.all().items():
                if key == k:
                    boolean = True
                    new_value = objs.get(key)
                    setattr(value, st[2], str(st[3]))
                    value.save()
            if boolean == False:
                print("** no instance found **")
    def emptyline(self):
        pass

p = HBNBCommand()
p.cmdloop()
