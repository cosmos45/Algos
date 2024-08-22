class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        

        def nextValidChar(str, index):
            backspace = 0
            while index >= 0:
                if backspace == 0 and str[index] != '#':
                    break
                elif str[index] == '#':
                    backspace += 1
                else:
                    backspace -= 1
                index -= 1
            return index

        indexofs, indexoft = len(s) - 1, len(t) - 1

        while indexofs >= 0 or indexoft >= 0:
            indexofs = nextValidChar(s, indexofs)
            indexoft = nextValidChar(t, indexoft)

            charofs = s[indexofs] if indexofs >= 0 else ""
            charoft = t[indexoft] if indexoft >= 0 else ""

            if charofs != charoft:
                return False
            indexofs -= 1
            indexoft -= 1
        return True