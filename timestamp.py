# why didn't i just do this in the demo itself? WHO KNOWS

def print_stamps(start, segment, length, stamps, segment_length, limit):
    for i in range(0, len(stamps)):
        stamp = start + (segment * length) + stamps[i]
        if stamp >= segment_length * limit:
            break

        print('{}, '.format(stamp), end='')


print('let timestamps = [')

segment_length = 32

# pattern 1

for i in range(0, segment_length):
    print('{}, '.format(i), end='')

# pattern 2

stamps = [ 0, 0.25, 0.75, 1.25, 1.5, 2, 2.25, 2.5 ]
start = segment_length
length = 2.75

print()

for i in range(0, 12):
    print_stamps(start, i, length, stamps, segment_length, 2)

# pattern 3

stamps = [ 0, 0.125, 0.375, 0.625, 0.875, 1.125, 1.25, 1.5 ]
start = segment_length * 2
length = 1.625

print()

for i in range(0, 20):
    print_stamps(start, i, length, stamps, segment_length, 3)

# pattern 4

stamps = [ 0, 1.625, 1.875, 2.125 ]
start = segment_length * 3
length = 2.25

print()

for i in range(0, 15):
    print_stamps(start, i, length, stamps, segment_length, 4)

print('\n]')
