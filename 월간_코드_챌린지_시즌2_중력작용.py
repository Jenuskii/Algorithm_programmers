values = [1,10,100,1000,10000]
edges = [[1,2],[1,3],[2,4],[2,5]]
queries = [[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[4,1000],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1],[2,1],[1,-1],[2,-1],[3,-1],[4,-1],[5,-1]]
results = [11111,11010,100,1000,10000,11111,10011,100,10,10000,11111,11010,100,10,10000]


# len_e = len(edges)
# val = [0] + values
# FATHER = dict()
# for i in edges:
#     father, kid = i
#     FATHER[kid] = father




# def Q1(n):
#     if n not in [edges[i][0] for i in range(len_e)]:
#         return val[n]
#     else:
#         return val[n] + sum([Q1(m) for m in set([edges[i][1] for i in range(len_e) if edges[i][0]  == n])])



# dp = ['null'] * len(val)
# for n in ({i for i in range(1,len(val))} - set([edges[i][0] for i in range(len_e)])):
#     dp[n] = val[n]

# def Q1(n):
#     if dp[n] != 'null':
#         return dp[n]
#     else:
#         dp[n] = val[n] + sum([Q1(m) for m in set([edges[i][1] for i in range(len_e) if edges[i][0]  == n])])
#     return dp[n]

# def Q2(u,w):
#     now = u
#     while now != 1:
#         val[now] = val[FATHER[now]]
#         now = FATHER[now]
#     val[now] = w
    

def solution(values,edges,queries):
    len_e = len(edges)
    val = [0] + values
    FATHER = dict()
    for i in edges:
        father, kid = i
        FATHER[kid] = father
    dp = ['null'] * len(val)
    for n in ({i for i in range(1,len(val))} - set([edges[i][0] for i in range(len_e)])):
        dp[n] = val[n]

    def Q1(n):
        if dp[n] != 'null':
            return dp[n]
        else:
            dp[n] = val[n] + sum([Q1(m) for m in set([edges[i][1] for i in range(len_e) if edges[i][0]  == n])])
        return dp[n]

    def Q2(u,w):
        now = u
        while now != 1:
            val[now] = val[FATHER[now]]
            now = FATHER[now]
        val[now] = w

    answer = []
    for query in queries:
        a, b = query
        if b == -1:
            answer.append(Q1(a))
        else:
            Q2(a,b)
            dp = ['null'] * len(val)

    return answer

print(solution(values,edges,queries))