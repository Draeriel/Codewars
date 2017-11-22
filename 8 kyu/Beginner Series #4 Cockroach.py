def cockroach_speed(s):
    if s > 0:
        return int((s * 100000 / 60) / 60)
    if s == 0:
        return 0