class Fish:
    """A class representing a fish.

    Methods:
        swim(): Prints a message indicating the fish is swimming.
        habitat(): Prints a message indicating the fish's habitat.
    """

    def swim(self):
        """Prints a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Prints a message indicating the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird.

    Methods:
        fly(): Prints a message indicating the bird is flying.
        habitat(): Prints a message indicating the bird's habitat.
    """

    def fly(self):
        """Prints a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints a message indicating the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish, inheriting from both Fish and Bird.

    Methods:
        fly(): Overrides the fly method to print "The flying fish is soaring!".
        swim(): Overrides the swim method to print "The flying fish is swimming!".
        habitat(): Overrides the habitat method to print "The flying fish lives both in water and the sky!".
    """

    def fly(self):
        """Prints a message indicating the flying fish is soaring!"""
        print("The flying fish is soaring!")

    def swim(self):
        """Prints a message indicating the flying fish is swimming!"""
        print("The flying fish is swimming!")

    def habitat(self):
        """Prints a message indicating the habitat of the flying fish."""
        print("The flying fish lives both in water and the sky!")
