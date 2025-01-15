def lengthOfLastWord(s):
    reverse = s[::-1].strip()

    listResult = []
    for i in reverse:
        if i != ' ':
            listResult.append(i)
        else:
            break
    
    res = ''.join(listResult)
    res = res[::-1]
    return len(res)

lengthOfLastWord('   fly me   to   the moon  ')
