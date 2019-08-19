from adafruit_binascii import hexlify, unhexlify, a2b_base64, b2a_base64

# Binary data.
data = b"CircuitPython is Awesome!"

# Get the hexadecimal representation of the binary data
hex_data = hexlify(data)
# Verify data
assert hex_data == b"43697263756974507974686f6e20697320417765736f6d6521", "hexlified data does not match expected data."

# Get the binary data represented by hex_data
bin_data = unhexlify(hex_data)
# Verify data
assert bin_data == data, "unhexlified binary data does not match original binary data."

# Convert binary data to a line of ASCII characters in base64 coding.
assert b2a_base64(b"Blinka") == b"Qmxpbmth\n", "Expected base64 coding does not match."

# Convert a block of base64 data back to binary data.
assert a2b_base64(b"Qmxpbmth\n") == b"Blinka", "Expected binary data does not match."