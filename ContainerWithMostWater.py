class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Maintain two pointers, left and right
        Initial water volume is 0
        While left < right:
            current volume = (right - left)*(min height)
            water volume = maximum (old volume, current volume)
            if height[left] < height [right]:
                left+=1
            else:
                right+=1

        args:
        height: list of numbers showing the height at every position

        return:
        water: max volume of water
        """
        water = 0
        i, j = 0, len(height) - 1
        while i < j:
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
