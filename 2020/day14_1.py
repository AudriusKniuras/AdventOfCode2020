f = open("input.txt", "r")

input = [x for x in f.read().split('\n')]

f.close()

results = {}

def apply_mask(mask, dec_value):
    bin_value = bin(dec_value).split('0b')[1]
    bits_added = 36 - len(bin_value)
    bin_value = "0" * bits_added + bin_value
    for index, bit in enumerate(mask):
        if bit != "X":
            bin_value = bin_value[:index] + bit + bin_value[index+1:]
    return int(bin_value, 2)

for line in input:
    if "mask" in line:
        mask = line.split(' ')[2]
    elif "mem"in line:
        mem = int(line.split('[')[1].split(']')[0])
        dec_value = int(line.split('=')[1].strip())
        dec_value_masked = apply_mask(mask, dec_value)

        results[mem] = dec_value_masked

print(results)

answer = 0
for value in results.values():
    answer += value

print(answer)