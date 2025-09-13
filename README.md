# Sleep-Tracking-Toolkit-
Here’s a clean **README.md** style draft for your `sleep_tracking_toolkit` package based on the requirements you listed:

---

# 💤 Sleep Tracking Toolkit

A Python package for recording, analyzing, and evaluating daily sleep data. This toolkit provides utilities for handling sleep records, computing scores, detecting trends, and generating summaries.

---

## 📂 Project Structure

```
sleep_tracking_toolkit/
│── record.py     # Class for managing daily sleep records
│── utils.py      # Helper functions for quality scoring & normalization
│── analytics.py  # Functions for analysis across multiple days
│── README.md     # Project documentation
```

---

## 📌 Modules Overview

### 1. `record.py`

#### Class: `DailySleepRecord`

**Attributes:**

* `date` *(str)* → Example: `'2025-04-29'`
* `segments` *(list of tuples)* → Each tuple `(duration, quality_score)`

  * `duration`: float (hours)
  * `quality_score`: int/float (0–100)

**Methods:**

* `average_quality()` → Returns average quality score (rounded to 2 decimals).
* `total_duration()` → Returns total sleep duration in hours (rounded to 2 decimals).
* `is_restful(duration_threshold=7, quality_threshold=75)` → Returns `True` if **all segments** meet both thresholds.
* `average_sleep_score()` → Returns average sleep score (using `compute_sleep_score()` from `utils`).
* `summary()` → Returns a dictionary with:

  ```python
  {
      "date": <date>,
      "avg_quality": <float>,
      "total_duration": <float>,
      "avg_sleep_score": <float>,
      "quality_label": <str>
  }
  ```

---

### 2. `utils.py`

#### Functions:

* `quality_label(score)` → Converts numeric score to label:

  * 85+ → `"Excellent"`
  * 70–84 → `"Good"`
  * 50–69 → `"Fair"`
  * <50 → `"Poor"`

* `normalize_quality(score, current_max=100)` → Normalizes score to 0–100 scale:

  ```
  (score / current_max) * 100
  ```

  Rounded to 2 decimals.

* `compute_sleep_score(duration, quality_score)` → Computes combined sleep score:

  ```
  score = min(duration / 8.0, 1.0) * 60 + quality_score * 0.4
  ```

  * Capped at 100
  * Rounded to 2 decimals

---

### 3. `analytics.py`

#### Functions:

* `overall_average_duration(records)` → Returns overall average sleep duration across all records.
* `best_sleep_day(records)` → Returns the **date** with the highest average sleep score.
* `detect_under_sleep_days(records, threshold)` → Returns list of **dates** where any segment duration is below `threshold`.
* `detect_spike(durations, *, threshold=2)` → Returns `True` if any **consecutive durations** differ by ≥ `threshold`.
* `duration_trend(durations)` → Returns list of `["up", "down", "same"]` describing duration changes.
* `average_sleep_score_across_days(records)` → Returns average of **all segment-level sleep scores** across all records.

---

## ✅ Example Usage

```python
from record import DailySleepRecord
from analytics import best_sleep_day, overall_average_duration
from utils import quality_label

# Create a daily record
record = DailySleepRecord(
    date="2025-04-29",
    segments=[(3.5, 70), (4.0, 80)]
)

print(record.summary())
# {
#   'date': '2025-04-29',
#   'avg_quality': 75.0,
#   'total_duration': 7.5,
#   'avg_sleep_score': 78.25,
#   'quality_label': 'Good'
# }
```

---

## 🚀 Features

* Track and summarize daily sleep data
* Normalize and score sleep quality
* Detect under-sleep and duration spikes
* Trend analysis across multiple days

---

