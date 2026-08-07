class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Prime factorize t
        T2 = T3 = T5 = T7 = 0
        temp = t
        while temp % 2 == 0: T2 += 1; temp //= 2
        while temp % 3 == 0: T3 += 1; temp //= 3
        while temp % 5 == 0: T5 += 1; temp //= 5
        while temp % 7 == 0: T7 += 1; temp //= 7
        
        # If t has prime factors other than 2, 3, 5, 7, it's impossible.
        if temp > 1:
            return "-1"
            
        # Step 2: DP to find min digits to get >= r2 twos and >= r3 threes
        # Sizes 65 and 45 are safe because 2^47 > 10^14 and 3^30 > 10^14.
        dp = [[float('inf')] * 45 for _ in range(65)]
        dp[0][0] = 0
        
        # Mapping digit -> (count of 2, count of 3, count of 5, count of 7)
        factors = {
            1: (0, 0, 0, 0), 2: (1, 0, 0, 0), 3: (0, 1, 0, 0),
            4: (2, 0, 0, 0), 5: (0, 0, 1, 0), 6: (1, 1, 0, 0),
            7: (0, 0, 0, 1), 8: (3, 0, 0, 0), 9: (0, 2, 0, 0)
        }
        
        for i in range(60):
            for j in range(40):
                if dp[i][j] == float('inf'): continue
                for d in [2, 3, 4, 6, 8, 9]:
                    c2, c3, _, _ = factors[d]
                    ni, nj = min(60, i + c2), min(40, j + c3)
                    if dp[i][j] + 1 < dp[ni][nj]:
                        dp[ni][nj] = dp[i][j] + 1
                        
        # Retroactively make it represent "AT LEAST i twos and j threes"
        for i in range(60, -1, -1):
            for j in range(40, -1, -1):
                if i < 60: dp[i][j] = min(dp[i][j], dp[i+1][j])
                if j < 40: dp[i][j] = min(dp[i][j], dp[i][j+1])
                    
        def min_len(r2, r3, r5, r7):
            return dp[r2][r3] + r5 + r7
            
        # Step 3: Compute prefix running totals of prime factors
        n = len(num)
        pref = [(0, 0, 0, 0)] * (n + 1)
        z_idx = n  # Keep track of the first '0'
        
        for i in range(n):
            d = int(num[i])
            if d == 0:
                z_idx = min(z_idx, i)
                pref[i+1] = pref[i]
            else:
                c2, c3, c5, c7 = factors[d]
                p2, p3, p5, p7 = pref[i]
                pref[i+1] = (p2 + c2, p3 + c3, p5 + c5, p7 + c7)
                
        # Check if the original number itself is already a valid answer
        if z_idx == n:
            p2, p3, p5, p7 = pref[n]
            if p2 >= T2 and p3 >= T3 and p5 >= T5 and p7 >= T7:
                return num
                
        # Helper: Greedily build the lexicographically smallest suffix
        def build_suffix(L, R2, R3, R5, R7):
            res = []
            for pos in range(L):
                for d in range(1, 10):
                    c2, c3, c5, c7 = factors[d]
                    nR2, nR3 = max(0, R2 - c2), max(0, R3 - c3)
                    nR5, nR7 = max(0, R5 - c5), max(0, R7 - c7)
                    
                    if min_len(nR2, nR3, nR5, nR7) <= L - 1 - pos:
                        res.append(str(d))
                        R2, R3, R5, R7 = nR2, nR3, nR5, nR7
                        break
            return "".join(res)
            
        # Step 4: Find the rightmost index where we can strictly increase a digit
        # We cannot maintain a prefix that contains a '0', so loop starts at min(n - 1, z_idx)
        for i in range(min(n - 1, z_idx), -1, -1):
            p2, p3, p5, p7 = pref[i]
            start_d = int(num[i]) + 1
            for d in range(start_d, 10):
                c2, c3, c5, c7 = factors[d]
                R2, R3 = max(0, T2 - p2 - c2), max(0, T3 - p3 - c3)
                R5, R7 = max(0, T5 - p5 - c5), max(0, T7 - p7 - c7)
                
                L = n - 1 - i
                if min_len(R2, R3, R5, R7) <= L:
                    return num[:i] + str(d) + build_suffix(L, R2, R3, R5, R7)
                    
        # Step 5: If modifying existing digits didn't work, we need a longer string length.
        # Find the max between (n + 1) and the absolute minimum digits required.
        req_len = min_len(T2, T3, T5, T7)
        new_L = max(n + 1, req_len)
        return build_suffix(new_L, T2, T3, T5, T7)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna