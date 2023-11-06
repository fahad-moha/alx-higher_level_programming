#!/usr/bin/python3

class MyInt(int):
    """
    A custom integer class that inherits from the built-in int class.
    """

    def __eq__(self, other):
        """
        Overrides the equality operator (==) to invert its behavior.

        Args:
            other: The object to compare the MyInt instance with.

        Returns:
            True if the values are not equal, False otherwise.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to invert its behavior.

        Args:
            other: The object to compare the MyInt instance with.

        Returns:
            True if the values are equal, False otherwise.
        """
        return super().__eq__(other)
