def can_break(s1, s2):
    # If lengths differ, cannot break
    if len(s1) != len(s2):
        return False

    # Sort both strings
    a = sorted(s1)
    b = sorted(s2)

    # Check if s1 can break s2
    s1_breaks = True
    for i in range(len(a)):
        if a[i] < b[i]:
            s1_breaks = False
            break

    # Check if s2 can break s1
    s2_breaks = True
    for i in range(len(a)):
        if b[i] < a[i]:
            s2_breaks = False
            break

    return s1_breaks or s2_breaks


# ---- Driver code ----
s1 = input().strip()
s2 = input().strip()

print("true" if can_break(s1, s2) else "false")
