

class WavySmooshy:

    def __init__(self):
        print("created Wavy Smooshy image")


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


    def get_smooshy_wavy_layer3(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_3 = [
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
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_3


    def get_smooshy_wavy_layer4(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_4 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_4


    def get_smooshy_wavy_layer5(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_5 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, ol, ol, ol, ol, ol, ol, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_5



    def get_smooshy_wavy_layer6(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_6 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, ol, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_6


    def get_smooshy_wavy_layer7(self, bg, ol, mc, sc, ec):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_7 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_7

    def get_smooshy_wavy_layer3_sunglasses(self, bg, ol, mc, sc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_3 = [
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
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_3

    def get_smooshy_wavy_layer4_sunglasses(self, bg, ol, mc, sc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_4 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_4

    def get_smooshy_wavy_layer5_sunglasses(self, bg, ol, mc, sc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_5 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, ol, ol, ol, ol, ol, ol, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_5

    def get_smooshy_wavy_layer6_sunglasses(self, bg, ol, mc, sc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_6 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, ol, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_6

    def get_smooshy_wavy_layer7_sunglasses(self, bg, ol, mc, sc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_7 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, mc, mc, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_7


    def get_smooshy_wavy_layer3_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_3 = [
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
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ec, lc, lc, lc, lc, lc, mc, mc, mc, ec, lc, lc, lc, lc, lc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_3



    def get_smooshy_wavy_layer4_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_4 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, ol, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, lc, lc, lc, lc, lc, mc, ec, mc, mc, lc, lc, lc, lc, lc, mc, mc, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_4


    def get_smooshy_wavy_layer5_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_5 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, mc, mc, mc, mc, mc, mc, ec, mc, mc, lc, lc, lc, lc, lc, mc, mc, lc, lc, lc, lc, lc, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, ol, ol, ol, ol, ol, ol, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_5



    def get_smooshy_wavy_layer6_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_6 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ec, lc, lc, lc, lc, lc, mc, mc, mc, ec, lc, lc, lc, lc, lc, mc, mc, mc, mc, ol, bg, lc, lc, lc, lc],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, ol, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, ol, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, ol, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_6


    def get_smooshy_wavy_layer7_laser(self, bg, ol, mc, sc, ec, lc):
        """
        :param bg: background color
        :param ol: outline color
        :param mc: main color
        :param sc: shadow color
        :return:
        """

        smooshy_generic_layer_7 = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, bg, bg, ol, mc, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, ol, bg, ol, mc, mc, mc, ol, ol, mc, mc, mc, mc, mc, mc, ol, bg, bg, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ec, lc, lc, mc, mc, mc, mc, mc, mc, ec, mc, mc, lc, lc, lc, lc, lc, mc, mc, lc, lc, lc, lc, lc, bg],
            [bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, mc, lc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, ol, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, ol, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, ol, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, mc, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, mc, mc, ol, ol, ol, ol, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, mc, mc, mc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, sc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg]
        ]

        return smooshy_generic_layer_7