def drawHangman(i):
    match i:
        case 0:
            return '\n\n\n\n\n\n=========='
        case 1:
            return '\n  |\n  |\n  |\n  |\n  |\n=========='
        case 2:
            return '  +---+\n  |\n  |\n  |\n  |\n  |\n=========='
        case 3:
            return '  +---+\n  |/\n  |\n  |\n  |\n  |\n=========='
        case 4:
            return '  +---+\n  |/  |\n  |\n  |\n  |\n  |\n=========='
        case 5:
            return '  +---+\n  |/  |\n  |   O\n  |\n  |\n  |\n=========='
        case 6:
            return '  +---+\n  |/  |\n  |   O\n  |   |\n  |\n  |\n=========='
        case 7:
            return '  +---+\n  |/  |\n  |   O\n  |   |\n  |  /\n  |\n=========='
        case 8:
            return '  +---+\n  |/  |\n  |   O\n  |   |\n  |  / \\\n  |\n=========='
        case 9:
            return '  +---+\n  |/  |\n  |   O\n  |  /|\n  |  / \\\n  |\n=========='
        case 10:
            return '  +---+\n  |/  |\n  |   O\n  |  /|\\\n  |  / \\\n  |\n=========='
        case _:
            "somebody fricked up while programming"