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

Conformal Prediction (CP) is a sophisticated framework within the realm of machine learning, designed to quantify uncertainty in predictions. This framework is particularly notable for its ability to generate statistically valid prediction regions, also known as prediction intervals, which are applicable across a wide array of models, whether they are based on traditional statistical methods or more complex deep learning algorithms.

CP operates by calculating nonconformity scores from previously labeled data. These scores assess how much a new, unlabeled piece of test data differs from the labeled examples. CP uses these scores to construct prediction sets for the new data, effectively estimating the range of possible labels it could be assigned. A crucial component of CP is the requirement for a user-defined significance level. This level sets a limit on the algorithm's error rate, dictating the maximum frequency of errors permitted. For instance, a significance level (SL) of 0.1 means that the algorithm is allowed to make erroneous predictions up to 10% of the time. This mechanism ensures that CP's predictions are statistically reliable to a degree specified by the user, striking a balance between accuracy and confidence.

CP is designed to compute and output a p-value for each available class by performing a ranking based on the non-conformity measure (α-value) of a test object in comparison to examples from the training dataset. This process involves assessing how well the test object conforms to the patterns observed in the training data for each class, thereby providing a statistical basis for decision-making regarding the most likely class or classes the test object belongs to.

Conformal prediction utilizes a concept akin to standard hypothesis testing, where the p-value, in conjunction with a predefined significance level threshold (sl), plays a crucial role in decision-making. Specifically, this approach determines whether a particular label should be included in the prediction set. The p-value, derived from the conformity measure, assesses the compatibility of a new instance with the existing data under each possible label. If the p-value exceeds the threshold (sl), it indicates a sufficient level of conformity, suggesting that the label under consideration is a plausible prediction for the new instance.