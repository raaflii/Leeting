def keyboardRow(words):
    row = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    res = []

    for k in row:
        for i in words:
            temp = []
            for j in i:
                j = j.lower()
                if j in k:
                    temp.append(j)
                else:
                    continue    

                if len(temp) == len(i):
                    res.append(i)

    print(res)

keyboardRow(["omk"])