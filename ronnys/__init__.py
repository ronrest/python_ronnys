
# ==============================================================================
#                                                                           DIRI
# ==============================================================================
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
    # ==========================================================================
    for item in dir(obj):
        if (item.startswith("_") and not internals):
            continue
        if s in item:
            print(item)


# ==============================================================================
#                                                                         RONNYS
# ==============================================================================
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
    print("printl()     Prints items in a list, one line at a time.")
    print("             Also allows you to filter for values containing some")
    print("             specific text/value")
    print("             USAGE: printl(a, "r")  # filters items containing r   ")
    print("                    printl(a, 3)    # filters valus contianing a 3 ")
    print("                    printl(a, 3, n=3) # returns the first 3 results")
    print("-------------------------------------------------------------------")
    print("var_vals()   Takes a list of strings representing variable names.")
    print("             Prints out key value pairs of the name of each variable")
    print("             and the value it has.")
    print("             USAGE: var_list = ['var1', 'var2', 'var3']")
    print("                    var_val(var_list)")
    print("===================================================================")


# ==============================================================================
#                                                                         PRINTL
# ==============================================================================
def printl(l, filter="", n=None):
    """
    Prints the items of some list one line at a time.

    Allows you to filter for items that contains some text/value in them.
    :param l:
    :param filter:
    :param n: only return the first n items (satisfying the filtered conditions)
    :examples:

        # filters items containing r
        printl(a, "r")

        # filters for items containing a 3
        printl(a, 3)

        # returns the first 3 results of items containing a 3
        printl(a, 3, n=3)
    """
    # ==========================================================================
    count = 1
    if n is None:
        n = float("inf")

    for item in l:
        if str(filter) in str(item):
            print(item)

            # Check how many items have been printed
            if count >= n:
                break
            else:
                count += 1


import inspect  # required for var_vals

# ==============================================================================
#                                                                       VAR VALS
# ==============================================================================
def var_vals(names, print_it=True, glob=False, depth=1):
    """
    Takes a list of strings representing variable names. Returns the vales for
    each of those variables.

    By default, it prints out in the console a key value pair of each variable,
    and the value that it has, one per line. To disable this use:
    print_it=False  which will return the values in a list instead.

    You can specify that you want to search global namespace instead of local
    namespace by setting glob=True.

    :param names: (list of strings) list of variable names.
    :param print_it: (boolean) Should it print a key value pair in the console
                    instead of returning the actual value?

                     (DEFAULT is False)
    :param glob: (boolean) use global namespace?

                    - False - Searches in local namespace of where this function
                              is called from.

                    (DEFAULT is False)
    :param depth: (boolean) Only to be used to write a wrapper function around
                   this function, so it knows how many function call stacks to
                   follow to get the desired frame.

                   (DEFAULT is 1)
    :return: the value of the variable you named (But only if you specified
             print_it=False, otherwise it prints to the console instead).

    :usage:
        a = 443
        b = 543
        c = 734
        d = 967
        vars = ["a", "b", "c", "d"]

        var_vals(vars)
    """
    # ==========================================================================
    vals = []
    if isinstance(names, str):
        names = [names]
    for name in names:
        #print "{name}  = {val}".format(name=name, val=globals()[name])
        vals.append(var_val(name, glob=glob, print_it=print_it, depth=1+depth))

    # Only return values as a list if printing is disabled
    if not print_it:
        return vals


# ==============================================================================
#                                                                        VAR_VAL
# ==============================================================================
def var_val(name, print_it=True, glob=False, depth=1):
    """
    Get the value of a variable based on its name.

    :param name: (str) Variable name as a string
    :param print_it: (boolean) Should it print a key value pair in the console
                    instead of returning the actual value?

                     (DEFAULT is False)
    :param glob: (boolean) use global namespace?

                    (DEFAULT is False)
    :param depth: (boolean) Only to be used to write a wrapper function around
                   this function, so it knows how many function call stacks to
                   follow to get the desired frame.

                   (DEFAULT is 1)
    :return: the value of the variable you named (But only if you specified
             print_it=False, otherwise it prints to the console instead).
    """
    # ==========================================================================
    import inspect
    assert isinstance(name, str), \
        "argument *name* in var_val() function MUST be a string, not a \n"\
        "'{}' object".format(str(type(name)))
    assert (depth >=1), \
        "argument *depth* in var_val() function MUST be must be at least 1"
    assert isinstance(depth, int), \
        "argument *depth* in var_val() function MUST be must be an integer"

    # Go up the function call stack
    frame = inspect.currentframe()
    for i in range(depth):
        frame = frame.f_back
    try:
        if glob:
            val = frame.f_globals[name]
        else:
            val = frame.f_locals[name]

        if print_it:
            print(name + "  =  " + str(val))
        else:
            return val
    except KeyError:
        if glob:scope = "GLOBAL"
        else: scope = "LOCAL"

        val = "THIS VARIABLE DOES NOT EXIST IN THE {} SCOPE".format(scope)
        print(name + "  =  " + str(val))
        return None
