hex_1997 = 0x7CD
hex_2023 = 0x7E7

resultado_int = hex_2023 - hex_1997
print(hex_1997, hex_2023, resultado_int)
print(hex(resultado_int))

hex_15 = "0xf"
hex_10 = "0xa"
resultado_str = int(hex_15, 16) + int(hex_10, 16)
print(resultado_str)
print(hex(resultado_str))