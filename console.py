#!/usr/bin/python3
"""
console module
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ the console """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        'Quit command to exit the program'
        return True

    def do_EOF(self, arg):
        ' ummm '
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
