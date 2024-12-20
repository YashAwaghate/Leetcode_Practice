class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = [False] * len(candies)
        max_candies = max(candies)
        for idx in range(len(candies)):
            if (candies[idx] + extraCandies) >= max_candies:
                result[idx] = True
        return result


def main():
    candies = [2,3,5,1,3]
    extraCandies = 3
    sol_obj = Solution()
    result = sol_obj.kidsWithCandies(candies, extraCandies)
    print(result)


if __name__ == '__main__':
    main()

