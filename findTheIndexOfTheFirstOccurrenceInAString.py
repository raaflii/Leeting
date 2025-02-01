def strStr(haystack, needle):
    if needle not in haystack:
        return -1
    
    return haystack.index(needle)

a = strStr("This is a sample string", "sample")
print(a)