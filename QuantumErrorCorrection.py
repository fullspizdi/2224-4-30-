```python
def apply_error_correction(data):
    """
    Applies quantum error correction codes to the data to ensure data integrity during quantum transmission.
    This function uses a simple repetition code for demonstration purposes.
    
    Parameters:
        data (bytes): The original data to be sent over the quantum network.
    
    Returns:
        bytes: The data encoded with quantum error correction codes.
    """
    # Convert data to binary representation for error correction processing
    binary_data = ''.join(format(byte, '08b') for byte in data)
    
    # Apply a simple repetition code (triplicate each bit for redundancy)
    corrected_binary_data = ''.join(bit * 3 for bit in binary_data)
    
    # Convert the corrected binary data back to bytes
    corrected_data = bytearray()
    for i in range(0, len(corrected_binary_data), 8):
        byte = corrected_binary_data[i:i+8]
        corrected_data.append(int(byte, 2))
    
    return bytes(corrected_data)

def decode_error_corrected_data(encoded_data):
    """
    Decodes the data that was encoded with quantum error correction codes.
    
    Parameters:
        encoded_data (bytes): The received data encoded with error correction codes.
    
    Returns:
        bytes: The original data after correcting errors and removing redundancy.
    """
    # Convert encoded data to binary representation
    binary_data = ''.join(format(byte, '08b') for byte in encoded_data)
    
    # Decode the data using majority voting for each set of three bits
    decoded_bits = []
    for i in range(0, len(binary_data), 3):
        triplet = binary_data[i:i+3]
        if triplet.count('1') > triplet.count('0'):
            decoded_bits.append('1')
        else:
            decoded_bits.append('0')
    
    # Convert the decoded binary data back to bytes
    decoded_data = bytearray()
    for i in range(0, len(decoded_bits), 8):
        byte = ''.join(decoded_bits[i:i+8])
        decoded_data.append(int(byte, 2))
    
    return bytes(decoded_data)
```
