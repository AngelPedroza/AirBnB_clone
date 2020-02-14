#!/usr/bin/python3
import cmd
from models import storage
from models.engine import file_storage

class HBNBCommand(cmd.Cmd):
    """Console for AirBNB clone"""
    prompt = '(hbnb)'

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
            for key, value in storage.all().items():
                if line == value.__class__.__name__:
                    bolean = True

            if bolean == False:
                print("** class doesn't exist **")

    def do_show(self, line):
        """ command show """

        if line is None or line == "":
            print("** class name missing **")
        else:
            class_error = 0
            for key, value in storage.all().items():
                if line == "{} {}".format(value.__class__.__name__, value.id):
                    print(value.__class__.__name__, value.id)
                    class_error = 1
                elif line == value.__class__.__name__ and line != value.id:
                    print("** no instance found **")
                    class_error = 1
                if line == value.__class__.__name__:
                    class_error = 1
                    print("** instance id missing **")
                    break

            if class_error == 0:
                print("** class doesn't exist **")

    def emptyline(self):
        pass

p = HBNBCommand()
p.cmdloop()
