class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
#array version
        if len(s1) > len(s2):
            return False

        freq1 = [0] * 26
        freq2 = [0] * 26

        # s1 frequency
        for ch in s1:
            idx = ord(ch) - ord('a')
            freq1[idx] += 1

        left = 0

        for right in range(len(s2)):

            idx = ord(s2[right]) - ord('a')
            freq2[idx] += 1

            # window size maintain
            if (right - left + 1) > len(s1):

                left_idx = ord(s2[left]) - ord('a')
                freq2[left_idx] -= 1
                left += 1

            # compare
            if freq1 == freq2:
                return True

        return False