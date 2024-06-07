import numpy as np
from scipy.stats import f

def anova_test(groups: list, values: list, alpha=0.05) -> float:
    """Perform an ANOVA test for the values and the groups passed as 
    two list-like objects. If alpha is None, returns the p-value of the
    test, if alpha is a float (float) returns True if there is a significative
    result (with a significant level alpha).

    Params:
    ===========================
    groups: list-alike. 
    The group at which belongs every value.

    values: list-alike.
    All the observations for each subject.

    Returns:
    ===========================
    p-value: float
    If alpha is None, returns the p-value of the test.

    result: bool
    Result of the test (Whether there is a significative result).
    """
    
    N: int = len(values)
    k: int = len(set(groups))

    # Split the observations (values) for each group.
    grouped_data: dict = {}
    for group, value in zip(groups, values):
        if not group in grouped_data:
            grouped_data[group] = [value]
        else:
            grouped_data[group].append(value)

    # SS: Sum of Squares
    grand_mean = np.mean(values)
    SS_total = np.sum((values - grand_mean)**2)
    SS_between = 0
    SS_within = 0
    for group, values in grouped_data.items():
        SS_between += len(values) * (np.mean(values) - grand_mean)**2
        SS_within += np.sum([(xi - np.mean(values))**2 for xi in values])

    # DF: Degrees of Freedom
    df_total = N - 1
    df_between = k - 1
    df_within = N - k

    # Mean Squares
    MS_between = SS_between / df_between
    MS_within = SS_within / df_within

    # F ratio
    F = MS_between / MS_within
    p_val = f.sf(F, df_between, df_within)

    if alpha is None:
        return p_val
    else:
        return p_val < alpha