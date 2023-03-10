# Monte Carlo Simulation

In this sub-challenge, you will write a Python program that uses a Monte Carlo simulation to estimate the value of pi. A Monte Carlo simulation is a method of using random numbers to solve problems. You will use NumPy to generate random numbers and perform basic statistical analysis to estimate the value of pi.

## TODOs

1. Import the NumPy library.
2. Define a variable $n$ and set it to 1000000.
3. Use the NumPy `random.rand` function to generate $n$ pairs of random numbers between 0 and 1, representing the x and y coordinates of points on a unit square.
4. Calculate the distance between each point and the origin using the Pythagorean theorem.
5. Determine how many points fall within a unit circle centered at the origin.
6. Estimate the value of pi by dividing the number of points that fall within the circle by the total number of points generated, and multiplying by 4.
7. Print the estimated value of pi.
8. Completing `estimate_pi.py`