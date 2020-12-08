import fileinput

class Instruction(object):
    def __init__(self, *args, **kwargs):
        if len(args):
            arg1 = args[0]
            if type(arg1) is list:
                self.operation = arg1[0]
                self.argument = int(arg1[1])
        if 'op' in kwargs:
            self.operation = kwargs['op']
        if 'arg' in kwargs:
            self.argument = kwargs['arg']

def run(code):
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
        if flag[program_ptr]:
            raise RuntimeError
        instr = code[program_ptr]
        (acc, prg) = process[instr.operation](instr.argument)
        flag[program_ptr] = True
        accumulator += acc
        program_ptr += prg
        if program_ptr == end:
            break
    return accumulator

def main():
    code = [Instruction(line.split()) for line in fileinput.input()]

    for index in range(len(code)):

        old_instr = code[index]
        if old_instr.operation == 'jmp':
            code[index] = Instruction(op = 'nop', arg = old_instr.argument)
        elif old_instr.operation == 'nop':
            code[index] = Instruction(op = 'jmp', arg = old_instr.argument)
        else:
            continue

        try:
            result = run(code)
            print(result)
        except RuntimeError:
            pass

        code[index] = old_instr

if __name__ == "__main__":
    #instr = Instruction("foobar 42".split())
    #instr = Instruction(op = "foobar", arg = 42)
    #print(instr.operation, instr.argument)
    main()
