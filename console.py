#!/usr/bin/python3
""" Console module for AirBnB clone """

import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        print("Exiting...")
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        print("Exiting...")
        return True
    
    def emptyline(self):
        """Do nothing when user input is empty"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()