#!/usr/bin/python3

import functools as ft

class Solution:
    def groupAnagrams(self, strs: [str]) -> [[str]]:
        maps = {}
        for i in strs:
            ordl = sorted(i)
            temp=""
            ordi = temp.join(ordl)

            if ordi in maps:
                maps[ordi].append(i)
            else:
                maps[ordi]=[i]

        outs = []
        for i in maps:
            outs.append(maps[i])

        return outs

pino = Solution()

inputs = ["eat","tea","tan","ate","nat","bat"]
print(pino.groupAnagrams(inputs))

inputs = [""]
print(pino.groupAnagrams(inputs))

inputs = ["a"]
print(pino.groupAnagrams(inputs))
