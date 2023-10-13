def longeststring(s):
    chr = {}
    max_length = 0
    start = 0
    
    for i in range(len(s)):
        if s[i] in chr and chr[s[i]] >= start:
            start = chr[s[i]]
        chr[s[i]] = i
        max_length = max(max_length, i-start+1)
        
    return max_length

print(longeststring('abcabcbb'))