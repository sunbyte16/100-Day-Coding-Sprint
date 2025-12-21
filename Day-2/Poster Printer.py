def can_print(s):
    # Split by W (white sheets)
    segments = s.split('W')

    for seg in segments:
        if not seg:
            continue
        # If segment has only one color, impossible
        if 'R' not in seg or 'B' not in seg:
            return "NO"
    return "YES"


# -------- Main --------
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(can_print(s))
