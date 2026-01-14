class Solution(object):
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []  # holds indices of days with unresolved warmer temperature

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
    print(sol.dailyTemperatures([30,40,50,60]))              # [1,1,1,0]
    print(sol.dailyTemperatures([30,60,90]))                 # [1,1,0]
