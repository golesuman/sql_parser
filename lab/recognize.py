def recognize_a(input_string):
    # DFA for 'a'
    current_state = 'q0'
    for char in input_string:
        if current_state == 'q0' and char == 'a':
            current_state = 'q1'
        else:
            return False
    return current_state == 'q1'

def recognize_a_star_b_plus(input_string):
    # DFA for 'a*b+'
    current_state = 'q0'
    for char in input_string:
        if current_state == 'q0' and char == 'a':
            current_state = 'q1'
        elif current_state == 'q1' and char == 'a':
            current_state = 'q1'
        elif current_state == 'q1' and char == 'b':
            current_state = 'q2'
        else:
            return False
    return current_state == 'q2'

def recognize_babb(input_string):
    # DFA for 'babb'
    current_state = 'q0'
    for char in input_string:
        if current_state == 'q0' and char == 'b':
            current_state = 'q1'
        elif current_state == 'q1' and char == 'a':
            current_state = 'q2'
        elif current_state == 'q2' and char == 'b':
            current_state = 'q3'
        elif current_state == 'q3' and char == 'b':
            current_state = 'q3'
        else:
            return False
    return current_state == 'q3'

# Test cases
input_strings = ['a', 'abbb', 'aab', 'babb', 'ba', 'abc', 'babbb']
for string in input_strings:
    print(f'String: "{string}"')
    print(f'Pattern a: {recognize_a(string)}')
    print(f'Pattern a*b+: {recognize_a_star_b_plus(string)}')
    print(f'Pattern babb: {recognize_babb(string)}')
    print('---')