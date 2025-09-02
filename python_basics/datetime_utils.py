"""
datetime_utils.py
Helpers for timestamps, parsing, and human-readable durations.
"""

from datetime import datetime, timedelta, timezone

ISO_FMT = "%Y-%m-%dT%H:%M:%S%z"

def now_utc():
    return datetime.now(timezone.utc)

def iso_timestamp(dt=None):
    dt = dt or now_utc()
    return dt.strftime(ISO_FMT)

def parse_iso(ts):
    # Accept 'Z' suffix too
    if ts.endswith("Z"):
        ts = ts.replace("Z", "+0000")
    return datetime.strptime(ts, ISO_FMT)

def human_duration(seconds):
    seconds = int(seconds)
    mins, sec = divmod(seconds, 60)
    hrs, mins = divmod(mins, 60)
    days, hrs = divmod(hrs, 24)
    parts = []
    if days: parts.append(f"{days}d")
    if hrs: parts.append(f"{hrs}h")
    if mins: parts.append(f"{mins}m")
    if sec or not parts: parts.append(f"{sec}s")
    return " ".join(parts)

def add_days(dt, days):
    return dt + timedelta(days=days)

if __name__ == "__main__":
    now = now_utc()
    print("UTC now:", now)
    iso = iso_timestamp(now)
    print("ISO:", iso)
    parsed = parse_iso(iso)
    print("Parsed equals now (to second):", parsed.replace(microsecond=0) == now.replace(microsecond=0))
    print("Human 93784s:", human_duration(93784))
    print("Three days later:", add_days(now, 3))
