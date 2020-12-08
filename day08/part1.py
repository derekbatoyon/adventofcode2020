import fileinput

class Instruction(object):
    def __init__(self, line):
        (o, a) = line.split()
        self.operation = o
        self.argument = int(a)

def main():
    code = [Instruction(line) for line in fileinput.input()]
    flag = [False] * len(code)

    accumulator = 0
    program_ptr = 0

    process = {
        'acc' : lambda a: (a, 1),
        'jmp' : lambda a: (0, a),
        'nop' : lambda a: (0, 1),
    }

    end = len(code)
    while program_ptr < end:
        instr = code[program_ptr]
        #print(instr.operation, instr.argument)
        if flag[program_ptr]:
            print(accumulator)
            break
        (acc, prg) = process[instr.operation](instr.argument)
        flag[program_ptr] = True
        accumulator += acc
        program_ptr += prg

if __name__ == "__main__":
    main()
