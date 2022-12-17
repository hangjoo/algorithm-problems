from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = [self.convert(num) for num in range(1, n + 1)]

        return answer

    @staticmethod
    def convert(num: int) -> str:
        if num % 15 == 0:
            return "FizzBuzz"
        elif num % 3 == 0:
            return "Fizz"
        elif num % 5 == 0:
            return "Buzz"
        else:
            return str(num)
