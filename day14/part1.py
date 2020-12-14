import fileinput
import re

def main():
    mask_set = re.compile('mask\s+=\s+(?P<mask>[01X]{36})$')
    mem_set = re.compile('mem\[(?P<address>\d+)\]\s+=\s+(?P<value>\d+)$')

    memory = dict()
    one_mask = 0
    zero_mask = 0xFFFFFFFFF # 36 bits

    for line in fileinput.input():
        if m := mask_set.match(line):
            one_mask = 0
            zero_mask = 0xFFFFFFFFF # 36 bits

            for i, bit in enumerate(reversed(m.group('mask'))):
                mask = 1 << i
                if bit == '1':
                    one_mask |= mask
                elif bit == '0':
                    zero_mask &= ~mask
                elif bit != 'X':
                    raise RuntimeError

        elif m := mem_set.match(line):
            address = int(m.group('address'))
            value = int(m.group('value'))
            memory[address] = value & zero_mask | one_mask

        else:
            raise RuntimeError

    print(sum(memory.values()))

if __name__ == "__main__":
    main()
