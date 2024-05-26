#!/usr/bin/python3
class SwimMixin:
    """A mixin class that provides swimming behavior.

    Methods:
        swim(): Prints a message indicating the creature swims.
    """

    def swim(self):
        """Prints a message indicating the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """A mixin class that provides flying behavior.

    Methods:
        fly(): Prints a message indicating the creature flies.
    """

    def fly(self):
        """Prints a message indicating the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A class representing a dragon that can swim and fly.

    Methods:
        roar(): Prints a message indicating the dragon roars.
    """

    def roar(self):
        """Prints a message indicating the dragon roars."""
        print("The dragon roars!")
