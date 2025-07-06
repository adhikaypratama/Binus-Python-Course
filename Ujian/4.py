def rerata_nilai_mhs(dataDict):
    return sum(dataDict)/len(dataDict)
    
dataDict = [80, 70, 70, 80]

print(dataDict, "\nRata-rata: ", rerata_nilai_mhs(dataDict))
