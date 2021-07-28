

class SmooshyLightningBackground:

    def __init__(self):
        print("created Generic Smooshy image")


    def get_smooshy_lightning_background_1(self, bg, ol, dc, gc, sc, mc, cc):
        """
        :param bg: background color
        :param ol: outline color
        :param dc: dirt color
        :param gc: grass color
        :param sc: sun color/lightning color
        :param mc: moon color
        :param cc: cloud color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg, bg, bg, sc, bg, bg, bg, sc, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg, bg, bg, bg, bg, sc, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, bg, sc, sc, sc, sc, sc, bg, sc, sc],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, sc, sc, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, sc, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg, bg, bg, bg, bg, sc, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg, bg, bg, sc, bg, bg, bg, sc, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg, bg, bg, bg, bg],
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
            [bg, bg, gc, bg, gc, gc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [gc, gc, gc, gc, bg, bg, bg, gc, bg, gc, bg, gc, gc, bg, bg, bg, bg, gc, gc, gc, gc, bg, bg, gc, bg, gc, bg, bg, gc, gc, bg, bg, gc, gc, bg, bg, bg, gc, gc, bg],
            [gc, bg, bg, gc, bg, gc, bg, gc, gc, gc, bg, gc, gc, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, bg, gc, bg],
            [gc, bg, bg, gc, bg, gc, gc, bg, bg, gc, bg, bg, gc, gc, bg, gc, gc, bg, bg, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc]
        ]

        return smooshy_background


    def get_smooshy_lightning_background_2(self, bg, ol, dc, gc, sc, mc, cc):
        """
        :param bg: background color
        :param ol: outline color
        :param dc: dirt color
        :param gc: grass color
        :param sc: sun color/lightning color
        :param mc: moon color
        :param cc: cloud color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, sc, bg, sc],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, sc, bg, bg],
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
            [bg, bg, gc, bg, gc, gc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [gc, gc, gc, gc, bg, bg, bg, gc, bg, gc, bg, gc, gc, bg, bg, bg, bg, gc, gc, gc, gc, bg, bg, gc, bg, gc, bg, bg, gc, gc, bg, bg, gc, gc, bg, bg, bg, gc, gc, bg],
            [gc, bg, bg, gc, bg, gc, bg, gc, gc, gc, bg, gc, gc, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, bg, gc, bg],
            [gc, bg, bg, gc, bg, gc, gc, bg, bg, gc, bg, bg, gc, gc, bg, gc, gc, bg, bg, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc]
        ]

        return smooshy_background


    def get_smooshy_lightning_background_3(self, bg, ol, dc, gc, sc, mc, cc):
        """
        :param bg: background color
        :param ol: outline color
        :param dc: dirt color
        :param gc: grass color
        :param sc: sun color/lightning color
        :param mc: moon color
        :param cc: cloud color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, ol],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, ol, ol, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
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
            [bg, bg, gc, bg, gc, gc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [gc, gc, gc, gc, bg, bg, bg, gc, bg, gc, bg, gc, gc, bg, bg, bg, bg, gc, gc, gc, gc, bg, bg, gc, bg, gc, bg, bg, gc, gc, bg, bg, gc, gc, bg, bg, bg, gc, gc, bg],
            [gc, bg, bg, gc, bg, gc, bg, gc, gc, gc, bg, gc, gc, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, bg, gc, bg],
            [gc, bg, bg, gc, bg, gc, gc, bg, bg, gc, bg, bg, gc, gc, bg, gc, gc, bg, bg, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc]
        ]

        return smooshy_background


    def get_smooshy_lightning_background_4(self, bg, ol, dc, gc, sc, mc, cc):
        """
        :param bg: background color
        :param ol: outline color
        :param dc: dirt color
        :param gc: grass color
        :param sc: sun color/lightning color
        :param mc: moon color
        :param cc: cloud color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg],
            [bg, bg, bg, ol, ol, ol, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg],
            [bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, ol],
            [bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg],
            [bg, bg, ol, ol, ol, cc, cc, cc, cc, cc, cc, ol, ol, ol, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, bg, bg, bg, ol, cc, cc, cc, ol, ol, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, ol, ol, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
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
            [bg, bg, gc, bg, gc, gc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [gc, gc, gc, gc, bg, bg, bg, gc, bg, gc, bg, gc, gc, bg, bg, bg, bg, gc, gc, gc, gc, bg, bg, gc, bg, gc, bg, bg, gc, gc, bg, bg, gc, gc, bg, bg, bg, gc, gc, bg],
            [gc, bg, bg, gc, bg, gc, bg, gc, gc, gc, bg, gc, gc, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, bg, gc, bg],
            [gc, bg, bg, gc, bg, gc, gc, bg, bg, gc, bg, bg, gc, gc, bg, gc, gc, bg, bg, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc]
        ]

        return smooshy_background


    def get_smooshy_lightning_background_5(self, bg, ol, dc, gc, sc, mc, cc):
        """
        :param bg: background color
        :param ol: outline color
        :param dc: dirt color
        :param gc: grass color
        :param sc: sun color/lightning color
        :param mc: moon color
        :param cc: cloud color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg],
            [bg, bg, bg, ol, ol, ol, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg],
            [bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, ol],
            [bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg],
            [bg, bg, ol, ol, ol, cc, cc, cc, cc, cc, cc, ol, ol, ol, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, ol, ol, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
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
            [bg, bg, gc, bg, gc, gc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [gc, gc, gc, gc, bg, bg, bg, gc, bg, gc, bg, gc, gc, bg, bg, bg, bg, gc, gc, gc, gc, bg, bg, gc, bg, gc, bg, bg, gc, gc, bg, bg, gc, gc, bg, bg, bg, gc, gc, bg],
            [gc, bg, bg, gc, bg, gc, bg, gc, gc, gc, bg, gc, gc, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, bg, gc, bg],
            [gc, bg, bg, gc, bg, gc, gc, bg, bg, gc, bg, bg, gc, gc, bg, gc, gc, bg, bg, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc]
        ]

        return smooshy_background


    def get_smooshy_lightning_background_6(self, bg, ol, dc, gc, sc, mc, cc):
        """
        :param bg: background color
        :param ol: outline color
        :param dc: dirt color
        :param gc: grass color
        :param sc: sun color/lightning color
        :param mc: moon color
        :param cc: cloud color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg],
            [bg, bg, bg, ol, ol, ol, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg],
            [bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, ol],
            [bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg],
            [bg, bg, ol, ol, ol, cc, cc, cc, cc, cc, cc, ol, ol, ol, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, ol, ol, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, ol, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, ol, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, gc, bg, gc, gc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [gc, gc, gc, gc, bg, bg, bg, gc, bg, gc, bg, gc, gc, bg, bg, bg, bg, gc, gc, gc, gc, bg, bg, gc, bg, gc, bg, bg, gc, gc, bg, bg, gc, gc, bg, bg, bg, gc, gc, bg],
            [gc, bg, bg, gc, bg, gc, bg, gc, gc, gc, bg, gc, gc, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, bg, gc, bg],
            [gc, bg, bg, gc, bg, gc, gc, bg, bg, gc, bg, bg, gc, gc, bg, gc, gc, bg, bg, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc]
        ]

        return smooshy_background

    def get_smooshy_lightning_background_7(self, bg, ol, dc, gc, sc, mc, cc):
        """
        :param bg: background color
        :param ol: outline color
        :param dc: dirt color
        :param gc: grass color
        :param sc: sun color/lightning color
        :param mc: moon color
        :param cc: cloud color
        :return:
        """

        smooshy_background = [
            [bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg, bg],
            [bg, bg, bg, ol, ol, ol, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol, bg],
            [bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, ol, bg],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, mc, mc, mc, mc, mc, ol],
            [ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, ol],
            [bg, ol, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, ol, bg],
            [bg, bg, ol, ol, ol, cc, cc, cc, cc, cc, cc, ol, ol, ol, cc, cc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, mc, mc, mc, ol, bg, bg],
            [bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, ol, bg, bg, bg, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, mc, mc, mc, mc, mc, ol, ol, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, ol, ol, ol, ol, ol, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [bg, bg, bg, bg, ol, sc, sc, sc, ol, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
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
            [bg, bg, gc, bg, gc, gc, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg, bg],
            [gc, gc, gc, gc, bg, bg, bg, gc, bg, gc, bg, gc, gc, bg, bg, bg, bg, gc, gc, gc, gc, bg, bg, gc, bg, gc, bg, bg, gc, gc, bg, bg, gc, gc, bg, bg, bg, gc, gc, bg],
            [gc, bg, bg, gc, bg, gc, bg, gc, gc, gc, bg, gc, gc, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, bg, gc, bg],
            [gc, bg, bg, gc, bg, gc, gc, bg, bg, gc, bg, bg, gc, gc, bg, gc, gc, bg, bg, bg, gc, gc, gc, gc, gc, bg, gc, gc, bg, gc, gc, gc, gc, gc, bg, gc, bg, gc, bg, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc, gc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc],
            [dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc, dc]
        ]

        return smooshy_background