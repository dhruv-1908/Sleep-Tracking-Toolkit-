# Sleep-Tracking-Toolkit-

1) record.py
Implement a class DailySleepRecord with the following:

Attributes:
date: string, e.g., '2025-04-29'
segments: list of tuples, each of the form (duration, quality_score) where:
duration is in hours (float)
quality_score is from 0 - 100 (int or float)
Methods:
average_quality(): returns the average of all quality scores, rounded to two decimal places
total_duration(): returns the sum of all sleep durations, rounded to two decimal places
is_restful(duration_threshold, quality_threshold): returns True if all segments of the day meet both duration and quality thresholds. Set default values of 7 and 75 for the thresholds respectively
average_sleep_score(): returns the average computed sleep score (using compute_sleep_score() in utils), rounded to two decimal places
summary(): returns a dictionary with keys 'date', 'avg_quality', 'total_duration', 'avg_sleep_score', and 'quality_label'
2) utils.py
Implement the following functions:

quality_label(score): converts a numeric score to a string label based on the following:
85 or more → 'Excellent'
70 to 84 → 'Good'
50 to 69 → 'Fair'
below 50 → 'Poor'
normalize_quality(score, current_max=100): normalizes a given score to a 0 - 100 scale using the formula:
score / current_max * 100, rounded to two decimal places
compute_sleep_score(duration, quality_score): computes a combined sleep score (0 - 100 scale) using the formula:
score = min(duration / 8.0, 1.0) * 60 + quality_score * 0.4, capped at 100, rounded to two decimal places
3) analytics.py
Implement the following functions:

overall_average_duration(records): Given a list of records, it returns the overall average sleep duration across all records. It should calculate one combined average from all readings.
best_sleep_day(records): Given a list of records, it returns the date of the record with the highest average sleep score
detect_under_sleep_days(records, threshold): returns a list of dates where any segment has duration below the threshold. It should include a date if at least one reading is below the threshold.
detect_spike(durations, *, threshold=2): This function checks whether the durations contain a sharp jump or drop between any two consecutive values. It returns True if any two consecutive durations differ by the given threshold or more. The threshold value should be passed by name and have a default.
duration_trend(durations): returns a list of 'up', 'down', or 'same' describing how the sleep duration changes in the list of durations. The function should compare each duration in the list with the one before it.
average_sleep_score_across_days(records): returns the average of all segment-level sleep scores (using the proper function already implemented) across all records
