MOD = 10**9 + 7

def comb_mod(n, r, fact, inv_fact):
    return (fact[n] * inv_fact[r] * inv_fact[n - r]) % MOD

def solve(L, M, K):
    n = K - L + 1
    fact = [1] * (L + 2 * n)
    inv_fact = [1] * (L + 2 * n)

    for i in range(1, L + 2 * n):
        fact[i] = (fact[i - 1] * i) % MOD

    inv_fact[L + 2 * n - 1] = pow(fact[L + 2 * n - 1], MOD - 2, MOD)
    for i in range(L + 2 * n - 2, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    S0 = 0
    for i in range(1, n + 1):
        S0 = (S0 + i) % MOD

    result = (pow(M + 1, L + 1, MOD) - 1) % MOD

    for i in range(1, L + 1):
        Si = 0
        for j in range(L + 2 * n - 1):
            Si = (Si + comb_mod(L + 1, j, fact, inv_fact) * pow(j + 1, i, MOD)) % MOD

        result = (result - (comb_mod(L + 1, i, fact, inv_fact) * Si) % MOD) % MOD

    result = (result + S0) % MOD

    return result

T = int(input())
for _ in range(T):
    L, M, K = map(int, input().split())
    result = solve(L, M, K)
    print(result)
