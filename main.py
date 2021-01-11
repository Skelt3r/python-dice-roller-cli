# A simple command line dice roller

# Main program loop
def main():
    start()
    notes()

    while True:
        try:
            command = input('> ').lower().strip()

            if command.startswith('roll'):
                interpret(command)
            elif command == 'stats':
                roll_stats()
            elif command == 'help':
                help()
            elif command == 'quit':
                farewell()
            else:
                error()

        except (IndexError, ValueError):
            error()


# Roll any number of any type of dice
def roll_dice(num_sides, num_rolls):
    from random import randint

    if num_rolls == 1:
        return randint(1, num_sides)
    elif num_rolls > 1:
        return [randint(1, num_sides) for roll in range(0, num_rolls)]
    else:
        error()


# Roll for a set of 5e ability scores
def roll_stats():
    def stat_gen():
        rolls = sorted(roll_dice(6, 4))
        rolls.pop(0)
        return sum(rolls)

    print(f'\n  {sorted([stat_gen() for stat in range(0, 6)], reverse=True)}\n')


# Interpret user input when using the roll command
def interpret(command):
    # Dissect the command into useful parts
    parts = command.split()
    roll = parts[1]
    nums = roll.split('d')
    num_rolls = int(nums[0])

    # Check for modifiers
    if nums[1].find('+') != -1:
        num_sides = int(nums[1].split('+')[0])
        mod = int(nums[1].split('+')[1])
    elif nums[1].find('-') != -1:
        num_sides = int(nums[1].split('-')[0])
        mod = -int(nums[1].split('-')[1])
    else:
        num_sides = int(nums[1])
        mod = 0

    # Roll the dice
    rolls = roll_dice(num_sides, num_rolls)

    # Format and print a single roll
    if num_rolls == 1:
        if mod == 0:
            print(f'\n  Result: {rolls}\n')
        else:
            print(f'\n  Result: {rolls} + {mod}\n  Sum: {rolls + mod}\n')

    # Format and print multiple rolls
    elif num_rolls > 1:
        if mod == 0:
            print(f'\n  Results: {rolls}\n  Sum: {sum(rolls)}\n')
        else:
            print(f'\n  Results: {rolls} + {mod}\n  Sum: {sum(rolls) + mod}\n')


# Start screen
def start():
    print(r'''
          ________ 
          \______ \
           | |  \  |
           | |__'  |
          /_______/ I C E
                        
             by Skelt3r

      Press ENTER to continue
    ''')

    input()


# Opening notes
def notes():
    print('  Type "help" to learn the syntax.\n'
          '  Type "quit" to close the program.\n')


# Command syntax
def help():
    print('\n  Use the "roll" command to roll any number/type of dice.\n'
          '\n  Examples:\n    > roll 1d20\n    > roll 2d4+5\n    > roll 4d6-2\n'
          '\n  Use the "stats" command to roll a set of 5e ability scores.\n')


# Throw an error when entering an invalid command
def error():
    print('\n  Sorry, I didn\'t understand your input.'
          '\n  Please try again or use the "help" command to review the syntax.\n')


# A message to be displayed when closing the program
def farewell():
    exit('\n  Thanks for rolling. Farewell!\n')


# Python go brrrrr
if __name__ == "__main__":
    main()
