#!/usr/bin/python3

""" Console module for AirBnB clone """

import cmd
import shlex
import models


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

    def do_create(self, line):
        """Create an instance and save it"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        instance = getattr(models, class_name)()
        instance.save()
        print(instance.id)

    def do_show(self, line):
        """Prints the string rep of an instance"""
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return

        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on class name + ID"""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        all_objects = models.storage.all()
        key = "{}.{}".format(class_name, instance_id)

        if key not in all_objects:
            print("** no instance found **")
            return

        del all_objects[key]
        models.storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        all_objects = models.storage.all()

        if not arg:
            print([str(instance) for instance in all_objects.values()])
        else:
            args = shlex.split(arg)
            class_name = args[0]

            if class_name not in models.classes:
                print("** class doesn't exist **")
                return

            for instance in all_objects.values():
                if type(instance).__name__ == class_name:
                    print(str(instance))

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        class_name = args[0]

        if class_name not in models.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        all_objects = models.storage.all()

        if key not in all_objects:
            print("** no instance found **")
            return

        # loop step per 2
        for idx in range(2, len(args), 2):
            attribut_name = args[idx].replace("{", "").replace(":", "")
            attribut_value = args[idx + 1].replace("}", "")

            if attribut_name in models.int_attrs:
                setattr(all_objects[key], attribut_name, int(attribut_value))

            elif attribut_name in models.float_attrs:
                setattr(all_objects[key], attribut_name, float(attribut_value))

            else:
                setattr(all_objects[key], attribut_name, attribut_value)

        all_objects[key].save()


if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop("Welcome to the HBNB console. Type 'quit' or 'EOF' to exit.")
