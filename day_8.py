"""Day 8 of the 2020 Advent of Code

Introduction to the computer!
"""

import copy

class BootCode:
    def __init__(self, instructions):
        self.accumulator = 0
        self.pointer = 0
        self.instructions = instructions

    def acc(self, val, *discard):
        self.accumulator += val
        self.pointer += 1

    def jmp(self, val, *discard):
        self.pointer += val

    def nop(self, *discard):
        self.pointer += 1

    def operation(self, instruction):
        getattr(self, instruction[0])(instruction[1])

    def findLoop(self):
        visited = set()
        while self.pointer not in visited:
            if self.pointer >= len(self.instructions):
                print("Success!")
                print(self.accumulator)
                return -1
            visited.add(self.pointer)
            self.operation(self.instructions[self.pointer])
        return self.accumulator

            
def readFile(fileName):
    instructions_raw = open(fileName).read().strip().split('\n')
    instruction_set = []
    for line in instructions_raw:
        temp = line.split(' ')
        instruction_set.append([temp[0], int(temp[1])])
    return instruction_set


def main():
    input = readFile('input_08_1.txt')
    game_console = BootCode(input)
    print('Part 1:', game_console.findLoop())
    print('Part 2:')
    for i in range(len(input)):
        if input[i][0] == 'jmp':
            input[i][0] = 'nop'
            game_console = BootCode(input)
            if game_console.findLoop() == -1:
                return True
            input[i][0] = 'jmp'
            
        elif input[i][0] == 'nop':
            input[i][0] = 'jmp'
            game_console = BootCode(input)
            if game_console.findLoop() == -1:
                return True
            input[i][0] = 'nop'
            
        


main()
            
