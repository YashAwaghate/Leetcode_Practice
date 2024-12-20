class Solution:
    def maxArea(self, height: list[int]) -> int:
        pt_l, pt_r = 0,len(height)-1
        max_area = -1
        while pt_r > pt_l:
            new_area = (pt_r - pt_l)*min(height[pt_l],height[pt_r])
            print(pt_l , pt_r , new_area)
            if (new_area) > max_area:
                max_area = new_area
            if height[pt_l] == min(height[pt_l],height[pt_r]):
                pt_l += 1
            else:
                pt_r -= 1
        return max_area

def main():
    height = [1,8,6,2,5,4,8,3,7]
    sol_obj = Solution()
    result = sol_obj.maxArea(height)
    print(result)


if __name__ == '__main__':
    main()
