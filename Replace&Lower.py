def replace (inscription):
    for every_char in inscription:
        if every_char.isupper():
            inscription = inscription.replace(every_char, '-' + every_char.lower())
        elif every_char.islower():
            continue
        else:
            inscription = inscription.replace(every_char, '-' + every_char)

    return inscription

text = 'thisIsMy2ProgramInPython'
print('String before replace: ', text)
print('String after replace: ', replace(text))

