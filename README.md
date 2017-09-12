# Gradient Descent Implementation in Python

We have seen in the lectures how Gradient Descent helps us minimize the cost function. In this exercise we will stepwise write to functions to implement our own batch gradient descent algorithm for univariate linear regression.

You may want to revise and refer to the DG algorithm from the slides.

You cannot use any sklearn objects for the purpose of this exercise.

## Task: Write your own Gradient Descent Algorithm

## 1. Write `error_calculator()` funtion:

- Wrtie a function that given b, theta, x and y, calculates squared error, where

  *y = theta * x + b*

- Accepts:
    - b (int/float) intercept
    - theta (int/float) coefficient
    - points (list `m x 2` format. First column contains x values and second column contains y values)
- Returns
    - MSE for given b, theta and points

## 2. Write `gradient()` funtion:

- Wrtie a function that given current b, current theta, x, y and learing rate, calculates the gradient and returns new b and theta

- Accepts:
    - current_b (int/float) current intercept
    - current_theta (int/float) current coefficient
    - points (list `m x 2` format. First column contains x values and second column contains y values)
    - learning_rate (float)
- Returns
    - new b
    - new theta

## 3. Write `gradient_descent()` funtion:

- Wrtie a function that given current b, current theta, x, y, learing rate, num_iterations performs gradient descent and returns lists of calculated b, theta and errors

- Accepts:
    - starting_b (int/float) initial intercept
    - starting_theta (int/float) initial coefficient
    - points (list `m x 2` format. First column contains x values and second column contains y values)
    - learning_rate (float)
    - num_iterations (int) number of iterations to perform gradient descent
- Returns
    - list of b
    - list of theta
    - list of erros for each stage

Note: you can use previously defined functions in this function

## 4. Write `plot_theta()` funtion:

- Wrtie a function that given current b, current theta, x, y, learing rate and num_iterations plots values of theta against iteration number

- Accepts:
    - starting_b (int/float) initial intercept
    - starting_theta (int/float) initial coefficient
    - points (list `m x 2` format. First column contains x values and second column contains y values)
    - learning_rate (float)
    - num_iterations (int) number of iterations to perform gradient descent
- Returns
    - plots a graph with
        - title "Theta"
        - x label "iterations"
        - y label "theta"

Note: you can use previously defined functions in this function

## 5. Write `plot_b()` funtion:

- Wrtie a function that given current b, current theta, x, y, learing rate and num_iterations plots values of b against iteration number

- Accepts:
    - starting_b (int/float) initial intercept
    - starting_theta (int/float) initial coefficient
    - points (list `m x 2` format. First column contains x values and second column contains y values)
    - learning_rate (float)
    - num_iterations (int) number of iterations to perform gradient descent
- Returns
    - plots a graph with
        - title "b"
        - x label "iterations"
        - y label "constant term"

Note: you can use previously defined functions in this function

## 6. Write `plot_errors()` funtion:

- Wrtie a function that given current b, current theta, x, y, learing rate and num_iterations plots values of errors against iteration number

- Accepts:
    - starting_b (int/float) initial intercept
    - starting_theta (int/float) initial coefficient
    - points (list `m x 2` format. First column contains x values and second column contains y values)
    - learning_rate (float)
    - num_iterations (int) number of iterations to perform gradient descent
- Returns
    - plots a graph with
        - title "Error"
        - x label "iterations"
        - y label "Error"

Note: you can use previously defined functions in this function