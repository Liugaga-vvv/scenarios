def update_global_variable() -> None:
    """
    This function updates the value of a global variable.
    """
    # write your code here
    global_var = None
    print("Global variable inside function:", global_var)


def update_local_variable() -> None:
    """
    This function updates the value of a local variable.
    """
    # write your code here
    local_var = None
    print("Local variable inside function:", local_var)


global_var = 0
local_var = 0

update_global_variable()
update_local_variable()

print("Global variable outside function:", global_var)
print("Local variable outside function:", local_var)
