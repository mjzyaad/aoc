filename = './inputs/day02_cube_conundrum.in'

def part_one():
    with open(filename, 'r') as f:
        answer = 0

        for s in f.readlines():
            s = s.strip()
            game, rounds = s.split(':')

            _ , game_number = game.split(' ')

            possible_game = True
            for round in rounds.split(';'):
                cubes = round.split(',')
                for colored_cube in cubes:
                    count, color = colored_cube.strip().split(' ')
                    color = color.strip()
                    
                    match color:
                        case 'red'   : possible_game = False if int(count) > 12 else possible_game
                        case 'green' : possible_game = False if int(count) > 13 else possible_game
                        case 'blue'  : possible_game = False if int(count) > 14 else possible_game
            
            if possible_game == True:
                answer += int(game_number)
                
        print('Answer to part 1 =', answer)


def part_two():
    with open(filename, 'r') as f:
        answer = 0

        for s in f.readlines():
            s = s.strip()
            _ , rounds = s.split(':')

            red_cubes   = 0
            green_cubes = 0
            blue_cubes  = 0
            for round in rounds.split(';'):
                cubes = round.split(',')
                for colored_cube in cubes:
                    count, color = colored_cube.strip().split(' ')
                    color = color.strip()
                    
                    match color:
                        case 'red'   : red_cubes   = max(red_cubes, int(count))
                        case 'green' : green_cubes = max(green_cubes, int(count))
                        case 'blue'  : blue_cubes  = max(blue_cubes, int(count))
            
            power = red_cubes * green_cubes * blue_cubes
            answer += power

        print('Answer to part 2 =', answer)


if __name__ == '__main__':
    part_one()
    part_two()
