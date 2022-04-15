#!/usr/bin/python3

# Given an integer n, return a string array answer (1-indexed) where:
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.

class Solution:
    def ans1(self, n):
        return n % 3 == 0 and n % 5 == 0

    def ans2(self, n):
        return n % 3 == 0

    def ans3(self, n):
        return n % 5 == 0

    def fizzBuzz(self, n: int) -> [str]:
        return ["FizzBuzz" if self.ans1(i) else "Fizz" if self.ans2(i) else "Buzz" if self.ans3(i) else str(i) for i in list(range(1,n+1))]

pino = Solution()
print(pino.fizzBuzz(5))
