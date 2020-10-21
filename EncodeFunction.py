# Stwórz funkcję encode() która jako argument przyjmuje string
# a zwraca ten string z literami zamienionymi wg podanego niżej
# schematu + wszystkimi literami zmienionymi na duże:
#
# I -> 1
# Z -> 2
# E -> 3
# A -> 4
# S -> 5
# T -> 7
# B -> 8
# O -> 0

def encode (text_before, to_replace, replaced):
    for every_char in to_replace:
            index_number_list = to_replace.index(every_char)
            text_before = text_before.replace(every_char, replaced[index_number_list])

    return text_before.upper()

text = 'Is Zed Eating All Strings Texts Before Oatmeal'
text_after = encode(text, ['I','Z','E','A','S','T','B','O'], ['1','2','3','4','5','7','8','0'])

print('String before replace: ', text)
print('String after replace: ', text_after)