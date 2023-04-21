# Modifying Enclosing Scope Variables with Non-Local

## Requirements

In this step, you will create a function that contains another function within it. The nested function will have its own local variable, and it will also reference a global variable from the outer function. In addition, the function modifies a variable in its enclosing scope. This will require the use of the `nonlocal` keyword, which allows a function to modify a variable in an outer, but non-global scope. Here are the steps:

1. Create a function called `outer_function` that takes no arguments.
2. Inside the `outer_function`, define a global variable called `global_var` and set its value to `10`.
3. Define a nested function called `inner_function` inside the `outer_function`.
4. Inside `inner_function`, define a local variable called `local_var` and set its value to `5`.
5. Also inside `inner_function`, reference the `global_var` variable defined in the outer function, and add `local_var` to it.
6. Finally, call the `inner_function` from the `outer_function`.
