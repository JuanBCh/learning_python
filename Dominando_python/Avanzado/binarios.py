bin_5 = 0b101
bin_10 = 0b1010

resultado_bin = bin_5 + bin_10

print(bin_5, bin_10, resultado_bin)
print(bin(resultado_bin))

bin_7 = "0b111"
bin_12 = "0b1100"

resultado_string = int(bin_7, 2) + int(bin_12, 2)
print(bin_7, bin_12, resultado_string)