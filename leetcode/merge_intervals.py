"""
    Task: Write a Python function called merge_intervals that takes a list of intervals as input and returns a new list of 
    intervals where overlapping intervals are merged.

    Input Format: The input will be a list of intervals, where each interval is represented by a list with two elements: 
    the start and end points of the interval. 
    
    Constraints

    The list of intervals will be non-empty.
    The start and end points of each interval will be integers.
    Output Format: The output will be a list of merged intervals, where each interval is represented by a list with two elements: the start and end points of the merged interval.

    Sample Input: [[1, 3], [2, 6], [8, 10], [15, 18]]

    Sample Output: [[1, 6], [8, 10], [15, 18]]

"""


def merge_intervals(intervals):

    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged
