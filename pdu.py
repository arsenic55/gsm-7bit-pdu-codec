def pdu_encode(m):
    # bit buffer to store bits temporarily
    bit_buffer = 0
    bits_in_buffer = 0 # tracking bits in buffer
    result = [] # storing the bytes

    for char in m:
        # gets ASCII value of 7-bit
        val=ord(char) & 0x7F
        bit_buffer = bit_buffer | (val << bits_in_buffer) # shifting value

        # added 7bits in buffer
        bits_in_buffer += 7

        if bits_in_buffer >= 8:
            # Filter the lowest 8 bits as a complete byte
            result.append(bit_buffer & 0xFF)
            bit_buffer >>= 8
            bits_in_buffer -= 8 # Reduce bit count 
    # handle bits in buffer
    if bits_in_buffer > 0:
        result.append(bit_buffer & 0xFF)

    # Converting byte to hexadec string
    return ''.join(f'{byte:02x}' for byte in result)

def pdu_decode(encrypted_hex):
    # bit buffer to store bits temporarily
    bit_buffer = 0
    bits_in_buffer = 0 # tracking bits in buffer
    result = [] # storing the characters

    #converting hexa into a list of bytes
    bytes_list = bytes.fromhex(encrypted_hex)

    for byte in bytes_list:
        # shifting byte into position and add to buffer
        bit_buffer = bit_buffer | (byte << bits_in_buffer)
        bits_in_buffer += 8

        while bits_in_buffer >= 7:
            # extract lowest 7 bits as an complete character
            val = bit_buffer & 0x7F
            result.append(chr(val))
            bit_buffer >>= 7
            bits_in_buffer -= 7 # reducing bit count by 7
    # join character and strip null padding at end
    return ''.join(result).rstrip('\x00')

if __name__ == '__main__':
    encrypted_hex = pdu_encode('Welcome to applied cryptography!')
    decrypted_text = pdu_decode(encrypted_hex)
    print(encrypted_hex)
    print(decrypted_text)