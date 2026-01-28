class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle)):
            window = haystack[i:len(needle)]
            print(f"window[{i}:{len(needle)}]. {window}")
            if window == needle:
                return i
        print(range(len(haystack) - len(needle)))
        return -1


run  =Solution()
r = run.strStr("heysomesome", "some")
print(r)
