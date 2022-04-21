#!/usr/bin/python3

class Solution:
    def kWeakestRows(self, mat: [[int]], k: int) -> [int]:
        sumlist = list(map(sum,mat))
        indexlist = list(range(len(sumlist)))
        outt = sorted(list(zip(sumlist, indexlist)))
        outl = [i[1] for i in outt ]

        return outl[:k]

[2,4,1,2,5]
[0,1,2,3,4]

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3

pino = Solution()
print(pino.kWeakestRows(mat,k))

