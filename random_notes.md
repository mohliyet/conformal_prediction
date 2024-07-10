# Random Notes
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

# Conformal Prediction (CP) Overview

## What is Conformal Prediction?

Conformal Prediction (CP) is a machine learning framework designed to quantify uncertainty in predictions, offering a method to generate statistically valid prediction intervals for a wide range of models, from traditional statistical methods to complex deep learning algorithms. CP calculates nonconformity scores using previously labeled data to assess how much a new, unlabeled test data point deviates from labeled examples. These scores are then used to construct prediction sets, estimating the range of possible labels for the new data.

A key aspect of CP is the use of a user-defined significance level (SL), which controls the algorithm's error rate. For example, an SL of 0.1 permits erroneous predictions up to 10% of the time, balancing accuracy with confidence. This ensures that CP's predictions are statistically reliable within the user-specified confidence level.

CP computes a p-value for each class by ranking the test object against the training dataset based on the non-conformity measure (α-value). This process evaluates how well the test object aligns with the patterns observed in the training data for each class, providing a statistical basis for decision-making. The p-value, in conjunction with the SL, determines whether a label should be included in the prediction set. If the p-value meets or exceeds the SL threshold, it indicates a sufficient level of conformity, making the label a plausible prediction for the new instance.

This framework allows for a dynamic adjustment of the prediction set's size based on statistical confidence, ensuring that only the most plausible classes are considered in the final prediction. By integrating CP, developers and researchers can enhance the robustness and reliability of their predictive systems, facilitating more informed decision-making across various domains.