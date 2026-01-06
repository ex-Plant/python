# Complete the configure_plugin_decorator function. It decorates a func that takes keyword arguments **kwargs, but the wrapper function it returns takes positional arguments *args. The arguments passed to the wrapper will be a series of tuples, each a key/value pair.

# Create a wrapper function that takes positional arguments *args:
# Within the wrapper function, convert the args into a dictionary with the dict function.
# Return the result of passing this dictionary into func as keyword arguments using the ** operator to unpack the dict.
# Return the wrapper function.
# plugin_config = configure_backups(("path", "~/duplicates"), ("prefix", "duplicate_"), ("extension", ".rtf"))

# # plugin_config:
# # {
# #   "path": "~/duplicates",
# #   "prefix": "duplicate_",
# #   "extension": ".rtf",
# # }


def configure_plugin_decorator(func):
    def wrapper(*args):
        print(args)
        dictionary = dict(args)
        return func(**dictionary)
    return wrapper

@configure_plugin_decorator
def configure_backups(path="~/backups", prefix="copy_", extension=".txt"):
    return {
        "path": path,
        "prefix": prefix,
        "extension": extension,
    }

@configure_plugin_decorator
def configure_login(user=None, password=None, token=None):
    return {
        "user": user,
        "password": password,
        "token": token,
    }

        

