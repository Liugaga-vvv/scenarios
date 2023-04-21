def outer_function() -> None:
    """
    Define a function that contains a nested function with local and global variables.

    :return: None
    """
    global_var = 10

    def inner_function() -> None:
        """
        Define a nested function with a local variable and a reference to a global variable.

        :return: None
        """
        local_var = 5
        nonlocal global_var
        global_var += local_var

    inner_function()
    print(global_var)
