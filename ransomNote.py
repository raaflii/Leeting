def canConstruct(ransomNote, magazine):
    listM = list(magazine)

    for i in ransomNote:
        if i not in listM:
            return False

        listM.remove(i)

    return True

a = canConstruct("aaa", "aba")
print(a)