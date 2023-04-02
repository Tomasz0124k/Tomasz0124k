A = ["Janusz", "Zbigniew", "Andrzej", "Jan", "Jarosław", "Monika"]
B = ["Karol", "Tomasz", "Jakub", "Jan", "Zbigniew", "Monika"]
C = ["Damian", "Zbigniew", "Jakub", "Zbigniew", "Jarosław", "Kamila"]
set_A = set(A)
set_B = set(B)
set_C = set(C)
#1
common_elements = set_A & set_B
print(common_elements)
#2
common_elements = set_A & set_B & set_C
print(common_elements)
#3
elements_only_in_C = set_C - set_A
print(elements_only_in_C)
#4
elements_only_in_B = set_B - (set_A | set_C)
print(elements_only_in_B)
#5 
all_elements = set_A | set_B | set_C
print(all_elements)
#6
elements_only_in_A = set_A - (set_B & set_C)
print(set_B & set_C)
print(elements_only_in_A)
