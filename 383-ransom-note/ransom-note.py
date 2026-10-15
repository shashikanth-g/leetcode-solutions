class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        fre = {}

        for ch in magazine:
            if ch in fre:
                fre[ch] += 1
            else:
                fre[ch] = 1

        for ch in ransomNote:
            if ch not in fre or fre[ch] == 0:
                return False

            fre[ch] -= 1

        return True
