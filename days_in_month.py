import numpy as np


def days_between_dates(next_month: str, cur_month: str):
    """
    The function receives two dates and returns the number of days between them.
    :param next_month: First month.
    :param cur_month: Second month
    :return: The number of days between them.
    """
    return np.datetime64(next_month) - np.datetime64(cur_month)


if __name__ == "__main__":
    print(f"Number of days, February, 2016:\n{days_between_dates('2016-03-01','2016-02-01')}\n"
          f"Number of days, February, 2017:\n{days_between_dates('2017-03-01','2017-02-01')}\n"
          f"Number of days, February, 2018:\n{days_between_dates('2018-03-01','2018-02-01')}")