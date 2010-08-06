VERSION = (0, 0, 4)

def get_version():
    """Returns the version as a human-format string."""
    v = '.'.join([str(i) for i in VERSION])
    return v
