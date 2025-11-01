"""
Gradient Descent Basics

Finding the minimum of f(x) = (x - 3)² using gradient descent.

Questions to answer:
1. What is the derivative of f(x) = (x - 3)²?
2. How do you use that derivative to know which direction is "downhill"?
3. How do you update x iteratively to reach the minimum?
"""
def f(x):
    return (x-3) ** 2

def derivative(x):
    return (2*x) - 6

def gradient_descent(starting_x, learning_rate, iterations):
    x = starting_x
    for i in range(iterations):
        grad = derivative(x)
        print(f"Iteration {i}: x = {x}, grad = {grad}")
        x = x-(learning_rate * grad)
        if abs(grad) < 0.001:
            break
    return x


if __name__ == "__main__":
    result = gradient_descent(0,0.1,100)
    print(f"\nFinal x: {result}")
    print(f"f({result}) = {f(result)}")