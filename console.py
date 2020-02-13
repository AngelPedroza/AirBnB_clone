#!/usr/bin/python3
import cmd

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

    def emptyline(self):
        pass

p = HBNBCommand()
p.cmdloop()
