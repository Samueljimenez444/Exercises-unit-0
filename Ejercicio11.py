def isVocalOrNot (letter):

    isVocal=False

    str(letter).lower

    match letter[1]:   
        case "a":
            isVocal=True

        case "e":
            isVocal=True

        case "i":
            isVocal=True

        case "o":
            isVocal=True

        case "u":
            isVocal=True
            
    return isVocal

letter = (input("Introduce a letter"))        

print(isVocalOrNot(letter))