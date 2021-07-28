

class RobotSmooshy:

    def __init__(self):
        print("created Robot Smooshy image")

    def get_boots(self, bg, ol, bc):

        smooshy_boots = [
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
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, ol, bg, bg, ol, bc, bc, bc, bc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bc, bc, bc, bc, bc, ol, bg, bg, ol, bc, bc, bc, bc, bc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, ol, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, ol, bc, bc, bc, ol, bg, bg, ol, bc, bc, bc, ol, bc, bc, bc, bc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, ol, ol, ol, ol, bg, bg, ol, ol, ol, ol, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_boots


    def get_ballcap(self, bg, ol, bc):

        smooshy_ballcap = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, bc, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg]
        ]

        return smooshy_ballcap


    def get_sunglasses(self, bg, ol, mc):

        smooshy_sunglasses = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_sunglasses


    def get_all_background(self, bg, ol, mc, sc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
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
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_background

    def get_smooshy_robot_layer3(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
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
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot


    def get_smooshy_robot_layer4(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
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
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot


    def get_smooshy_robot_layer5(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot

    def get_smooshy_robot_layer6(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot


    def get_smooshy_robot_layer7(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot

    def get_smooshy_robot_layer3_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
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
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, lc, lc, lc, lc, ol, ec, ec, lc, lc, lc, lc, lc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot

    def get_smooshy_robot_layer4_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
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
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, lc, lc, lc, lc, lc, ec, ol, ol, lc, lc, lc, lc, lc, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot

    def get_smooshy_robot_layer5_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, lc, lc, lc, lc, lc, ec, ol, lc, lc, lc, lc, lc, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot

    def get_smooshy_robot_layer6_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, lc, lc, lc, lc, ol, ec, ec, lc, lc, lc, lc, lc, ol, ec, ec, ol, bg, bg, lc, lc, lc, lc],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot

    def get_smooshy_robot_layer7_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_robot = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ec, ec, ec, ec, ec, ol, bg, bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, ol, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, ol, ol, ec, ec, ol, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, lc, ol, ol, ol, ol, ec, ec, lc, ol, ol, lc, lc, lc, lc, lc, ol, bg, lc, lc, lc, lc, lc],
            [bg, bg, bg, bg, bg, bg, ol, ec, ec, ol, mc, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, ol, ol, ec, ec, lc, ol, ol, ol, mc, ol, ec, ec, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_robot