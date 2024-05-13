import numpy as np
import pandas as pd
import numpy as np
from crepes import ConformalClassifier, ConformalPredictiveSystem
from crepes.extras import hinge, margin, binning, DifficultyEstimator

def softmax(logits):
    """
    Apply the softmax function to a list of numbers.

    Args:
        logits (list or np.array): A list of numbers.

    Returns:
        np.array: A numpy array representing the softmax probabilities of the input numbers.
    """
    exp_logits = np.exp(logits)
    sum_exp_logits = np.sum(exp_logits)
    softmax_probs = exp_logits / sum_exp_logits
    return softmax_probs

def softmax_df(df):
    """
    Apply the softmax function to each row of a DataFrame.

    Args:
        df (pd.DataFrame): A pandas DataFrame.

    Returns:
        pd.DataFrame: A DataFrame with the softmax probabilities of each row.
    """
    # Apply softmax function to each row of the DataFrame
    softmax_probs = df.apply(softmax, axis=1)
    return softmax_probs

def calculate_sigmoid(df, conf_score_cols, objectness_score_col, sigmoid_cols):
    """
    Calculate sigmoid values by dividing conf_score by objectness_score.
    """
    df[sigmoid_cols] = df[conf_score_cols] / df[objectness_score_col].values[:, None]
    return df

def calculate_logit(df, sigmoid_cols, logit_cols):
    """
    Calculate logit values from sigmoid values.
    """
    df[logit_cols] = np.log(df[sigmoid_cols].astype(float) / (1 - df[sigmoid_cols].astype(float)))
    return df

def calculate_softmax(df, logit_cols, softmax_cols, softmax_func):
    """
    Calculate softmax values from logit values.
    """
    df[softmax_cols] = np.round(softmax_func(df[logit_cols]), 7)
    return df

def calculate_hinge_scores(df, softmax_cols, hinge_score_cols):
    """
    Calculate hinge scores for a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to calculate hinge scores for.
        softmax_cols (list): The names of the softmax columns in df.
        hinge_score_cols (list): The names of the hinge score columns to add to df.

    Returns:
        pd.DataFrame: The DataFrame with added hinge score columns.
    """
    df[hinge_score_cols] = hinge(df[softmax_cols])
    return df

def calculate_p_values(df, hinge_score_cols, p_value_cols, cc_std):
    """
    Calculate p-values for a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to calculate p-values for.
        hinge_score_cols (list): The names of the hinge score columns in df.
        p_value_cols (list): The names of the p-value columns to add to df.
        cc_std (object): The conformal prediction object to use for predictions.

    Returns:
        pd.DataFrame: The DataFrame with added p-value columns.
    """
    df[p_value_cols] = cc_std.predict_p(df[hinge_score_cols].values)
    return df

def calculate_prediction_sets(df, hinge_score_cols, p_set_cols, cc_std, confidence=0.991):
    """
    Calculate prediction sets for a DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to calculate prediction sets for.
        hinge_score_cols (list): The names of the hinge score columns in df.
        p_set_cols (list): The names of the prediction set columns to add to df.
        cc_std (object): The conformal prediction object to use for predictions.
        confidence (float): The confidence level to use for prediction sets.

    Returns:
        pd.DataFrame: The DataFrame with added prediction set columns.
    """
    df[p_set_cols] = cc_std.predict_set(df[hinge_score_cols].values, confidence=confidence)
    return df

