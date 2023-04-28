def update_global_variable() -> None:
    """
    This function updates the value of a global variable.
    """
    global global_var
    global_var = 10
    print("Global variable inside function:", global_var)


def update_local_variable() -> None:
    """
    This function updates the value of a local variable.
    """
    local_var = 5
    print("Local variable inside function:", local_var)


global_var = 0
local_var = 0

update_global_variable()
update_local_variable()

print("Global variable outside function:", global_var)
print("Local variable outside function:", local_var)
