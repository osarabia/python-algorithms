

array_input = [3,4,5,6,7,8]
i = 0
while i < len(array_input)/2:
    last_index = len(array_input) - 1 - i
    first_element = array_input[i]
    array_input[i] = array_input[last_index]
    array_input[last_index] = first_element
    i = i + 1
print(array_input)
