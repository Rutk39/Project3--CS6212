def minimize_cost(galaxies, k, cost_matrix):
    n = len(galaxies)
    
    # Initialize dp array with dimensions (n, k+1)
    dp = [[float('inf')] * (k + 1) for _ in range(n)]
    
    # Initialize the first galaxy (1) with cost 0 for passing through 0 astro-haunted galaxies
    dp[1][0] = 0

    for j in range(1, k + 1):
        for i in range(2, n):
            if galaxies[i] == 1:
                for i_prime in range(1, i):
                    if galaxies[i_prime] == 1:
                        dp[i][j] = min(dp[i][j], dp[i_prime][j - 1] + cost_matrix[i_prime][i])

    # Find the minimum cost to reach galaxy n while passing through at most k astro-haunted galaxies
    min_cost = min(dp[n - 1])
    return min_cost

# Example usage
galaxies = [0, 1, 0, 1, 0, 0, 1]  # Example astro-haunted galaxy configuration
k = 2  # Maximum allowed astro-haunted galaxies
cost_matrix = [
    [0, 2, 0, 4, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
]

result = minimize_cost(galaxies, k, cost_matrix)
print("Minimum cost:", result)

