#!/usr/bin/python3

def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if possible.

    Args:
        obj: The object to add the attribute to.
        attr_name: The name of the attribute.
        attr_value: The value of the attribute.

    Raises:
        TypeError: If the object can't have a new attribute.

    Example:
        >>> my_obj = {}
        >>> add_attribute(my_obj, "name", "John")
        >>> print(my_obj.name)
        John
    """
    if hasattr(obj, attr_name):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
