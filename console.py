#!/usr/bin/python3
""" Console module for AirBnB clone """
import cmd

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

    def default(self, line):
        if line.strip() == "":
            return
        print(f"Command not recognized: {line}")

if __name__ == "__main__":
    console = HBNBCommand()
    console.cmdloop("Welcome to the HBNB console. Type 'quit' or 'EOF' to exit.")
