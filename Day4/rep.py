def repete(word):
    final = []
    for letter in word:
        if letter.lower() in "aeiou":
            final.append(letter*2)
        else:
            final.append(letter)
    #palavra = final
    return final
print(repete("banana"))

#python -m pdb rep.py    executa em modo debug
#breakpoint()