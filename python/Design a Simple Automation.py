class Automaton(object):
    def __init__ (self):
        self.states = {
                'q1': self.q1,
                'q2': self.q2,
                'q3': self.q3
                }

        self.current_state = 'q1'

    def q1(self, command):
        if command == '1':
            self.current_state = 'q2'

    def q2(self, command):
        if command == '0':
            self.current_state = 'q3'
        elif command == '1':
            self.current_state = 'q2'
    def q3(self, command):
        if command == '0' or command == '1':
            self.current_state = 'q2'

    def read_commands(self, commands):
        # Return True if we end in our accept state, False otherwise
        for command in commands:
            state_function = self.states[self.current_state]
            state_function(command)
        return self.current_state == 'q2'

my_automaton = Automaton()
result = my_automaton.read_commands(["1", "0", "0", "1", "0"])
print(result)

# Do anything necessary to set up your automaton's states, q1, q2, and q3
