def optimal_bst_simple(keys, p, q, n):
    
    cost = [[0.0] * (n + 1) for _ in range(n + 1)]
    weight = [[0.0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        cost[i][i] = q[i]
        weight[i][i] = q[i]

    for l in range(1, n + 1):
        for i in range(n - l + 1):
            j = i + l

            if l == 1:
                weight[i][j] = q[i] + p[i] + q[j]
            else:
                weight[i][j] = weight[i][j-1] + p[j-1] + q[j]

            cost[i][j] = float('inf') 

            for k in range(i, j):
                current_cost = cost[i][k] + cost[k + 1][j] + weight[i][j]

                if current_cost < cost[i][j]:
                    cost[i][j] = current_cost

    min_expected_cost = cost[0][n]
    return min_expected_cost 


n = 4
P = [0.1, 0.2, 0.4, 0.3]
Q = [0.05, 0.1, 0.05, 0.05, 0.1]
Keys = [10, 20, 30, 40]


minimum_cost = optimal_bst_simple(Keys, P, Q, n)


print(f"Minimum expected cost: {minimum_cost:.4f}")