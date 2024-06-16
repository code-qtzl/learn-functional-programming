# learn-functional-programming

### first-class-and-higher-order-functions

-   **First-class function:** A function that is treated like any other value
-   **Higher-order function:** A function that accepts another function as an argument or returns a function

#### First-class function Example:

```
def square(x):
return x \* x

# Assign function to a variable
f = square

print(f(5))
# 25
```

#### Higher-order function Example:

```
def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)
# [1, 4, 9, 16, 25]
```
