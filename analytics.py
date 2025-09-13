from utils import compute_sleep_score

def overall_average_duration(records):
    all_durations = [d for rec in records for d, _ in rec.segments]
    return round(sum(all_durations) / len(all_durations), 2) if all_durations else 0

def best_sleep_day(records):
    if not records:
        return None
    best = max(records, key=lambda rec: rec.average_sleep_score())
    return best.date

def detect_under_sleep_days(records, threshold=6):
    return [rec.date for rec in records if any(d < threshold for d, _ in rec.segments)]

def detect_spike(durations, *, threshold=2):
    return any(abs(durations[i] - durations[i - 1]) >= threshold for i in range(1, len(durations)))

def duration_trend(durations):
    if len(durations) < 2:
        return []
    return [
        'up' if durations[i] > durations[i - 1]
        else 'down' if durations[i] < durations[i - 1]
        else 'same'
        for i in range(1, len(durations))
    ]

def average_sleep_score_across_days(records):
    all_scores = [
        compute_sleep_score(d, q)
        for rec in records for d, q in rec.segments
    ]
    return round(sum(all_scores) / len(all_scores), 2) if all_scores else 0
