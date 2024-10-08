class Solution:
    def minSwaps(self, s: str) -> int:
        ans = 0
        for c in s:
            if c == '[':
                ans += 1
            elif ans > 0:
                ans -= 1
        return (ans + 1) // 2
def main():
    obj = Solution()
    print(obj.minSwaps("][]["))
    print(obj.minSwaps("]]][[["))
    print(obj.minSwaps("[]"))


if __name__ == '__main__':
    main()