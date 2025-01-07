def convertRomanToInt(roman):
    daftarRoman = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    listHasil = []
    hasil = 0

    pisahString = list(roman)
    # print(pisahString)
    
    for i in pisahString:
        listHasil.append(daftarRoman[i])
    # print(listHasil)

    for j in listHasil:
        hasil += j

    for k in range (0, len(listHasil)-1):
        # print(listHasil[k] == 1 and listHasil[j+1] == 5 or listHasil[j+1] == 10)
        # print(listHasil[k] == 10 and listHasil[k+1] == 50 or listHasil[k+1] == 100)
        # print(listHasil[k] == 100 and listHasil[j+1] == 500 or listHasil[j+1] == 1000)
        
        if listHasil[k] == 1 and (listHasil[k+1] == 5 or listHasil[k+1] == 10):
            hasil -= 2*daftarRoman["I"]
            # print(k, 1)

        if listHasil[k] == 10 and (listHasil[k+1] == 50 or listHasil[k+1] == 100):
            hasil -= 2*daftarRoman["X"]
            # print(k, 2)

        if listHasil[k] == 100 and (listHasil[k+1] == 500 or listHasil[k+1] == 1000):
            hasil -= 2*daftarRoman["C"]
            # print(k, 3)
    
    print(hasil)


convertRomanToInt("MCMXCIV")
