def percentageLetter(self, s: str, letter: str) -> int:
        a = len(s)
        b = 0
        for i in range(a):
            if s[i]==letter:
                b += 1
        return floor(100 * b/a)
