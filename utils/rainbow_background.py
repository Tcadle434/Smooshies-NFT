

class RainbowBackground:

    def __init__(self):
        print("created Generic Smooshy image")


    def get_raninbow_background(self, c1, c2, c3, c4, c5, c6):
        """
        :param bg: background color
        :param ol: outline color
        :param gc: green color
        :param rc: red color
        :return:
        """

        smooshy_background = [
            [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1],
            [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1],
            [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1],
            [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1],
            [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1],
            [c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1, c1],
            [c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2],
            [c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2],
            [c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2],
            [c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2],
            [c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2],
            [c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2],
            [c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2, c2],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4],
            [c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4],
            [c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4],
            [c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4],
            [c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4],
            [c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4],
            [c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4, c4],
            [c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5],
            [c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5],
            [c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5],
            [c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5],
            [c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5],
            [c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5],
            [c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5, c5],
            [c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6],
            [c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6],
            [c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6],
            [c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6],
            [c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6],
            [c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6, c6]
        ]

        return smooshy_background