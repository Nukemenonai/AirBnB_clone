#!/usr/bin/python3
"""
console module
"""
import cmd
import sys
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models
import json


objs = {'BaseModel': BaseModel, 'User': User, 'State': State, 'City': City,
        'Amenity': Amenity, 'Place': Place, 'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ the console """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        "Doesn't execute an action"
        pass

    def do_EOF(self, args):
        """
        Exit command
        """
        print("")
        return True

    def do_create(self, args):
        """
        creates a new instance of basemodel
        arg: Class name
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            if args in objs:
                new = eval(str(args) + "()")
                new.save()
                print(new.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """
        prints the string representation of an instance
        arg 1: class name | arg 2: di
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            sp = args.split()
            if sp[0] in objs:
                if len(sp) < 2:
                    print("""** instance id missing **""")
                else:
                    Objcls = models.storage.all()
                    key = str(sp[0]) + "." + str(sp[1])
                    if key in Objcls:
                        print(Objcls[key])
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name
        arg 1: class name | arg 2: id
        """
        if args is None or len(args) == 0:
            print("** class name missing **")
        else:
            sp = args.split()
            if sp[0] in objs:
                if len(sp) < 2:
                    print("""** instance id missing **""")
                else:
                    Objcls = models.storage.all()
                    key = str(sp[0]) + "." + str(sp[1])
                    if key in Objcls:
                        del(Objcls[key])
                        models.storage.save()
                    else:
                        print("** no instance found **")
            else:
                print("** class doesn't exist **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        argument (optional): class name
        """
        Objcls = models.storage.all()
        objects = []
        if args is "":
            for key in Objcls:
                objects.append(str(Objcls[key]))
            print(objects)
        else:
            try:
                sp = args.split()
                eval(sp[0])
                for obj in Objcls:
                    _dict = Objcls[obj].to_dict()
                    if _dict['__class__'] == sp[0]:
                        objects.append(str(Objcls[obj]))
                print(objects)
            except:
                print("** class doesn't exist **")

    def do_update(self, args):
        """
        updates an instance based on name and  id
        arg 1: class name | arg 2: id
        """
        sp = shlex.split(args)
        if len(sp) == 0:
            print("** class name missing **")
        else:
            try:
                eval(str(sp[0]))
            except:
                print("** class doesn't exist **")
                return
            if len(sp) == 1:
                print("** instance id missing **")
            else:
                Objcls = models.storage.all()
                attr = str(sp[0]) + "." + str(sp[1])
                if attr not in Objcls:
                    print("** no instance found **")
                else:
                    if len(sp) == 2:
                        print("** attribute name missing **")
                    else:
                        if len(sp) == 3:
                            print("** value missing **")
                        else:
                            setattr(Objcls[attr], sp[2], sp[3])
                            models.storage.save()

    def do_count(self, args):
        """Count the number of instances of a class"""
        nb_objects = 0
        objects = models.storage.all()
        new = {}
        for obj in objects:
            new[obj] = objects[obj].to_dict()
        for n_obj in new:
            if (args == new[n_obj]['__class__']):
                nb_objects = nb_objects + 1
        print(nb_objects)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
