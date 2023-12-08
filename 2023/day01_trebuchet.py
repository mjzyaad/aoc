filename = './inputs/day01_trebuchet.in'

def part_one():
    with open(filename, 'r') as f:
        sum = 0
        for s in f.readlines():
            str_digits = ''.join(filter(str.isdigit, s))
            sum = sum + int(str_digits[0] + str_digits[-1])
        
        print('Answer to part 1 =', sum)


def part_two():
    digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    with open(filename, 'r') as f:
        sum = 0
        for s in f.readlines():
            s = s.strip()
            t = ""
            
            for i in range(len(s)):
                for j in range(1, 10):
                    if s.find(digits[j], i, i + len(digits[j])) >= 0:
                        t += str(j)
                    else:
                        t += s[i]

            str_digits = ''.join(filter(str.isdigit, t))
           
            sum = sum + int(str_digits[0] + str_digits[-1])
        
        print('Answer to part 2 =', sum)

if __name__ == '__main__':
    part_one()
    part_two()
