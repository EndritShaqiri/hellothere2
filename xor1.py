def xor_hex_string(hex_data, key):
    # Convert the hex string into bytes
    data_bytes = bytes.fromhex(hex_data)
    
    # Perform the XOR operation on each byte
    xor_result = bytes([b ^ key for b in data_bytes])
    
    return xor_result

# Input data
hex_input = "ffedf5acc5accdc1acc2c3d8acdfc9dedac5c2cbaccac3deacd5c3d9accdc2d5c1c3dec9"
xor_key = 0x8C

# Execute transformation
result_bytes = xor_hex_string(hex_input, xor_key)

# Output results
print(f"{result_bytes.decode('utf-8', errors='ignore')}")