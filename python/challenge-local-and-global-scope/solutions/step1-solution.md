# step1-solution

In this step, the function `update_global_variable()` updates the value of a global variable `global_var` by using the `global` keyword to declare that it is referring to the global variable.

On the other hand, the function `update_local_variable()` defines a local variable `local_var` that can only be accessed within the function.

When both functions are called and the values of the variables are printed outside of the functions, the value of `global_var` has been changed to `10` inside the `update_global_variable()` function and then printed as `10` outside of it. However, the value of `local_var` defined inside the `update_local_variable()` function is not accessible outside of the function and so the value printed outside of the function is `0`.
