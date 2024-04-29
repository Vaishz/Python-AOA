def rabin_karp(s, p, d=26, q=11):
    n = len(s)
    m = len(p)
    h = pow(d, m-1) % q
    hash_p = 0
    hash_s = 0
    output = []
    for i in range(m):
        hash_p = (d*hash_p + ord(p[i])) % q
        hash_s = (d*hash_s + ord(s[i])) % q
    for i in range(n-m+1):
        if hash_s == hash_p:
            if s[i:i+m] == p:  #RECHECKING  
                output.append(i)
        if i < n-m:
            hash_s = (d*(hash_s-ord(s[i])*h)+ord(s[i+m])) % q
    return output


s = "acaabacaaabaababcda"
p = "aaba"
print(rabin_karp(s, p))
# Output: [2, 8, 11]

