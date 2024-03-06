import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Exit the program"""
        print("Exiting...")
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        print("Exiting...")
        return True

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        if arg == "":
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if cls_name not in storage.classes.keys():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = f"{cls_name}.{obj_id}"
            if key in storage.all():
                print(storage.all()[key])
            else:
                print("** no instance found **")
        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if cls_name not in storage.classes.keys():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = f"{cls_name}.{obj_id}"
            if key in storage.all():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")
        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        args = arg.split()
        obj_list = []
        if len(args) == 0:
            for obj in storage.all().values():
                obj_list.append(str(obj))
        else:
            cls_name = args[0]
            if cls_name not in storage.classes.keys():
                print("** class doesn't exist **")
                return
            for key, obj in storage.all().items():
                if key.split('.')[0] == cls_name:
                    obj_list.append(str(obj))
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            cls_name = args[0]
            if cls_name not in storage.classes.keys():
                print("** class doesn't exist **")
                return
            if len(args) < 2:
                print("** instance id missing **")
                return
            obj_id = args[1]
            key = f"{cls_name}.{obj_id}"
            if key not in storage.all():
                print("** no instance found **")
                return
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attr_name = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            attr_value = args[3]
            obj = storage.all()[key]
            setattr(obj, attr_name, attr_value.strip('"'))
            obj.save()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop("Welcome to the HBNB console. Type 'quit' or 'EOF' to exit.")
