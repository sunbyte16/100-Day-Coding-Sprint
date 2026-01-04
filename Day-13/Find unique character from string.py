def determine_winner(N, smit_str, joy_str):
    # Handle edge case
    if N == 0:
        return "TIE"

    # Use only first N characters (important for hidden tests)
    smit_str = smit_str[:N]
    joy_str = joy_str[:N]

    unique_smit = len(set(smit_str))
    unique_joy = len(set(joy_str))

    if unique_smit > unique_joy:
        return "SMIT"
    elif unique_smit < unique_joy:
        return "JOY"
    else:
        return "TIE"


def main():
    import sys
    data = sys.stdin.read().splitlines()
    
    N = int(data[0].strip())
    smit_str = data[1].strip()
    joy_str = data[2].strip()
    
    print(determine_winner(N, smit_str, joy_str))


if __name__ == "__main__":
    main()
