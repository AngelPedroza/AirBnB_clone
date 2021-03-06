#!/usr/bin/python3
"""Gooooooo AirBNB"""
import cmd
import json
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

    # Class Attribute to help precmd
    l_com = ["show", "all", "create", "update", "destroy", "count"]

    def precmd(self, line):
        """
        Excute befoer cmdloop but after the input,
        so this method change the string in line and return it changed
        """
        if "." in line and "(" in line and ")" in line:
            n_l = line.split(".")
            cmm = n_l[1].split("(")
            arg = cmm[1].split(")")
            gg = arg[0]
            if "," in gg:
                gg = gg.replace("\"", "").replace(" ", "")
                gg = gg.split(",")
                gg = "\"{} {} {}\"".format(gg[0], gg[1], gg[2])
            if n_l[0] in storage.DC and cmm[0] in HBNBCommand.l_com:
                line = "{} {} {}".format(cmm[0], n_l[0], gg[1:-1])
        return line

    def do_count(self, line):
        """return how many instances are"""
        count = 0
        if line in storage.DC:
            for key, value in storage.all().items():
                if str(value.__class__.__name__) == line:
                    count += 1
        print(count)

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """EOF execution to exit the program
        """
        return True

    def do_create(self, line):
        """Create a instance of a AirBnb class"""
        if line is None or line == "":
            print("** class name missing **")
        else:
            bolean = False
            if line in storage.DC:
                bolean = True

            if bolean is False:
                print("** class doesn't exist **")
                return
            if bolean is True:
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
                return
            if length < 2:
                print("** instance id missing **")
                return
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
                return
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
        elif length < 2 and st[0] in storage.DC:
            print("** instance id missing **")
        elif length == 2:
            for key, value in storage.all().items():
                if value.id == st[1]:
                    print("** attribute name missing **")
                    return
            print("** no instance found **")
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

                    if valor[-1:] == "\"":
                        valor = valor[1:-1]

                    setattr(value, st[2],
                            type(getattr(value, st[2], "NO ATTR"))(valor))
                    value.save()
            if boolean is False:
                print("** no instance found **")

    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
