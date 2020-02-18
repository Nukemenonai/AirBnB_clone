#!/usr/bin/python3
"""
console module
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """ the console """
    prompt = '(hbnb)'

    def do_quit(self):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self):
        """
        Exit command
        """
        return True

    def do_create(classname):
        """
        creates a new instance of basemodel
        arg: Class name
        """
        pass

    def do_show(classname, classid):
        """
        prints the string representation of an instance
        arg 1: class name | arg 2: di
        """
        pass

    def do_destroy(classname, classid):
        """
        Deletes an instance based on the class name
        arg 1: class name | arg 2: id
        """
        pass

    def do_all(classname):
        """
        Prints all string representation of all instances
        argument (optional): class name
        """
        pass

    def do_update(self, arg):
        """
        updates an instance based on name and  id
        arg 1: class name | arg 2: id
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
