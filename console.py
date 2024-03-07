#!/usr/bin/python3

"""This module contains the entry point of the command interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the program"""
        print("Exiting...")
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("Exiting...")
        return True
    
    def emptyline(self):
        """Do nothing when user input is empty"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
