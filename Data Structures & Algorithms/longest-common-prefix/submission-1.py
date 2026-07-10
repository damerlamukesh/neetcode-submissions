class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Traverse each character of the first string
        for i in range(len(strs[0])):

            # Compare with all remaining strings
            for s in strs[1:]:

                # Stop if:
                # 1. Current string is shorter
                # 2. Characters don't match
                if i == len(s) or s[i] != strs[0][i]:
                    return strs[0][:i]

        # Entire first string is the common prefix
        return strs[0]
        