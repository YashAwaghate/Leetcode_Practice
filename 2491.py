"""
You are given a positive integer array skill of even length n where skill[i]
denotes the skill of the ith player. Divide the players into n / 2 teams of
size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills
of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if
there is no way to divide the players into teams such that the total skill
of each team is equal.

Example 1:
Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation:
Divide the players into the following teams: (1, 5), (2, 4), (3, 3),
 where each team has a total skill of 6.
The sum of the chemistry of all the teams is:
1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

Example 2:
Input: skill = [3,4]
Output: 12
Explanation:
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.

Example 3:
Input: skill = [1,1,2,3]
Output: -1
Explanation:
There is no way to divide the players into teams such that the
total skill of each team is equal.

"""
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        print(skill)
        if len(skill) % 2 != 0:
            return -1

        skill.sort()
        skill_lvl = skill[0] + skill[-1]
        chem = 0
        for index in range(len(skill)//2):
            p1=skill[index]
            p2 = skill[len(skill)-1-index]
            curr_skill = p1 + p2
            if curr_skill == skill_lvl:
                chem += (p1*p2)
            else:
                return -1
        return chem


def main():
    obj = Solution()
    print(obj.dividePlayers([3, 2, 5, 1, 3, 4]))
    print(obj.dividePlayers([3,4]))
    print(obj.dividePlayers([1,1,2,3]))


if __name__ == '__main__':
    main()
