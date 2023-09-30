def fixed_xor(buffer1, buffer2):
    """Takes two byte-objects and returns their XOR combination as a byte-object"""
    return bytes([b1 ^ b2 for b1, b2 in zip(buffer1, buffer2)])

# Hex decode the input strings to get bytes objects
buffer1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
buffer2 = bytes.fromhex("686974207468652062756c6c277320657965")

# XOR the two buffers and then hex encode the result to get the final output
result = fixed_xor(buffer1, buffer2).hex()

print(result)  # This should print: 746865206b696420646f6e277420706c6179
