import fileinput
import re

def permute_mask(mask):
    index = mask.find('X')
    if index == -1:
        yield mask
    else:
        yield from permute_mask(mask[:index] + '0' + mask[index+1:])
        yield from permute_mask(mask[:index] + '1' + mask[index+1:])

def decode_address(mask, address):
    new_mask = ['1' if bit == '0' and address & (1 << i) else bit for i, bit in enumerate(reversed(mask))]
    yield from permute_mask(''.join(reversed(new_mask)))

def main():
    mask_set = re.compile('mask\s+=\s+(?P<mask>[01X]{36})$')
    mem_set = re.compile('mem\[(?P<address>\d+)\]\s+=\s+(?P<value>\d+)$')

    memory = dict()
    mask = '0' * 36

    for line in fileinput.input():
        if m := mask_set.match(line):
            mask = m.group('mask')

        elif m := mem_set.match(line):
            address = int(m.group('address'))
            value = int(m.group('value'))

            for a in decode_address(mask, address):
                memory[a] = value

        else:
            raise RuntimeError

    print(sum(memory.values()))

def test():
    for address in decode_address('000000000000000000000000000000X1001X', 42):
        print(address, int(address, 2))
    for address in decode_address('00000000000000000000000000000000X0XX', 26):
        print(address, int(address, 2))

if __name__ == "__main__":
    main()
