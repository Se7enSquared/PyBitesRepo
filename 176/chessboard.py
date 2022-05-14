WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for i in range(size):
        if i % 2 == 0:
            print(size//2 * (WHITE + BLACK))
        else:
            print(size//2 * (BLACK + WHITE))