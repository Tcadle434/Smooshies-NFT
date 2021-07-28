

class PunkSmooshy:

    def __init__(self):
        print("created Punk Smooshy image")

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


    def get_smooshy_punk_layer3(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
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

        return punk_layer


    def get_smooshy_punk_layer4(self, bg, ol, mc, sc, hc, ec, ew, fc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, ew, mc, mc, mc, mc, mc, mc, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, mc, mc, mc, mc, mc, ec, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer

    def get_smooshy_punk_layer5(self, bg, ol, mc, sc, hc, ec, ew, fc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, ew, mc, mc, mc, mc, mc, mc, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, mc, mc, mc, mc, mc, ec, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, fc, fc, fc, fc, fc, ol, ol, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, ol, ol, ol, ol, ol, bg, bg, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, mc, mc, ol, ol, mc, mc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, mc, ol, ol, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, sc, sc, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer


    def get_smooshy_punk_layer6(self, bg, ol, mc, sc, hc, ec, ew, fc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, ew, mc, mc, mc, mc, mc, mc, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, mc, mc, mc, mc, mc, ec, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, ol, bg, bg, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, mc, ol, bg, ol, mc, ol, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, mc, ol, ol, mc, mc, ol, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, bg, bg, bg, bg, bg, bg, bg, bg, mc, ol, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer

    def get_smooshy_punk_layer7(self, bg, ol, mc, sc, hc, ec, ew, fc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, ew, mc, mc, mc, mc, mc, mc, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, mc, mc, mc, mc, mc, ec, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, ol, ol, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, mc, mc, ol, ol, mc, mc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, mc, ol, ol, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, sc, sc, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer


    def get_smooshy_punk_layer4_cig(self, bg, ol, mc, sc, hc, ec, ew, fc, c1, c2):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, ew, mc, mc, mc, mc, mc, mc, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, mc, mc, mc, mc, mc, ec, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, c1, c1, c2, c2, c2, c2, c2, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer


    def get_smooshy_punk_layer5_cig(self, bg, ol, mc, sc, hc, ec, ew, fc, c1, c2, sm):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, ew, mc, mc, mc, mc, mc, mc, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, mc, mc, mc, mc, mc, ec, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, sm, sm, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, c1, c1, c2, c2, c2, c2, c2, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, fc, fc, fc, fc, fc, ol, ol, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, ol, ol, ol, ol, ol, bg, bg, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, mc, mc, ol, ol, mc, mc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, mc, ol, ol, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, sc, sc, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer


    def get_smooshy_punk_layer6_cig(self, bg, ol, mc, sc, hc, ec, ew, fc, c1, c2, sm):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, ew, mc, mc, mc, mc, mc, mc, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, mc, mc, mc, mc, mc, ec, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, sm, sm, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, c1, c1, c2, c2, c2, c2, c2, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, ol, bg, bg, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, mc, ol, bg, ol, mc, ol, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, mc, ol, ol, mc, mc, ol, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, bg, bg, bg, bg, bg, bg, bg, bg, mc, ol, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer

    def get_smooshy_punk_layer7_cig(self, bg, ol, mc, sc, hc, ec, ew, fc, c1, c2, sm):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, ew, mc, mc, mc, mc, mc, mc, ew, ew, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, mc, mc, mc, mc, mc, ec, ew, ol, bg, bg, bg, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, sm, sm, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, sm, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, c1, c1, c2, c2, c2, c2, c2, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, ol, ol, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, mc, mc, ol, ol, mc, mc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, mc, ol, ol, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, sc, sc, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer




    def get_smooshy_punk_layer3_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, ec, lc, lc, lc, lc, lc, mc, mc, mc, ec, lc, lc, lc, lc, lc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
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

        return punk_layer


    def get_smooshy_punk_layer4_laser(self, bg, ol, mc, sc, hc, ec, ew, fc, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, lc, mc, mc, mc, mc, mc, mc, ew, lc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, lc, lc, lc, lc, lc, ec, ew, ol, lc, lc, lc, lc, lc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, lc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer

    def get_smooshy_punk_layer5_laser(self, bg, ol, mc, sc, hc, ec, ew, fc, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, lc, mc, mc, mc, mc, mc, mc, ew, lc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, ew, mc, mc, mc, mc, mc, mc, ec, ew, ol, lc, lc, lc, lc, lc, bg, bg, lc, lc, lc, lc, lc, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, lc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, fc, fc, fc, fc, fc, ol, ol, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, ol, ol, ol, ol, ol, bg, bg, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, mc, mc, ol, ol, mc, mc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, mc, ol, ol, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, sc, sc, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer


    def get_smooshy_punk_layer6_laser(self, bg, ol, mc, sc, hc, ec, ew, fc, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, lc, mc, mc, mc, mc, mc, mc, ew, lc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, lc, lc, lc, lc, lc, mc, mc, ec, lc, lc, lc, lc, lc, bg, bg, bg, bg, bg, bg, bg, lc, lc, lc, lc],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, lc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, ol, bg, bg, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, mc, ol, bg, ol, mc, ol, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, ol, mc, mc, mc, mc, ol, ol, mc, mc, ol, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, bg, bg, bg, bg, bg, bg, bg, bg, mc, ol, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer

    def get_smooshy_punk_layer7_laser(self, bg, ol, mc, sc, hc, ec, ew, fc, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :param hc: hair color
        :param ec: eye color
        :param ew: eye white color
        :param fc: facial hair color
        :return:
        """

        punk_layer = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, bg, bg, hc, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, hc, bg, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, hc, hc, mc, mc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, hc, hc, hc, hc, mc, mc, mc, mc, hc, hc, hc, hc, hc, mc, mc, mc, mc, ol, bg, hc, hc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, fc, fc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ew, lc, mc, mc, mc, mc, mc, mc, ew, lc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ec, lc, lc, mc, mc, mc, mc, mc, ec, ew, ol, lc, lc, lc, lc, lc, bg, bg, lc, lc, lc, lc, lc, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, lc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, mc, mc, mc, mc, mc, mc, mc, mc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, mc, mc, mc, mc, mc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, fc, fc, fc, fc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, fc, fc, fc, ol, ol, ol, ol, ol, fc, fc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, ol, ol, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, mc, mc, ol, ol, mc, mc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, mc, ol, ol, mc, ol, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, ol, sc, sc, ol, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return punk_layer

