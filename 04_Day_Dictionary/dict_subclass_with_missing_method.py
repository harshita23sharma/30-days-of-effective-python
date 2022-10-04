"""
We can define our own dict subclass with a __missing__ method in order to
construct default values that must know  which key was being accessed.
Also, drawvback of defaultdict is overcome here as defaultdict can not have
any argument in the function passed, so we can't access or have
default value depending on the key being accessed
"""
from collections import defaultdict


def open_picture(profile_path):
    try:
        return open(profile_path, "a+b")
    except OSError:
        print(f"Failed to open path {profile_path}")
        raise


class Pictures(dict):
    def __missing__(self, key):
        value = open_picture(key)
        self[key] = value
        return value


# When pictures[path] dictionary access finds that the path key isn't present in the dictionary,
# the __missing__ method is called, creates the default value for the key, insert in
# the dictionary, return it to the caller.

if __name__ == "__main__":
    pictures = defaultdict(open_picture)
    path = "profile_1234.jpg"
    # handle = pictures[path]
    # handle.seek(0)
    # image_data = handle.read() # TypeError : open_picture() missing 1 required positional argument: 'profile_path'

    pictures = Pictures()
    handle = pictures[path]
    handle.seek(0)
    image_data = handle.read()
