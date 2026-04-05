def xor_hex_string(hex_data, key):
    # Convert the hex string into bytes
    data_bytes = bytes.fromhex(hex_data)
    
    # Perform the XOR operation on each byte
    xor_result = bytes([b ^ key for b in data_bytes])
    
    return xor_result

# Input data
hex_input1 = "ffedf5acc5accdc1acc2c3d8acdfc9dedac5c2cbaccac3deacd5c3d9accdc2d5c1c3dec9"
hex_input2 = "eae3feebe9f8acede0e0acf8e4e9ace5e2fff8fef9eff8e5e3e2ffacede2e8acfef9e2acaefbe4e3ede1e5ae"
xor_key = 0x8C

# Execute transformation
result_bytes1 = xor_hex_string(hex_input1, xor_key)
result_bytes2 = xor_hex_string(hex_input2, xor_key)


# Output results
print(f"{result_bytes1.decode('utf-8', errors='ignore')}")
print(f"{result_bytes2.decode('utf-8', errors='ignore')}")
