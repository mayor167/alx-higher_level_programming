#!/usr/bin/python3
"""Define base model class"""
import json
import csv
import turtle


class Base:
    """Base model class.

    Represent "base" for classes*.

    Attributes:
        __nb_objects (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new Base.

        Args:
            id (int): Identify the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON serialization of list of dicts.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write JSON serialization of list of objects to file.

        Args:
            list_objs (list): List of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as myjsonfile:
            if list_objs is None:
                myjsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                myjsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of JSON string.

        Args:
            json_string (str): JSON str representation of list of dicts.
        Returns:
            If json_string is None or empty - empty list.
            If not - Python list represented by a json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return the class instantied from dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_cl = cls(1, 1)
            else:
                new_cl = cls(1)
            new_cl.update(**dictionary)
            return new_cl

    @classmethod
    def load_from_file(cls):
        """Return list of classes instantiated from a file of JSON strings.

        Reads from file `<cls.__name__>.json`.

        Returns:
            If file not exist - empty list.
            If not - list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as myjsonfile:
                list_dicts = Base.from_json_string(myjsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write CSV serialization of list of objects to a file.

        Args:
            list_objs (list): List of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as mycsvfile:
            if list_objs is None or list_objs == []:
                mycsvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writ = csv.DictWriter(mycsvfile, fieldnames=fieldnames)
                for myobj in list_objs:
                    writ.writerow(myobj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return list of classes instantiated from CSV file.

        Read from file `<cls.__name__>.csv`.

        Returns:
            If file does not exist - empty list.
            If not - list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as mycsvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(mycsvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares with turtle module.

        Args:
            list_rectangles (list): Rectangle list of objects to draw.
            list_squares (list): Square list of objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
