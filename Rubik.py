class Rubik(object):

    global CUBE_STATE

    def __init__(self):
        self.input()

    def strHelper(self, start, finish):
        txt = ""
        for i in range(start, finish):
            txt += CUBE_STATE['red'][i] + "|"
        txt += " "
        for i in range(start, finish):
            txt += CUBE_STATE['blue'][i] + "|"
        txt += " "
        for i in range(start, finish):
            txt += CUBE_STATE['orange'][i] + "|"
        return txt

    # Produces a textual description of a state, with the faces of a cube unfolded into a 2-D representation.
    def __str__(self):
        txt = "          " + CUBE_STATE['white'][2] + "|" + \
        CUBE_STATE['white'][5] + "|" + CUBE_STATE['white'][8] + "|\n "
        txt += "         " + CUBE_STATE['white'][1] + "|" + \
        CUBE_STATE['white'][4] + "|" + CUBE_STATE['white'][7] + "|\n "
        txt += "         " + CUBE_STATE['white'][0] + "|" + \
        CUBE_STATE['white'][3] + "|" + CUBE_STATE['white'][6] + "|\n"
        for i in range(8, 5, -1):
            txt += CUBE_STATE['green'][i] + "|"
        txt += " " + self.strHelper(0, 3) + "\n"
        for i in range(5, 2, -1):
            txt += CUBE_STATE['green'][i] + "|"
        txt += " " + self.strHelper(3, 6) + "\n"
        for i in range(2, -1, -1):
            txt += CUBE_STATE['green'][i] + "|"
        txt += " " + self.strHelper(6, 9)
        for i in range(0, 3):
            txt += "\n          "
            txt += CUBE_STATE['yellow'][6 + i] + "|" + CUBE_STATE['yellow'][3 + i] + "|" \
                + CUBE_STATE['yellow'][0 + i] + "|"
        return txt

    def __hash__(self):
        return self.__str__().__hash__()

    # Performs an appropriately deep copy of a state,
    # for use by operators in creating new states.
    def copy(self):
        global CUBE_STATE
        newState = Rubik()
        newState.CUBE_STATE = [face[:] for face in self.CUBE_STATE]
        return newState

    # The user will locate the face of the cube where the center
    # cubie is the color specified, and input from left to right, top to
    # bottom) the colors of each cube on the face prompted.
    # The user should specify each color by their first letter.
    # Eg. 'white' denoted as 'w', 'red' as 'r', etc.
    def input(self):
        global CUBE_STATE
        print("INPUT: ")
        # white = input("White side: ").split()
        # red = input("Red side: ").split()
        # orange = input("Orange side: ").split()
        # blue = input("Blue side: ").split()
        # green = input("Green side: ").split()
        # yellow = input("Yellow side: ").split()
        CUBE_STATE = {
            'white': ['w0', 'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8'],
            'red': ['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8'],
            'orange': ['o0', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8'],
            'blue': ['b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'],
            'green': ['g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'],
            'yellow': ['y0', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8']
        }

    # This method will look at the face of the cube where the center cube is the
    # color specified, and then rotate it by 90 degrees clockwise.
    # A lot of this code is redundant.
    # TODO: Find a better way to clean this up.
    def rotate(self, color):
        global CUBE_STATE
        white = CUBE_STATE['white']
        green = CUBE_STATE['green']
        yellow = CUBE_STATE['yellow']
        blue = CUBE_STATE['blue']
        orange = CUBE_STATE['orange']
        red = CUBE_STATE['red']
        if color is 'red':
            tempA, tempB, tempC = white[0], white[3], white[6]
            for i in range(0, 9, 3):
                white[i] = green[i]
                green[i] = yellow[i]
                yellow[i] = blue[i]
            blue[0], blue[3], blue[6] = tempA, tempB, tempC
        elif color == 'orange':
            tempA, tempB, tempC = white[2], white[5], white[8]
            for i in range(2, 9, 3):
                white[i] = blue[i]
                blue[i] = yellow[i]
                yellow[i] = green[i]
            green[2], green[5], green[8] = tempA, tempB, tempC
        elif color == 'white':
            tempA, tempB, tempC = green[6], green[7], green[8]
            green[6], green[7], green[8] = red[2], red[1], red[0]
            red[0], red[1], red[2] = blue[0], blue[1], blue[2]
            blue[0], blue[1], blue[2] = orange[0], orange[1], orange[2]
            orange[0], orange[1], orange[2] = tempA, tempB, tempC
        temp = CUBE_STATE[color]
        CUBE_STATE[color] = [temp[6], temp[3], temp[0], temp[7], temp[4], temp[1], temp[8], temp[5], temp[2]]
        print(str(self))


if __name__ == "__main__":
    rubik = Rubik()
    rubik.rotate('white')


