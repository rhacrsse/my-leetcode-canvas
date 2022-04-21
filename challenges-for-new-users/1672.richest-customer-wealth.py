#!/usr/bin/python3

class Solution:
    def maximumWealth(self, accounts: [[int]]) -> int:
        return max(list(map(sum,accounts)))
        #return max([sum(i) for i in accounts])

pino = Solution()
accounts = [[1,2,3],[3,2,1]]
print(pino.maximumWealth(accounts))

accounts = [[1,5],[7,3],[3,5]]
print(pino.maximumWealth(accounts))

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(pino.maximumWealth(accounts))
