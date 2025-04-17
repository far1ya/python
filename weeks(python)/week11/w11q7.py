def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices is len(p) - 1
    dp = [[0] * n for _ in range(n)]  # DP table to store the minimum multiplication costs
    split = [[0] * n for _ in range(n)]  # Table to store the split point for optimal solution

    # l is the chain length
    for length in range(2, n + 1):  # length of the subproblem chain
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')  # Set to infinity to find the minimum
            for k in range(i, j):
                q = dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q
                    split[i][j] = k

    # Return the DP table and split table
    return dp, split

def print_optimal_parenthesization(split, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(split, i, split[i][j])
        print(" x ", end="")
        print_optimal_parenthesization(split, split[i][j] + 1, j)
        print(")", end="")

def matrix_chain_multiplication(p):
    dp, split = matrix_chain_order(p)
    print(f"Minimum number of multiplications is {dp[0][len(p) - 2]}")
    print("Optimal Parenthesization is: ", end="")
    print_optimal_parenthesization(split, 0, len(p) - 2)
    print()

# Example usage
# Matrix dimensions: A1 (10x20), A2 (20x30), A3 (30x40), A4 (40x30)
p = [10, 20, 30, 40, 30]  # Dimensions p0 x p1, p1 x p2, ..., pn-1 x pn
matrix_chain_multiplication(p)
