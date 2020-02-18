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

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """ ummm """
        return True

    def do_create(self, arg):
        """ creates a new instance of basemodel"""
        pass

    def do_show(self, arg):
        """ prints the string representation of an instance """
        pass

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name"""
        pass

    def do_all(self, arg):
        """ Prints all string representation of all instances"""
        pass

    def do_update(self, arg):
        """ updates an instance based on id"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
