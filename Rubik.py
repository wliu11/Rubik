class Rubik(object):

    global CUBE_STATE
    CUBE_STATE = []

    def __init__(self):
        self.CUBE_STATE = CUBE_STATE

    def __eq__(self, other):
        if isinstance(other, Rubik):
            for face in CUBE_STATE:
                if self.CUBE_STATE[face] != other.CUBE_STATE[face]:
                    return False
            return True
        return False

    def strHelper(self, start, finish):
        txt = " "
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
        txt = "       " + CUBE_STATE['white'][2] + "|" + \
        CUBE_STATE['white'][5] + "|" + CUBE_STATE['white'][8] + "|\n "
        txt += "      " + CUBE_STATE['white'][1] + "|" + \
        CUBE_STATE['white'][4] + "|" + CUBE_STATE['white'][7] + "|\n "
        txt += "      " + CUBE_STATE['white'][0] + "|" + \
        CUBE_STATE['white'][3] + "|" + CUBE_STATE['white'][6] + "|\n"
        for i in range(8, 5, -1):
            txt += CUBE_STATE['green'][i] + "|"
        txt += "" + self.strHelper(0, 3) + "\n"
        for i in range(5, 2, -1):
            txt += CUBE_STATE['green'][i] + "|"
        txt += "" + self.strHelper(3, 6) + "\n"
        for i in range(2, -1, -1):
            txt += CUBE_STATE['green'][i] + "|"
        txt += "" + self.strHelper(6, 9)
        for i in range(0, 3):
            txt += "\n       "
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
        newState.CUBE_STATE = self.CUBE_STATE
        return newState

    # The user will locate the face of the cube where the center
    # cubie is the color specified, and input from left to right, top to
    # bottom) the colors of each cube on the face prompted.
    # The user should specify each color by their first letter.
    # See documentation for which orientation to input colors for each face.
    # Eg. 'white' denoted as 'w', 'red' as 'r', etc.
    def input(self):
        global CUBE_STATE
        print("INPUT: ")
        # CUBE_STATE = {
        #     'red': input("Red side: ").split(),
        #     'white': input("White side: ").split(),
        #     'orange': input("Orange side: ").split(),
        #     'blue': input("Blue side: ").split(),
        #     'green': input("Green side: ").split(),
        #     'yellow': input("Yellow side: ").split()
        # }
        # CUBE_STATE = {
        #     'white': ['w0', 'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8'],
        #     'red': ['r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8'],
        #     'orange': ['o0', 'o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8'],
        #     'blue': ['b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8'],
        #     'green': ['g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8'],
        #     'yellow': ['y0', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8']
        # }
        CUBE_STATE = {
            'white': ['g', 'b', 'w', 'w', 'w', 'y', 'r', 'b', 'w'],
            'red': ['y', 'g', 'b', 'w', 'r', 'g', 'y', 'r', 'r'],
            'orange': ['r', 'g', 'o', 'y', 'o', 'b', 'g', 'r', 'w'],
            'blue': ['w', 'r', 'g', 'r', 'b', 'o', 'b', 'g', 'y'],
            'green': ['o', 'b', 'o', 'o', 'g', 'y', 'o', 'w', 'g'],
            'yellow': ['y', 'o', 'r', 'y', 'y', 'w', 'b', 'o', 'b']
        }

    # This method will look at the face of the cube where the center cube is the
    # color specified, and then rotate it by 90 degrees clockwise.
    # A lot of this code is redundant.
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
        elif color is 'orange':
            tempA, tempB, tempC = white[2], white[5], white[8]
            for i in range(2, 9, 3):
                white[i] = blue[i]
                blue[i] = yellow[i]
                yellow[i] = green[i]
            green[2], green[5], green[8] = tempA, tempB, tempC
        elif color is 'white':
            temp = [green[6], green[7], green[8]]
            green[6], green[7], green[8] = red[2], red[1], red[0]
            for i in range(3):
                red[i] = blue[i]
                blue[i] = orange[i]
            orange[0], orange[1], orange[2] = temp[2], temp[1], temp[0]
        elif color is 'green':
            tempA, tempB, tempC = red[0], red[3], red[6]
            red[0], red[3], red[6] = white[2], white[1], white[0]
            white[0], white[1], white[2] = orange[2], orange[5], orange[8]
            orange[2], orange[5], orange[8] = yellow[6], yellow[7], yellow[8]
            yellow[6], yellow[7], yellow[8] = tempA, tempB, tempC
        elif color is 'blue':
            tempA, tempB, tempC = orange[0], orange[3], orange[6]
            orange[0], orange[3], orange[6] = white[6], white[7], white[8]
            white[6], white[7], white[8] = red[8], red[5], red[2]
            red[2], red[5], red[8] = yellow[0], yellow[1], yellow[2]
            yellow[0], yellow[1], yellow[2] = tempC, tempB, tempA
        elif color is 'yellow':
            tempA, tempB, tempC = blue[6], blue[7], blue[8]
            blue[6], blue[7], blue[8] = red[6], red[7], red[8]
            red[6], red[7], red[8] = green[0], green[1], green[2]
            green[0], green[1], green[2] = orange[8], orange[7], orange[6]
            orange[6], orange[7], orange[8] = tempA, tempB, tempC
        temp = CUBE_STATE[color]
        CUBE_STATE[color] = [temp[6], temp[3], temp[0], temp[7], temp[4], temp[1],
                             temp[8], temp[5], temp[2]]
        print(self)
        return CUBE_STATE


# If all the values are in order, then CUBE_STATE is a goal state.
def goal_test(r):
    return r.CUBE_STATE == {'white': ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
                            'red': ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'],
                            'orange': ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
                            'blue': ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
                            'green': ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'],
                            'yellow': ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
                            }


if __name__ == "__main__":
    rubik = Rubik()
    rubik.input()
    print(rubik)


