def user_logic(fat, protein, vitamin):
    # Convert protein and vitamin arrays to sets for O(1) lookup
    protein_set = set(protein)
    vitamin_set = set(vitamin)
    
    fat_count = sum(1 for x in fat if x not in protein_set and x not in vitamin_set)
    
    fat_set = set(fat)
    vitamin_set2 = set(vitamin)  # separate set for protein calculation
    protein_count = sum(1 for x in protein if x not in fat_set and x not in vitamin_set2)
    
    fat_set2 = set(fat)
    protein_set2 = set(protein)
    vitamin_count = sum(1 for x in vitamin if x not in fat_set2 and x not in protein_set2)
    
    return (fat_count, protein_count, vitamin_count)


def main():
    import sys
    data = sys.stdin.read().strip().split()
    
    n = int(data[0])
    fat = list(map(int, data[1:n+1]))
    protein = list(map(int, data[n+1:2*n+1]))
    vitamin = list(map(int, data[2*n+1:3*n+1]))
    
    result = user_logic(fat, protein, vitamin)
    print(result[0], result[1], result[2])


if __name__ == "__main__":
    main()
