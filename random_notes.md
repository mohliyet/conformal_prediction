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

Inductive Conformal Prediction (ICP) stands out for its efficiency, especially with models that are resource-intensive to train, like Convolutional Neural Networks (CNNs). A key advantage of ICP is that it eliminates the need to retrain the underlying model for each new test set example. This feature is particularly beneficial for applications involving heavy models, where retraining for every new instance would be impractical or too costly in terms of computational resources.

Mondrian Inductive Conformal Prediction (ICP) introduces a nuanced approach to the calculation of non-conformity measures, or α-values, by making them class-dependent. This method, referred to as "Mondrian," diverges from the traditional ICP framework that was initially introduced in an online setting in 2005. By tailoring α-values to each specific class, Mondrian ICP allows for a more refined assessment of how well a new instance conforms to the observed patterns within the training data for each class. This adaptation not only enhances the precision of the prediction sets generated by CP but also broadens the applicability of the model by moving away from the strict online setting of its inception. This flexibility makes Mondrian ICP particularly valuable in complex scenarios where the relevance and characteristics of the data can significantly vary across different classes.

The Conformal Prediction (CP) algorithm is a robust framework designed to enhance the reliability of predictions made by machine learning models. It operates in two main phases: training and prediction.

### Training Phase
1. **Model Training:** Begin by training a machine learning model (MLM) on your dataset. This model is the foundation upon which CP builds its predictive capabilities.
2. **Calibration:** Once the MLM is trained, run a separate calibration set through it. This step is crucial as it involves saving the output from a chosen stage of the model, which is later used to assess new data points.
3. **Non-conformity Measurement:** Utilize a non-conformity function to compute an α-value for each data point in the calibration set. The α-value is a measure of how much a data point deviates from the norm established by the training data, calculated for its true class.

### Prediction Phase
1. **α-value Generation for Test Data:** For each new test data point, generate a new α-value using the same non-conformity function. This α-value reflects the test data point's deviation from the calibration set.
2. **P-value Calculation:** Calculate a p-value for each class for the test data point. The p-value represents the probability that the test data point belongs to a particular class, based on its α-value.
3. **Class Inclusion:** Determine the classes to include in the output based on the p-value. If the p-value for a class is greater than the significance level (a threshold set by the user), that class is considered a plausible label for the test data point and included in the prediction set.

This methodical approach allows CP to provide statistically significant predictions, offering a clear measure of confidence in the results. By incorporating both α-values and p-values, CP effectively quantifies the uncertainty of each prediction, making it a powerful tool for decision-making processes where accuracy and reliability are paramount.