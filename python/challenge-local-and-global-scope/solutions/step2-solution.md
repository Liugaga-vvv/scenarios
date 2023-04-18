# step2-solution

The `nonlocal` keyword is used to indicate that a variable should be treated as a variable in an outer (but non-global) scope. In this case, `global_var` is defined in the outer function, and is therefore not a local variable. By using the `nonlocal` keyword, the `inner_function` can access and modify the `global_var` variable.
