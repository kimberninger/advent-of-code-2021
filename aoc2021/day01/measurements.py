def count_larger_measurements(measurements: list[int], *, window_size: int = 1):
    """
    Count the number of summed measurements that are larger than the previous one.

    :param measurements: The depth measurements.
    :param window_size: The size of the window to compute the sum of measurements on.

    :return: The number of summed measurements that are larger than the previous one.
    """
    return sum(1 for a, b in zip(measurements[window_size:], measurements[:-window_size]) if a > b)
