import math

def find_path(G):
    n = len(G)
    INF = math.inf
    
    C = [INF] * n
    P = [0] * n
    
    sink = n - 1
    C[sink] = 0
    
    for i in range(n - 2, -1, -1):
        m_cost = INF
        m_next = -1
        
        for j in range(i + 1, n):
            e_cost = G[i][j]
            
            if e_cost != INF:
                t_cost = e_cost + C[j]
                
                if t_cost < m_cost:
                    m_cost = t_cost
                    m_next = j
        
        C[i] = m_cost
        P[i] = m_next
    
    path = [0] * (n + 1)
    path[0] = 0 
    
    curr = 0
    k = 1
    
    while curr != sink:
        if curr == -1 or P[curr] == -1:
             break
        
        next_node = P[curr]
        path[k] = next_node
        curr = next_node
        k += 1
        
    f_path = path[:k]
    
    return C[0], f_path

INF = math.inf
G_data = [
    [INF,   5,   2, INF, INF, INF, INF, INF, INF],
    [INF, INF, INF,   3,   3,   3, INF, INF, INF],
    [INF, INF, INF, INF,   5,   8, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF,   1,   4, INF],
    [INF, INF, INF, INF, INF, INF,   6,   2, INF],
    [INF, INF, INF, INF, INF, INF,   6,   2, INF],
    [INF, INF, INF, INF, INF, INF, INF, INF,   7],
    [INF, INF, INF, INF, INF, INF, INF, INF,   3],
    [INF, INF, INF, INF, INF, INF, INF, INF, INF]
]

m_cost, p_raw = find_path(G_data)

path_final = [node + 1 for node in p_raw]

print(f"Total Cost: {m_cost}")
print(f"Shortest Path: {path_final}")
