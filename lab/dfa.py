class DFA:
    def __init__(self):
        self.states = {'q0', 'q1', 'q2'}
        self.alphabet = {'0', '1'}
        self.transitions = {
            'q0': {'0': 'q1', '1': 'q0'},
            'q1': {'0': 'q1', '1': 'q2'},
            'q2': {'0': 'q3', '1': 'q2'},
            'q3': {'0': 'q3', '1': 'q2'}
        }
        self.start_state = 'q0'
        self.accept_state = 'q2'

    def validate_string(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transitions[current_state][symbol]

        return current_state == self.accept_state


# Create an instance of the DFA
dfa = DFA()

# Test some strings
strings_to_test = ['0101', '0011', '001', '101', '010111', '001', '1001']
for string in strings_to_test:
    if dfa.validate_string(string):
        print(f"'{string}' is accepted.")
    else:
        print(f"'{string}' is not accepted.")
