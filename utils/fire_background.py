

class FireBackground:

    def __init__(self):
        print("created Generic Smooshy image")


    def get_smooshy_fire_background_1(self, bg, c1, c2, c3, c4):
        """
        :param bg: background color
        :param ol: outline color
        :param gc: green color
        :param rc: red color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, c1, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, c1, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, bg, c1, c1, bg, bg, bg, bg, bg, c1, c2, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, bg, bg, bg, c1, c1],
            [c1, c1, bg, c1, bg, bg, bg, c1, c1, c1, c1, bg, bg, bg, c1, c1, c2, c1, bg, bg, bg, c1, c2, c2, c2, c1, bg, c1, c2, c1, c1, bg, bg, bg, bg, bg, bg, c1, c2, c2],
            [c1, c2, c1, c1, bg, bg, bg, c1, c2, c1, c1, c1, bg, bg, c1, c1, c2, c2, c1, bg, bg, bg, c1, c2, c2, c1, c1, c2, c2, c2, c1, bg, bg, bg, bg, bg, c1, c1, c2, c2],
            [c1, c2, c1, c1, bg, bg, c1, c2, c2, c2, c2, c1, bg, bg, c1, c1, c3, c2, c1, bg, bg, bg, c1, c2, c2, c2, c2, c2, c2, c2, c1, bg, bg, bg, bg, bg, c1, c2, c2, c2],
            [c2, c2, c2, c2, c1, bg, c1, c2, c3, c2, c2, c1, bg, bg, c1, c2, c3, c2, c2, c1, bg, c1, c2, c2, c2, c2, c2, c2, c2, c2, c2, c1, bg, bg, bg, c1, c2, c2, c2, c3],
            [c2, c3, c2, c2, c1, c1, c2, c3, c3, c2, c1, c1, bg, bg, c1, c2, c3, c2, c2, c1, bg, c1, c2, c3, c3, c3, c1, c2, c3, c2, c2, c1, c1, c1, bg, bg, c1, c3, c3, c3],
            [c2, c3, c3, c2, c1, c2, c2, c3, c3, c3, c2, c1, c1, bg, c1, c2, c2, c3, c3, c1, c1, c1, c2, c3, c3, c2, c1, c1, c3, c3, c3, c1, c1, c1, c1, c1, c3, c3, c3, c3],
            [c2, c3, c2, c2, c2, c2, c3, c3, c3, c3, c2, c2, c1, c1, c2, c2, c2, c3, c3, c2, c1, c2, c2, c3, c3, c2, c2, c2, c3, c3, c3, c2, c2, c1, c2, c2, c3, c3, c3, c3],
            [c3, c3, c2, c2, c2, c3, c3, c3, c3, c2, c2, c2, c2, c2, c2, c2, c3, c3, c3, c3, c2, c2, c2, c3, c3, c2, c2, c2, c3, c3, c3, c2, c3, c2, c2, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c2, c2, c3, c3, c3, c3, c2, c2, c3, c3, c3, c2, c2, c3, c3, c3, c3, c2, c2, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3]
        ]

        return smooshy_background


    def get_smooshy_fire_background_2(self, bg, c1, c2, c3, c4):
        """
        :param bg: background color
        :param ol: outline color
        :param gc: green color
        :param rc: red color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, c1, bg, bg, bg, c1, bg, bg, bg, bg, bg, c1, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, c1, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, c1, bg, bg, bg, c1, bg, bg, bg, c1, bg, c1, c1, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, c1, bg, bg, bg, bg, c1, bg, c1, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, c1, bg, bg, c1, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, c1, bg, c1, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, bg, c1, c1, c1, c1, bg, c1, c1, c1, c1, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, c1, c1, c1, c1, c1, bg, bg, bg, c1, c1, c1, c1, c1, c1, bg, bg, bg, c1, c1, c1, bg, bg, c1, c1, c1, c2, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, c1, bg, bg, c1, bg, c1, c1, c1, c1, c1, c1, c1, bg, bg, c1, c1, c1, c1, bg, bg, bg, bg, c1, c1, c1, bg, bg, bg, c1, c1, c1, c2, c2, bg],
            [bg, bg, c1, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, c1, c1, c1, c1, bg, bg, bg, c1, c1, bg, c1, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, c1, c1, c2, c2, c2],
            [bg, bg, bg, bg, bg, bg, c1, c1, c1, c1, bg, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, bg, c1, c2, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, c1, c2, c2, c2],
            [c1, c1, bg, c1, bg, bg, bg, c1, c1, c1, c1, bg, bg, bg, c1, c1, c2, c1, bg, bg, bg, c1, c2, c2, c2, c1, bg, c1, c2, c1, c1, bg, bg, bg, bg, bg, c1, c1, c2, c2],
            [c1, c2, c1, c1, bg, bg, bg, c1, c2, c1, c1, c1, bg, bg, c1, c1, c2, c2, c1, bg, bg, bg, c1, c2, c2, c1, c1, c2, c2, c2, c1, bg, c1, bg, bg, bg, c1, c1, c2, c2],
            [c1, c2, c1, c1, bg, bg, c1, c2, c2, c2, c2, c1, bg, bg, c1, c1, c3, c2, c1, bg, bg, bg, c1, c2, c2, c2, c2, c2, c2, c2, c1, bg, bg, c1, c1, bg, c1, c2, c2, c2],
            [c2, c2, c2, c2, c1, bg, c1, c2, c3, c2, c2, c1, bg, bg, c1, c2, c3, c2, c2, c1, bg, c1, c2, c2, c2, c2, c2, c2, c2, c2, c2, c1, bg, c1, c1, c1, c2, c2, c2, c3],
            [c2, c3, c2, c2, c1, c1, c2, c3, c3, c2, c1, c1, bg, bg, c1, c2, c3, c2, c2, c1, bg, c1, c2, c3, c3, c3, c1, c2, c3, c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, c3],
            [c2, c3, c3, c2, c1, c2, c2, c3, c3, c3, c2, c1, c1, bg, c1, c2, c2, c3, c3, c1, c1, c1, c2, c3, c3, c2, c1, c1, c3, c3, c3, c1, c1, c1, c1, c1, c3, c3, c3, c3],
            [c2, c3, c2, c2, c2, c2, c3, c3, c3, c3, c2, c2, c1, c1, c2, c2, c2, c3, c3, c2, c1, c2, c2, c3, c3, c2, c2, c2, c3, c3, c3, c2, c2, c1, c2, c2, c4, c3, c3, c3],
            [c3, c3, c2, c2, c2, c3, c3, c3, c3, c2, c2, c2, c2, c2, c2, c2, c3, c3, c3, c3, c2, c2, c2, c3, c3, c2, c2, c2, c4, c3, c3, c2, c3, c2, c2, c3, c4, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c2, c2, c3, c3, c3, c3, c2, c2, c3, c3, c3, c2, c2, c3, c3, c3, c3, c2, c2, c3, c3, c3, c3, c4, c4, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c4, c3, c3, c3, c3, c3, c3, c3, c3, c4, c3, c3, c3, c3, c3, c3, c3, c3, c4, c4, c3, c4, c4, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c4, c4, c4, c3, c3, c3, c4, c3, c3, c4, c3, c4, c3, c3, c3, c3, c3, c3, c4, c3, c3, c3, c3, c3, c4, c3, c3, c3, c4, c3, c3, c3, c3, c3, c3, c3]
        ]

        return smooshy_background

    def get_smooshy_fire_background_3(self, bg, c1, c2, c3, c4):
        """
        :param bg: background color
        :param ol: outline color
        :param gc: green color
        :param rc: red color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, c1, bg, bg, bg, c1, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg],
            [bg, c1, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, c1, bg, c1, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, c1, bg, bg, bg, bg, c1, bg, c1, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg],
            [bg, c1, bg, c1, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, c1, bg, c1, bg, bg, bg, bg, c1, bg, bg, bg, bg, c1, c1, c1, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, c1, bg, bg, bg, bg, bg, c1, c1, c1, c1, bg, bg, bg, bg, c1, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, c1, c1, c1, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, bg, c1, c1, bg, bg, bg, bg, c1, c1, c2, c2, bg],
            [bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, bg, c1, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, c1, c2, c2, c2],
            [bg, bg, bg, bg, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, bg, c1, c2, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, c1, c2, c2, c2],
            [c1, c1, bg, c1, bg, bg, bg, c1, c1, c1, c1, bg, bg, bg, c1, c1, c2, c1, bg, bg, bg, c1, c2, c2, c2, c1, bg, c1, c2, c1, c1, bg, bg, bg, bg, bg, c1, c1, c2, c2],
            [c1, c2, c1, c1, bg, bg, bg, c1, c2, c1, c1, c1, bg, bg, c1, c1, c2, c2, c1, bg, bg, bg, c1, c2, c2, c1, c1, c2, c2, c2, c1, bg, c1, bg, bg, bg, c1, c1, c2, c2],
            [c1, c2, c1, c1, bg, bg, c1, c2, c2, c2, c2, c1, bg, bg, c1, c1, c3, c2, c1, bg, bg, bg, c1, c2, c2, c2, c2, c2, c2, c2, c1, bg, bg, c1, c1, bg, c1, c2, c2, c2],
            [c2, c2, c2, c2, c1, bg, c1, c2, c3, c2, c2, c1, bg, bg, c1, c2, c3, c2, c2, c1, bg, c1, c2, c2, c2, c2, c2, c2, c2, c2, c2, c1, bg, c1, c1, c1, c2, c2, c2, c3],
            [c2, c3, c2, c2, c1, c1, c2, c3, c3, c2, c1, c1, bg, bg, c1, c2, c3, c2, c2, c1, bg, c1, c2, c3, c3, c3, c1, c2, c3, c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, c3],
            [c2, c3, c3, c2, c1, c2, c2, c3, c3, c3, c2, c1, c1, bg, c1, c2, c2, c3, c3, c1, c1, c1, c2, c3, c3, c2, c1, c1, c3, c3, c3, c1, c1, c1, c1, c1, c3, c3, c3, c3],
            [c2, c3, c2, c2, c2, c2, c3, c3, c3, c3, c2, c2, c1, c1, c2, c2, c2, c3, c3, c2, c1, c2, c2, c3, c3, c2, c2, c2, c3, c3, c3, c2, c2, c1, c2, c2, c4, c3, c3, c3],
            [c3, c3, c2, c2, c2, c3, c3, c3, c3, c2, c2, c2, c2, c2, c2, c2, c3, c3, c3, c3, c2, c2, c2, c3, c3, c2, c2, c2, c4, c3, c3, c2, c3, c2, c2, c3, c4, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c2, c2, c3, c3, c3, c3, c2, c2, c3, c3, c3, c2, c2, c3, c3, c3, c3, c2, c2, c3, c3, c3, c3, c4, c4, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c4, c3, c3, c3, c3, c3, c3, c3, c3, c4, c3, c3, c3, c3, c3, c3, c3, c3, c4, c4, c3, c4, c4, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c4, c4, c4, c3, c3, c3, c4, c3, c3, c4, c3, c4, c3, c3, c3, c3, c3, c3, c4, c3, c3, c3, c3, c3, c4, c3, c3, c3, c4, c3, c3, c3, c3, c3, c3, c3]
        ]

        return smooshy_background


    def get_smooshy_fire_background_4(self, bg, c1, c2, c3, c4):
        """
        :param bg: background color
        :param ol: outline color
        :param gc: green color
        :param rc: red color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, c1, bg, bg, c1, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg],
            [bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, c1, c1, bg, bg, bg, bg, bg, bg, c1, c1, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, c1],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, c1, c1, c1, c1],
            [bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, c1, bg, bg, bg, c1, bg, bg, bg, bg, bg, c1, c1, c1, c1, bg, bg, bg, bg, bg, bg, bg, c1, c1, c1, c1, bg],
            [bg, c1, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, c1, bg, bg, c1, c1, c1, bg, bg, c1, c1, c1, c1, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, bg, bg],
            [bg, c1, bg, c1, bg, bg, bg, bg, bg, bg, c1, c1, bg, bg, bg, bg, c1, c1, c1, bg, bg, bg, c1, c1, c1, c1, bg, bg, bg, bg, c1, c1, c1, bg, bg, c1, c1, c1, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, c1, c1, c1, c1, c1, bg, bg, c1, c1, c1, c1, bg, bg, c1, c1, c1, c1, bg, bg, bg, bg, c1, c1, c1, bg, bg, c1, c1, c1, bg, bg, bg],
            [bg, bg, bg, bg, c1, c1, bg, bg, c1, c1, c1, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, bg, c1, c1, bg, bg, bg, bg, c1, c1, c2, c2, bg],
            [bg, bg, c1, c1, c1, c1, bg, c1, c1, c1, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, bg, c1, bg, bg, bg, bg, bg, c1, bg, bg, bg, bg, bg, bg, c1, c2, c2, c2],
            [c1, c1, c1, c1, c1, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, bg, c1, c2, c1, bg, bg, bg, c1, c1, c1, bg, bg, bg, bg, c1, c1, c2, c2, c2],
            [c1, c1, c1, c1, bg, bg, bg, c1, c1, c1, c1, bg, bg, bg, c1, c1, c2, c1, bg, bg, bg, c1, c2, c2, c2, c1, bg, c1, c2, c1, c1, bg, bg, bg, bg, bg, c1, c1, c2, c2],
            [c1, c2, c1, c1, bg, bg, bg, c1, c2, c1, c1, c1, bg, bg, c1, c1, c2, c2, c1, bg, bg, bg, c1, c2, c2, c1, c1, c2, c2, c2, c1, bg, c1, bg, bg, bg, c1, c1, c2, c2],
            [c1, c2, c1, c1, bg, bg, c1, c2, c2, c2, c2, c1, bg, bg, c1, c1, c3, c2, c1, bg, bg, bg, c1, c2, c2, c2, c2, c2, c2, c2, c1, bg, bg, c1, c1, bg, c1, c2, c2, c2],
            [c2, c2, c2, c2, c1, bg, c1, c2, c3, c2, c2, c1, bg, bg, c1, c2, c3, c2, c2, c1, bg, c1, c2, c2, c2, c2, c2, c2, c2, c2, c2, c1, bg, c1, c1, c1, c2, c2, c2, c3],
            [c2, c3, c2, c2, c1, c1, c2, c3, c3, c2, c1, c1, bg, bg, c1, c2, c3, c2, c2, c1, bg, c1, c2, c3, c3, c3, c1, c2, c3, c2, c2, c1, c1, c1, c1, c1, c1, c3, c3, c3],
            [c2, c3, c3, c2, c1, c2, c2, c3, c3, c3, c2, c1, c1, bg, c1, c2, c2, c3, c3, c1, c1, c1, c2, c3, c3, c2, c1, c1, c3, c3, c3, c1, c1, c1, c1, c1, c3, c3, c3, c4],
            [c2, c3, c2, c2, c2, c2, c3, c3, c3, c3, c4, c2, c1, c1, c2, c2, c2, c3, c3, c2, c1, c2, c2, c3, c3, c2, c2, c2, c3, c3, c3, c2, c2, c1, c2, c2, c4, c3, c4, c3],
            [c3, c3, c2, c2, c2, c3, c3, c3, c3, c2, c2, c2, c2, c2, c2, c2, c3, c3, c3, c3, c2, c2, c2, c3, c3, c2, c4, c2, c4, c3, c3, c2, c3, c2, c4, c3, c4, c3, c3, c3],
            [c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c2, c2, c3, c3, c3, c3, c2, c2, c3, c3, c3, c2, c2, c3, c3, c3, c3, c2, c2, c3, c3, c3, c3, c4, c4, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c4, c3, c3, c3, c3, c3, c3, c3, c3, c4, c3, c3, c3, c3, c3, c3, c3, c3, c4, c4, c3, c4, c4, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3, c3],
            [c3, c3, c3, c3, c4, c4, c4, c3, c3, c3, c4, c3, c3, c4, c3, c4, c3, c3, c3, c3, c3, c3, c4, c3, c3, c3, c3, c3, c4, c3, c3, c3, c4, c3, c3, c3, c3, c3, c3, c3]
        ]

        return smooshy_background