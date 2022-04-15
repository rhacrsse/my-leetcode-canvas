#!/usr/bin/python3

import functools as ft

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        pino={i for i in ransomNote}
        listone = { ransomNote.count(i) <= magazine.count(i) for i in pino }
        return True if False not in listone else False
