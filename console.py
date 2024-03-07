#!/usr/bin/python3

"""
This module contains the entry point of the command interpreter
"""

import cmd
import shlex
from models import storage
from models import classes
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter class
    """
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
        """Prints the string representation of an instance based on the class
        name and id"""
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
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
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
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        all_objects = storage.all()

        if not arg:
            print([str(instance) for instance in all_objects.values()])
        else:
            args = shlex.split(arg)
            class_name = args[0]

            if class_name not in classes:
                print("** class doesn't exist **")
                return

            for instance in all_objects.values():
                if type(instance).__name__ == class_name:
                    print(str(instance))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
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
        all_objects = storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value_str = args[3]

        instance = all_objects[key]
        attribute_type = type(getattr(instance, attribute_name))

        try:
            attribute_value = attribute_type(attribute_value_str)
        except ValueError:
            print("** invalid value type **")
            return

        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** cannot update attribute {} **".format(attribute_name))
            return

        setattr(instance, attribute_name, attribute_value)
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
