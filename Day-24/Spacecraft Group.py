def spaceship_fleets(target, pos, speed):
    """
    Returns the number of distinct spaceship fleets that arrive at the destination.
    Parameters:
        target (int): Distance to the star system
        pos (list of int): Current positions of spaceships
        speed (list of int): Speeds of spaceships
    Returns:
        int: Number of fleets
    """
    # Sort ships by starting position descending
    ships = sorted(zip(pos, speed), key=lambda x: -x[0])
    
    fleets = 0
    last_time = 0  # time taken by the last fleet
    
    for p, s in ships:
        time = (target - p) / s
        if time > last_time:
            fleets += 1
            last_time = time
        # else: ship joins the fleet ahead
    
    return fleets


def main():
    import sys
    input = sys.stdin.read
    data = list(map(int, input().split()))
    
    n = data[0]             # Number of spaceships
    target = data[1]        # Distance to star system
    pos = data[2:n+2]       # Positions array
    speed = data[n+2:2*n+2] # Speeds array
    
    result = spaceship_fleets(target, pos, speed)
    print(result)


if __name__ == "__main__":
    main()
