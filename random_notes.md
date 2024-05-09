## Python Code Snippets

### Module

A Python file called `math_operations.py` with functions defined in it.

    # math_operations.py
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

You can import and use this module as follows:

    import math_operations
    result = math_operations.add(5, 3)
    print(result)  # Outputs: 8

### Package

A directory with an `__init__.py` file and multiple module files.

    my_package/__init__.py
        math_operations.py
        string_operations.py

You can import and use this package as follows:

    from my_package import math_operations
    result = math_operations.add(5, 3)
    print(result)  # Outputs: 8

### Library

Using a library involves importing it and using its functions. Here's an example with the `math` library.

    import math
    print(math.sqrt(16))  # Outputs: 4.0

### Framework

Django is a popular Python web framework. Here's a very basic example of a Django view.

    from django.http import HttpResponse
    def hello(request):
        return HttpResponse("Hello, World!")

This `hello` function is a very simple view that returns an HTTP response with the text "Hello, World!". In a full Django application, you'd have many such views, and you'd use the Django framework to route incoming HTTP requests to the appropriate views.
