#SYED ABDULLAH ASHAR
#200901074
#DFS CODE TO FIND PATH FROM A to G where 1 is blocker
grid = [
    [ 'A', 1, 1, 1 ],
    [ 0, 1, 1, 0 ],
    [ 0, 0, 0, 0 ],
    [ 0, 1, 1, 0 ],
    [ 0, 0, 1, 'G' ]
]

# Checking valadity of function
def is_valid_cell(row, col):
    # Checking and verifying 
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
        return False
    # Check if the cell is not blocked
    if grid[row][col] == 1:
        return False
    
    return True


def find_path(start_row, start_col, end_row, end_col):
    
    stack = [(start_row, start_col)]
    
    
    visited = set()
    
    # Use a dictionary to keep track of the parent of each cell in the path
    parents = {}
    
    # DFS loop
    while stack:
        # Pop the current cell from the stack
        row, col = stack.pop()
        
        # Mark the current cell as visited
        visited.add((row, col))
        
        # Check if we have reached the end cell
        if row == end_row and col == end_col:
            # Reconstruct the path by following the parent links
            path = [(row, col)]
            while (row, col) != (start_row, start_col):
                row, col = parents[(row, col)]
                path.append((row, col))
            path.reverse()
            return path
        
        # Try each neighbor in turn
        for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor_row, neighbor_col = row + d_row, col + d_col
            neighbor = (neighbor_row, neighbor_col)
            # Check if the neighbor is valid and has not been visited
            if is_valid_cell(neighbor_row, neighbor_col) and neighbor not in visited:
                # Add the neighbor to the stack and mark it as visited
                stack.append(neighbor)
                visited.add(neighbor)
                # Set the parent of the neighbor to the current cell
                parents[neighbor] = (row, col)
    
    
    return None

# Find the path from A to G
start_row, start_col = 0, 0
end_row, end_col = 4, 3
path = find_path(start_row, start_col, end_row, end_col)

# Print the path
if path is None:
    print("No path found")
else:
    print("Path:", path)
