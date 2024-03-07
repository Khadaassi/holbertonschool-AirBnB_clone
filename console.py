#!/usr/bin/python3

"""This module contains the entry point of the command interpreter"""

import cmd
from models import f_storage
from models import classes
from models.engine.file_storage import FileStorage


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

def do_create(self, arg):
    """Create a new instance of BaseModel"""
    if not arg:
        print("** class name missing **")
        return
    
    args = arg.split()
    class_name = args[0]

    if class_name not in classes:
        print("** class doesn't exist **")
        return

    new_instance = classes[class_name]()
    new_instance.save()
    print(new_instance.id)

    
def do_show(self, arg):
    """Prints the string representation of an instance based on the class name and id"""
    args = arg.split()

    if not args:
        print("** class name missing **")
        return

    class_name = args[0]

    if class_name not in classes:
        print("** class doesn't exist **")
        return

    if len(args) < 2:
        print("** instance id missing **")
        return

    instance_id = args[1]
    key = "{}.{}".format(class_name, instance_id)
    all_objects = f_storage.all()

    if key not in all_objects:
        print("** no instance found **")
        return

    print(all_objects[key])



if __name__ == "__main__":
    HBNBCommand().cmdloop()
