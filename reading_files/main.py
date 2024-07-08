from os import strerror


try:
    binary_file = open('file.bin', 'rb')
    data = bytearray(binary_file.read(10))
    binary_file.close()

    for b in data:
        print(hex(b), end=' ')

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
