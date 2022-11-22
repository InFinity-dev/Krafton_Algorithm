def kmpsearch(pattern, txt):
    m = len(pattern)
    n = len(txt)

    lps = [0] * m
    piarray(pattern, lps)

    i = 0
    j = 0
    while i < n:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        elif pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

        if j == m:
            print(f'{i - j + 1} 번째 글자에서 일치하는 패턴을 찾았습니다.')
            print(f'>>>> {txt[i - j:]}')
            j = lps[j - 1]


# Pattern = 찾는 문자열 패턴
# LPS = Longest Proper Prefix which is Suffix
def piarray(pattern, lps):
    length = 0

    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1


text = 'ABABDABACDABABCABAB'
pat = 'ABABCABAB'

kmpsearch(pat, text)
