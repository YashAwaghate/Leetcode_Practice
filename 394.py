class Solution:
    def asteroidCollision(self, asteroids):

        pointer = 1

        while pointer < len(asteroids):
            current_num = asteroids[pointer]
            previous_num = asteroids[pointer - 1]

            if current_num < 0 and previous_num > 0:
                abs_current_num = abs(current_num)
                abs_previous_num = abs(previous_num)
                winning_num = 0
                if abs_current_num > abs_previous_num:
                    winning_num = current_num
                elif abs_previous_num > abs_current_num:
                    winning_num = previous_num
                elif abs_current_num == abs_previous_num:
                    winning_num = 0

                if winning_num != 0:
                    asteroids = asteroids[:pointer - 1] + [
                        winning_num] + asteroids[pointer + 1:]

                elif winning_num == 0:
                    asteroids = asteroids[:pointer - 1] + asteroids[pointer + 1:]

                if pointer > 1:
                    pointer -= 1

            else:
                pointer += 1

        return asteroids


def main():
    candies = [-2,2,1,-2]
    sol_obj = Solution()
    result = sol_obj.asteroidCollision(candies)
    print(result)


if __name__ == '__main__':
    main()
