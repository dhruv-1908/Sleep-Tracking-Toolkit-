from utils import compute_sleep_score, quality_label

class DailySleepRecord:
    def __init__(self, date, segments):
        self.date = date
        self.segments = segments

    def average_quality(self):
        if not self.segments:
            return 0
        return round(sum(q for _, q in self.segments) / len(self.segments), 2)

    def total_duration(self):
        return round(sum(d for d, _ in self.segments), 2)

    def is_restful(self, duration_threshold=7, quality_threshold=75):
        return all(d >= duration_threshold and q >= quality_threshold for d, q in self.segments)

    def average_sleep_score(self):
        if not self.segments:
            return 0
        scores = [compute_sleep_score(d, q) for d, q in self.segments]
        return round(sum(scores) / len(scores), 2)

    def summary(self):
        avg_quality = self.average_quality()
        total_duration = self.total_duration()
        avg_sleep_score = self.average_sleep_score()
        return {
            'date': self.date,
            'avg_quality': avg_quality,
            'total_duration': total_duration,
            'avg_sleep_score': avg_sleep_score,
            'quality_label': quality_label(avg_sleep_score)
        }
