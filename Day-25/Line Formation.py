class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def minChanges(head, n):
    # Step 1: Extract linked list values into a list
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    # Step 2: Sort the list to get the desired order
    sorted_values = sorted(values)
    
    # Step 3: Count positions where the value differs
    changes = 0
    for original, sorted_val in zip(values, sorted_values):
        if original != sorted_val:
            changes += 1
    
    return changes

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    values = list(map(int, data[1:]))  # Remaining input is the heights of the students
    
    # Create the linked list
    head = Node(values[0])
    temp = head
    for val in values[1:]:
        temp.next = Node(val)
        temp = temp.next
    
    # Call user logic function and print the output
    result = minChanges(head, n)
    print(result)

if __name__ == "__main__":
    main()
