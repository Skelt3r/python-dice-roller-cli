from random import randint

class DiceRoller():
    def run(self):
        self.start()
        while True:
            try:
                command = input('> ').lower().strip()

                if command.startswith('roll'):
                    self.interpret(command)
                elif command == 'stats':
                    self.roll_stats()
                elif command == 'help':
                    self.message('help')
                elif command == 'quit':
                    exit()
                else:
                    self.message('error')

            except (IndexError, ValueError):
                self.message('error')


    def roll_dice(self, num_sides, num_rolls):
        if num_rolls == 1:
            return randint(1, num_sides)
        elif num_rolls > 1:
            return [randint(1, num_sides) for _ in range(0, num_rolls)]
        else:
            self.message('error')


    def roll_stats(self):
        def stat_gen():
            rolls = sorted(self.roll_dice(6, 4))
            rolls.pop(0)
            return sum(rolls)

        print(f'\n  {sorted([stat_gen() for _ in range(0, 6)], reverse=True)}\n')


    def interpret(self, command):
        elements = command.split()
        roll = elements[1]
        nums = roll.split('d')
        num_rolls = int(nums[0])

        if nums[1].find('+') != -1:
            num_sides = int(nums[1].split('+')[0])
            mod = int(nums[1].split('+')[1])
        elif nums[1].find('-') != -1:
            num_sides = int(nums[1].split('-')[0])
            mod = -int(nums[1].split('-')[1])
        else:
            num_sides = int(nums[1])
            mod = 0

        rolls = self.roll_dice(num_sides, num_rolls)

        if num_rolls == 1:
                print(f'\n  Result: {rolls}\n' if mod == 0 else f'\n  Result: {rolls} + {mod}\n  Sum: {rolls + mod}\n')
        elif num_rolls > 1:
                print(f'\n  Results: {rolls}\n  Sum: {sum(rolls)}\n' if mod == 0 else f'\n  Results: {rolls} + {mod}\n  Sum: {sum(rolls) + mod}\n')


    def start(self):
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
        self.message('intro')


    def message(self, type):
        match type:
            case 'error':
                print('\n  Sorry, I didn\'t understand your input.'
                      '\n  Please try again or use the "help" command to review the syntax.\n')
            case 'help':
                print('\n  Use the "roll" command to roll any number/type of dice.\n'
                      '\n  Examples:\n    > roll 1d20\n    > roll 2d4+5\n    > roll 4d6-2\n'
                      '\n  Use the "stats" command to roll a set of 5e ability scores.\n')
            case 'intro':
                print('  Type "help" to learn the syntax.\n'
                      '  Type "quit" to close the program.\n')


if __name__ == "__main__":
    dice = DiceRoller()
    dice.run()
