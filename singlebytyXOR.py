import binascii

def single_byte_xor(hex_string):
    numbers = binascii.unhexlify(hex_string)
    key = max(numbers, key=numbers.count) ^ ord(' ')
    text=''.join(chr(number ^ key) for number in numbers)
    print(text)


# The given hex encoded strin
hexString = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

single_byte_xor(hexString)