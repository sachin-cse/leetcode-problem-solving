def threesum(s):
    s.sort()
    result = []
    
    for k in range(len(s)):
        if k > 0 and s[k] == s[k - 1]:  # Skip duplicates
            continue
        
        target = -s[k]
        i, j = k + 1, len(s) - 1
        
        while i < j:
            total = s[i] + s[j]
            
            if total < target:
                i += 1
            elif total > target:
                j -= 1
            else:
                result.append([s[k], s[i], s[j]])
                i += 1
                j -= 1
                
                # Skip duplicates
                while i < j and s[i] == s[i - 1]:
                    i += 1
                while i < j and s[j] == s[j + 1]:
                    j -= 1
    
    return result

print(threesum([-1, 0, 1, 2, -1, -4]))
