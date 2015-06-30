def diri(obj, s="", internals=False):
    """
    Is like dir() function, but allows you to filter for values containing some
    text.

    If only the first argument is provided, then it behaves pretty much the same
    way that dir() behaves, only it prints every item in a new line, and hides
    internal values.

    :param obj: (object)
    :param s: (string)
    :param internals: (boolean) should it show internal methods and values?
                      ie, values begining with "_" or "__"?

                      (DEFAULT is False)
    """
    for item in dir(obj):
        if (item.startswith("_") and not internals):
            continue
        if s in item:
            print(item)


def ronnys():
    """
    prints a summary of all the functions available in this package
    """
    print("===================================================================")
    print("                          RONNYS FUNCTIONS")
    print("===================================================================")
    print("diri()       like dir but with filtering for items containing some ")
    print("             text. Also allows you to filter internal values.")
    print("             USAGE: diri(a, 'get')")
    print("                    diri(a, 'get', internals=True)")
    print("-------------------------------------------------------------------")
    print("")
    print("===================================================================")
