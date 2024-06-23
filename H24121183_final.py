# Function to parse input matrix
def parse_matrix(input_str):
    matrix = []
    rows = input_str.split('|')
    for row in rows:
        matrix.append([int(num) for num in row.split(',')])
    return matrix

# Function to multiply two matrices
def multiply_matrices(U, V):
    n = len(U)
    M = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                M[i][j] += U[i][k] * V[k][j]
    return M

# Function to print matrix
def print_matrix(M):
    for row in M:
        print(row)

# Main function
def main():
    # Input matrices
    u_input = input("Enter matrix U: ")
    v_input = input("Enter matrix V: ")
    
    # Parse matrices
    U = parse_matrix(u_input)
    V = parse_matrix(v_input)
    
    # Multiply matrices
    M = multiply_matrices(U, V)
    
    # Output result
    print("M = U x V")
    print_matrix(M)

# Run main function
if __name__ == "__main__":
    main()
