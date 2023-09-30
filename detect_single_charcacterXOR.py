import binascii

# Performs cryptanalysis on a file object, one of whose lines contains text encrypted using fixed_xor.
# Returns decrypted plaintext of that line.

def detect_single_character_xor(file_object):
  
    line_plaintexts = dict()
    # For each line in file, call single_byte_xor_cryptanalysis to return the most likely plaintext and its score
    for line in file_object.readlines():
        line = line.strip('\n')  # Get rid of newline at the end of our hexadecimal string
        line_bytes = binascii.unhexlify(line)
        likely_pt, _, score = single_byte_xor_cryptanalysis(line_bytes)
        line_plaintexts[likely_pt] = score
    return max(line_plaintexts, key=line_plaintexts.get)


def test_detect_single_character_xor():
    with open('set1_challenge4_ciphertext.txt') as file_obj:
        assert set1.detect_single_character_xor(file_obj) == b'Now that the party is jumping\n'