from PIL import Image
from PIL import ImageColor
import numpy as np
import os
from random import seed
from random import randint
import json

from utils.smooshy_generic import GenericSmooshy
from utils.smooshy_wavy import WavySmooshy
from utils.smooshy_alien import AlienSmooshy
from utils.smooshy_robot import RobotSmooshy
from utils.smooshy_monkey import MonkeySmooshy
from utils.smooshy_punk import PunkSmooshy

from utils.candle_chart_background import SmooshyChartBackground
from utils.rainbow_background import RainbowBackground
from utils.space_background import SpaceBackground
from utils.fire_background import FireBackground
from utils.lightning_animated_background import SmooshyLightningBackground


dirname = str(r"C:\Users\thoma\Documents\Blog\TopShot and NFTs\Smooshies\Smooshies_App")

smooshy_generic_object = GenericSmooshy()
smooshy_wavy_object = WavySmooshy()
smooshy_alien_object = AlienSmooshy()
smooshy_robot_object = RobotSmooshy()
smooshy_monkey_object = MonkeySmooshy()
smooshy_punk_object = PunkSmooshy()

smooshy_chart_background_object = SmooshyChartBackground()
smooshy_rainbow_background_object = RainbowBackground()
smooshy_space_background_object = SpaceBackground()
smooshy_fire_background_object = FireBackground()
smooshy_lightning_background_object = SmooshyLightningBackground()



dimensions = 400, 400


def create_gif_from_images(image_list, filenumber):
    image_list[0].save(dirname + '/smooshy-gifs/' + str(filenumber) + '.gif', save_all=True, append_images=image_list[1:], optimize=False, duration=[500,100,100,100,200,500,200,100,100,100], loop=0)

def create_background_from_images(image_list, filenumber):
    image_list[0].save(dirname + '/smooshy-backgrounds/' + str(filenumber) + '.gif', save_all=True, append_images=image_list[1:], optimize=False, duration=[500,100,100,100,200,500,200,100,100,100], loop=0)

def create_metadata_file(attributes, filenumber):
    metadata = create_metadata_object(attributes, filenumber)
    with open(dirname + '/metadata/' + str(filenumber) +'.json', 'w') as f:
        json.dump(metadata, f, indent=2)
        # print("New json file is created from data.json file")


def create_metadata_object(attributes, filenumber):
    metadata = {}
    name = "Smooshie #" + str(filenumber)
    metadata["name"] = name
    metadata["description"] = name + " is one of 10,000 randomly generated Smooshies stored on the Ethereum Blockchain. What will this loveable blob morph into?"
    metadata["image"] = ""
    metadata["external_url"] = "https://smooshies.io/"
    metadata["attributes"] = attributes

    return metadata


def add_boots(smooshy_object, layer, bg, ol, bc):
    #bc is boot color

    # a = randint(0,100)
    #
    # # 50% brown
    # if a > 50:
    #     bc = (165, 42, 42)
    #
    # # 30% black
    # elif 50 >= a > 20:
    #     bc = (0, 0, 0)
    #
    # # 20% gold
    # else:
    #     bc = (204,172,0)

    boot_layer = smooshy_object.get_boots(bg, ol, bc)
    layer[33:] = boot_layer[33:]

    return layer


def add_ballcap(smooshy_object, bg, ol, hc):
    #hc hat color

    ballcap_layer = smooshy_object.get_ballcap(bg, ol, hc)

    return ballcap_layer


def add_sunglasses(smooshy_object, bg, ol, mc):

    sunglasses_layer = smooshy_object.get_sunglasses(bg, ol, mc)

    return sunglasses_layer


def add_halo(smooshy_object, bg, ol, mc):
    halo_layer = smooshy_object.get_halo(bg, ol, mc)

    return halo_layer


def add_background(background_layer, image_layer):
    i = 0
    for row in image_layer:
        j = 0
        for pixel in row:
            if pixel == (238, 238, 238):
                image_layer[i][j] = background_layer[i][j]

            j = j + 1
        i = i + 1

    return image_layer


def main_color_picker(rand):
    color_list = []
    if rand > 50:
        mc = (randint(0, 256), randint(0, 256), randint(0, 256))

        color_list.append(mc)
        color_list.append(mc)
        color_list.append(mc)
        color_list.append(mc)
        color_list.append(mc)
        color_list.append(mc)
        color_list.append(mc)

        trait_type = "Solid"

    else:
        color_list.append((randint(0, 256), randint(0, 256), randint(0, 256)))
        color_list.append((randint(0, 256), randint(0, 256), randint(0, 256)))
        color_list.append((randint(0, 256), randint(0, 256), randint(0, 256)))
        color_list.append((randint(0, 256), randint(0, 256), randint(0, 256)))
        color_list.append((randint(0, 256), randint(0, 256), randint(0, 256)))
        color_list.append((randint(0, 256), randint(0, 256), randint(0, 256)))
        color_list.append((randint(0, 256), randint(0, 256), randint(0, 256)))

        trait_type = "Flashy"

    return color_list, trait_type

def eye_picker(rand):
    #Normal Black
    if rand > 100:
        ec1 = (0, 0, 0)
        ec2 = (0, 0, 0)
        ec3 = (0, 0, 0)
        ec4 = (0, 0, 0)
        ec5 = (0, 0, 0)
        ec6 = (0, 0, 0)
        ec7 = (0, 0, 0)

        trait_type = "Normal"
    # Red
    elif 100 >= rand > 30:
        ec1 = (255, 0, 0)
        ec2 = (255, 0, 0)
        ec3 = (255, 0, 0)
        ec4 = (255, 0, 0)
        ec5 = (255, 0, 0)
        ec6 = (255, 0, 0)
        ec7 = (255, 0, 0)

        trait_type = "Red"
    # flashing
    elif 30 >= rand > 0:
        ec1 = (randint(0, 256), randint(0, 256), randint(0, 256))
        ec2 = (randint(0, 256), randint(0, 256), randint(0, 256))
        ec3 = (randint(0, 256), randint(0, 256), randint(0, 256))
        ec4 = (randint(0, 256), randint(0, 256), randint(0, 256))
        ec5 = (randint(0, 256), randint(0, 256), randint(0, 256))
        ec6 = (randint(0, 256), randint(0, 256), randint(0, 256))
        ec7 = (randint(0, 256), randint(0, 256), randint(0, 256))

        trait_type = "Flashing"

    eye_list.append(ec1)
    eye_list.append(ec2)
    eye_list.append(ec3)
    eye_list.append(ec4)
    eye_list.append(ec5)
    eye_list.append(ec6)
    eye_list.append(ec7)

    return eye_list, trait_type

def background_picker(rand):
    background_indicator = False
    background_list = []
    sc = (128, 128, 128)
    bg = (238, 238, 238)
    trait_type = "Light Grey"

    # 50% chance no special background is used
    if rand > 500:
        background_indicator = False
        # if rand > 600:
        a = randint(0, 256)
        b = randint(0, 256)
        c = randint(0, 256)

        bg = (a, b, c)

        if (a - 25) > 0 and (b - 25) > 0 and (c - 25) > 0:
            sc = (a-25, b-25, c-25)
        else:
            sc = (0, 0, 0)

        trait_type = "Solid Color"

    # 5% candle chart
    elif 500 >= rand > 450:
        background_indicator = True
        background1 = get_smooshy_chart_background(smooshy_chart_background_object, ol)
        background2 = get_smooshy_chart_background(smooshy_chart_background_object, ol)
        background3 = get_smooshy_chart_background(smooshy_chart_background_object, ol)
        background4 = get_smooshy_chart_background(smooshy_chart_background_object, ol)
        background5 = get_smooshy_chart_background(smooshy_chart_background_object, ol)
        background6 = get_smooshy_chart_background(smooshy_chart_background_object, ol)
        background7 = get_smooshy_chart_background(smooshy_chart_background_object, ol)

        background_list.append(background1)
        background_list.append(background2)
        background_list.append(background3)
        background_list.append(background4)
        background_list.append(background5)
        background_list.append(background6)
        background_list.append(background7)

        trait_type = "Candlestick Chart"

    # 5% rainbow background
    elif 450 >= rand > 400:
        background_indicator = True
        background1 = get_smooshy_rainbow_background(smooshy_rainbow_background_object)
        background2 = get_smooshy_rainbow_background(smooshy_rainbow_background_object)
        background3 = get_smooshy_rainbow_background(smooshy_rainbow_background_object)
        background4 = get_smooshy_rainbow_background(smooshy_rainbow_background_object)
        background5 = get_smooshy_rainbow_background(smooshy_rainbow_background_object)
        background6 = get_smooshy_rainbow_background(smooshy_rainbow_background_object)
        background7 = get_smooshy_rainbow_background(smooshy_rainbow_background_object)

        background_list.append(background1)
        background_list.append(background2)
        background_list.append(background3)
        background_list.append(background4)
        background_list.append(background5)
        background_list.append(background6)
        background_list.append(background7)

        sc = (0,0,0)

        trait_type = "Rainbow"

    # 5% space background
    elif 400 >= rand > 350:
        background_indicator = True
        space_list = get_smooshy_space_background(smooshy_space_background_object)
        background1 = space_list[0]
        background2 = space_list[1]
        background3 = space_list[2]
        background4 = space_list[3]
        background5 = space_list[4]
        background6 = space_list[5]
        background7 = space_list[6]

        background_list.append(background1)
        background_list.append(background2)
        background_list.append(background3)
        background_list.append(background4)
        background_list.append(background5)
        background_list.append(background6)
        background_list.append(background7)

        sc = (0, 0, 139)

        trait_type = "Outer Space"

    # 5% fire background
    elif 350 >= rand > 300:
        background_indicator = True
        fire_list = get_smooshy_fire_background(smooshy_fire_background_object)
        background1 = fire_list[0]
        background2 = fire_list[1]
        background3 = fire_list[2]
        background4 = fire_list[3]
        background5 = fire_list[2]
        background6 = fire_list[1]
        background7 = fire_list[0]

        background_list.append(background1)
        background_list.append(background2)
        background_list.append(background3)
        background_list.append(background4)
        background_list.append(background5)
        background_list.append(background6)
        background_list.append(background7)

        sc = (0, 0, 0)

        trait_type = "Hellfire"

    #5% animated lightning background
    elif 300 >= rand > 250:
        background_indicator = True
        lightning_list = get_smooshy_animated_lightning_background(smooshy_lightning_background_object)
        background1 = lightning_list[0]
        background2 = lightning_list[1]
        background3 = lightning_list[2]
        background4 = lightning_list[3]
        background5 = lightning_list[4]
        background6 = lightning_list[5]
        background7 = lightning_list[6]

        background_list.append(background1)
        background_list.append(background2)
        background_list.append(background3)
        background_list.append(background4)
        background_list.append(background5)
        background_list.append(background6)
        background_list.append(background7)

        sc = (0, 0, 0)

        trait_type = "Lightning"

    # 5% sunny background
    elif 250 >= rand > 200:
        background_indicator = True
        background1 = get_smooshy_sunny_background(smooshy_lightning_background_object)
        background2 = get_smooshy_sunny_background(smooshy_lightning_background_object)
        background3 = get_smooshy_sunny_background(smooshy_lightning_background_object)
        background4 = get_smooshy_sunny_background(smooshy_lightning_background_object)
        background5 = get_smooshy_sunny_background(smooshy_lightning_background_object)
        background6 = get_smooshy_sunny_background(smooshy_lightning_background_object)
        background7 = get_smooshy_sunny_background(smooshy_lightning_background_object)

        background_list.append(background1)
        background_list.append(background2)
        background_list.append(background3)
        background_list.append(background4)
        background_list.append(background5)
        background_list.append(background6)
        background_list.append(background7)

        sc = (0, 0, 0)

        trait_type = "Sunny Day"


    return background_indicator, background_list, sc, bg, trait_type

def boot_color_picker(rand):

    # 50% brown
    if rand > 500:
        bc = (165, 42, 42)
        trait_type = "Solid Brown"

    # 30% black
    elif 500 >= rand > 200:
        bc = (0, 0, 0)
        trait_type = "Solid Black"

    # 20% gold
    else:
        bc = (204,172,0)
        trait_type = "Solid Gold"

    return bc, trait_type

def generate_basic_smooshies(smooshy_object, background_flag, background_layers, num, bg, ol, mc, sc, boots, sunglasses, hat, halo, laser_eyes, eyes, attributes_list):
    image_list = []
    attributes_dict5 = {}
    attributes_dict6 = {}
    attributes_dict7 = {}

    attributes_dict5["trait_type"] = "Eyes"
    attributes_dict5["value"] = "Regular"

    if sunglasses is True:
        l1 = smooshy_object.get_smooshy_generic_base_sunglasses(bg, ol, mc[0], sc)
        l2 = smooshy_object.get_smooshy_generic_layer_2_sunglasses(bg, ol, mc[1], sc)
        l3 = smooshy_object.get_smooshy_generic_layer_3_sunglasses(bg, ol, mc[2], sc)
        l4 = smooshy_object.get_smooshy_generic_layer_4_sunglasses(bg, ol, mc[3], sc)
        l5 = smooshy_object.get_smooshy_generic_layer_5_sunglasses(bg, ol, mc[4], sc)
        l6 = smooshy_object.get_smooshy_generic_layer_6_sunglasses(bg, ol, mc[5], sc)
        l7 = smooshy_object.get_smooshy_generic_layer_7_sunglasses(bg, ol, mc[6], sc)

        attributes_dict5["value"] = "Sunglasses"

    elif laser_eyes is True:
        if randint(1,1000) > 200:
            attributes_dict5["value"] = "Red Laser Eyes"
            lc = (255, 0, 0)
        else:
            attributes_dict5["value"] = "Green Laser Eyes"
            lc = (0, 128, 0)
        l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
        l2 = smooshy_object.get_smooshy_generic_layer_2_laser(bg, ol, mc[1], sc, eyes[1], lc)
        l3 = smooshy_object.get_smooshy_generic_layer_3_laser(bg, ol, mc[2], sc, eyes[2], lc)
        l4 = smooshy_object.get_smooshy_generic_layer_4_laser(bg, ol, mc[3], sc, eyes[3], lc)
        l5 = smooshy_object.get_smooshy_generic_layer_5_laser(bg, ol, mc[4], sc, eyes[4], lc)
        l6 = smooshy_object.get_smooshy_generic_layer_6_laser(bg, ol, mc[5], sc, eyes[5], lc)
        l7 = smooshy_object.get_smooshy_generic_layer_7_laser(bg, ol, mc[6], sc, eyes[6], lc)

    else:
        l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
        l2 = smooshy_object.get_smooshy_generic_layer_2(bg, ol, mc[1], sc, eyes[1])
        l3 = smooshy_object.get_smooshy_generic_layer_3(bg, ol, mc[2], sc, eyes[2])
        l4 = smooshy_object.get_smooshy_generic_layer_4(bg, ol, mc[3], sc, eyes[3])
        l5 = smooshy_object.get_smooshy_generic_layer_5(bg, ol, mc[4], sc, eyes[4])
        l6 = smooshy_object.get_smooshy_generic_layer_6(bg, ol, mc[5], sc, eyes[5])
        l7 = smooshy_object.get_smooshy_generic_layer_7(bg, ol, mc[6], sc, eyes[6])

    attributes_list.append(attributes_dict5)

    attributes_dict6["trait_type"] = "Boots"
    attributes_dict6["value"] = "None"
    if boots is True:
        #Rainbow flashy boots
        if randint(1,1000) > 800:
            l1 = add_boots(smooshy_object, l1, bg, ol,(randint(0, 256), randint(0, 256), randint(0, 256)))
            l2 = add_boots(smooshy_object, l2, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l3 = add_boots(smooshy_object, l3, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l4 = add_boots(smooshy_object, l4, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l5 = add_boots(smooshy_object, l5, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l6 = add_boots(smooshy_object, l6, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l7 = add_boots(smooshy_object, l7, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))

            attributes_dict6["value"] = "Flashing"

        else:
            bc, boot_trait_type = boot_color_picker(randint(1,1000))

            l1 = add_boots(smooshy_object, l1, bg, ol, bc)
            l2 = add_boots(smooshy_object, l2, bg, ol, bc)
            l3 = add_boots(smooshy_object, l3, bg, ol, bc)
            l4 = add_boots(smooshy_object, l4, bg, ol, bc)
            l5 = add_boots(smooshy_object, l5, bg, ol, bc)
            l6 = add_boots(smooshy_object, l6, bg, ol, bc)
            l7 = add_boots(smooshy_object, l7, bg, ol, bc)

            attributes_dict6["value"] = boot_trait_type

    attributes_list.append(attributes_dict6)


    attributes_dict7["trait_type"] = "Headgear"
    attributes_dict7["value"] = "None"
    if hat is True:
        hc = (randint(0, 256), randint(0, 256), randint(0, 256))
        l1[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l2[8:19] = add_ballcap(smooshy_object, bg, ol, hc)
        l3[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l4[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l5[5:16] = add_ballcap(smooshy_object, bg, ol, hc)
        l6[2:13] = add_ballcap(smooshy_object, bg, ol, hc)
        l7[5:16] = add_ballcap(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Ballcap"


    if halo is True:
        hc = (255, 255, 0)
        l1[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l2[6:15] = add_halo(smooshy_object, bg, ol, hc)
        l3[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l4[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l5[3:12] = add_halo(smooshy_object, bg, ol, hc)
        l6[0:9] = add_halo(smooshy_object, bg, ol, hc)
        l7[3:12] = add_halo(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Halo"

    attributes_list.append(attributes_dict7)

    if background_flag is True:
        l1 = add_background(background_layers[0], l1)
        l2 = add_background(background_layers[1], l2)
        l3 = add_background(background_layers[2], l3)
        l4 = add_background(background_layers[3], l4)
        l5 = add_background(background_layers[4], l5)
        l6 = add_background(background_layers[5], l6)
        l7 = add_background(background_layers[6], l7)

    array1 = np.array(l1, dtype=np.uint8)
    array2 = np.array(l2, dtype=np.uint8)
    array3 = np.array(l3, dtype=np.uint8)
    array4 = np.array(l4, dtype=np.uint8)
    array5 = np.array(l5, dtype=np.uint8)
    array6 = np.array(l6, dtype=np.uint8)
    array7 = np.array(l7, dtype=np.uint8)

    im1 = Image.fromarray(array1)
    im2 = Image.fromarray(array2)
    im3 = Image.fromarray(array3)
    im4 = Image.fromarray(array4)
    im5 = Image.fromarray(array5)
    im6 = Image.fromarray(array6)
    im7 = Image.fromarray(array7)

    im1 = im1.resize(dimensions, resample=0)
    im2 = im2.resize(dimensions, resample=0)
    im3 = im3.resize(dimensions, resample=0)
    im4 = im4.resize(dimensions, resample=0)
    im5 = im5.resize(dimensions, resample=0)
    im6 = im6.resize(dimensions, resample=0)
    im7 = im7.resize(dimensions, resample=0)

    image_list.append(im1)
    image_list.append(im2)
    image_list.append(im3)
    image_list.append(im4)
    image_list.append(im5)
    image_list.append(im6)
    image_list.append(im7)
    image_list.append(im4)
    image_list.append(im3)
    image_list.append(im2)

    create_gif_from_images(image_list, num)
    create_metadata_file(attributes_list, num)


def generate_wavy_smooshies(smooshy_object, smooshy_wavy_object, background_flag, background_layers, num, bg, ol, mc, sc, boots, sunglasses, hat, halo,laser_eyes, eyes, attributes_list):
    image_list = []
    attributes_dict5 = {}
    attributes_dict6 = {}
    attributes_dict7 = {}

    attributes_dict5["trait_type"] = "Eyes"
    attributes_dict5["value"] = "Regular"

    l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
    l2 = smooshy_object.get_smooshy_generic_layer_2(bg, ol, mc[1], sc, eyes[1])
    l3 = smooshy_wavy_object.get_smooshy_wavy_layer3(bg, ol, mc[2], sc, eyes[2])
    l4 = smooshy_wavy_object.get_smooshy_wavy_layer4(bg, ol, mc[3], sc, eyes[3])
    l5 = smooshy_wavy_object.get_smooshy_wavy_layer5(bg, ol, mc[4], sc, eyes[4])
    l6 = smooshy_wavy_object.get_smooshy_wavy_layer6(bg, ol, mc[5], sc, eyes[5])
    l7 = smooshy_wavy_object.get_smooshy_wavy_layer7(bg, ol, mc[6], sc, eyes[6])

    if sunglasses is True:
        l1 = smooshy_object.get_smooshy_generic_base_sunglasses(bg, ol, mc[0], sc)
        l2 = smooshy_object.get_smooshy_generic_layer_2_sunglasses(bg, ol, mc[1], sc)
        l3 = smooshy_wavy_object.get_smooshy_wavy_layer3_sunglasses(bg, ol, mc[2], sc)
        l4 = smooshy_wavy_object.get_smooshy_wavy_layer4_sunglasses(bg, ol, mc[3], sc)
        l5 = smooshy_wavy_object.get_smooshy_wavy_layer5_sunglasses(bg, ol, mc[4], sc)
        l6 = smooshy_wavy_object.get_smooshy_wavy_layer6_sunglasses(bg, ol, mc[5], sc)
        l7 = smooshy_wavy_object.get_smooshy_wavy_layer7_sunglasses(bg, ol, mc[6], sc)

        attributes_dict5["value"] = "Sunglasses"


    elif laser_eyes is True:
        if randint(1,1000) > 200:
            lc = (255, 0, 0)
            attributes_dict5["value"] = "Red Laser Eyes"
        else:
            lc = (0, 128, 0)
            attributes_dict5["value"] = "Green Laser Eyes"

        l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
        l2 = smooshy_object.get_smooshy_generic_layer_2_laser(bg, ol, mc[1], sc, eyes[1], lc)
        l3 = smooshy_wavy_object.get_smooshy_wavy_layer3_laser(bg, ol, mc[2], sc, eyes[2], lc)
        l4 = smooshy_wavy_object.get_smooshy_wavy_layer4_laser(bg, ol, mc[3], sc, eyes[3], lc)
        l5 = smooshy_wavy_object.get_smooshy_wavy_layer5_laser(bg, ol, mc[4], sc, eyes[4], lc)
        l6 = smooshy_wavy_object.get_smooshy_wavy_layer6_laser(bg, ol, mc[5], sc, eyes[5], lc)
        l7 = smooshy_wavy_object.get_smooshy_wavy_layer7_laser(bg, ol, mc[6], sc, eyes[6], lc)

    attributes_list.append(attributes_dict5)

    attributes_dict6["trait_type"] = "Boots"
    attributes_dict6["value"] = "None"
    if boots is True:
        #Rainbow flashy boots
        if randint(1,1000) > 800:
            l1 = add_boots(smooshy_object, l1, bg, ol,(randint(0, 256), randint(0, 256), randint(0, 256)))
            l2 = add_boots(smooshy_object, l2, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l3 = add_boots(smooshy_object, l3, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l4 = add_boots(smooshy_object, l4, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l5 = add_boots(smooshy_object, l5, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l6 = add_boots(smooshy_object, l6, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l7 = add_boots(smooshy_object, l7, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))

            attributes_dict6["value"] = "Flashing"

        else:
            bc, boot_trait_type = boot_color_picker(randint(1,1000))

            l1 = add_boots(smooshy_object, l1, bg, ol, bc)
            l2 = add_boots(smooshy_object, l2, bg, ol, bc)
            l3 = add_boots(smooshy_object, l3, bg, ol, bc)
            l4 = add_boots(smooshy_object, l4, bg, ol, bc)
            l5 = add_boots(smooshy_object, l5, bg, ol, bc)
            l6 = add_boots(smooshy_object, l6, bg, ol, bc)
            l7 = add_boots(smooshy_object, l7, bg, ol, bc)

            attributes_dict6["value"] = boot_trait_type

    attributes_list.append(attributes_dict6)


    attributes_dict7["trait_type"] = "Headgear"
    attributes_dict7["value"] = "None"
    if hat is True:
        hc = (randint(0, 256), randint(0, 256), randint(0, 256))
        l1[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l2[8:19] = add_ballcap(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Ballcap"

    if halo is True:
        hc = (255, 255, 0)
        l1[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l2[6:15] = add_halo(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Halo"

    attributes_list.append(attributes_dict7)

    if background_flag is True:
        l1 = add_background(background_layers[0], l1)
        l2 = add_background(background_layers[1], l2)
        l3 = add_background(background_layers[2], l3)
        l4 = add_background(background_layers[3], l4)
        l5 = add_background(background_layers[4], l5)
        l6 = add_background(background_layers[5], l6)
        l7 = add_background(background_layers[6], l7)

    array1 = np.array(l1, dtype=np.uint8)
    array2 = np.array(l2, dtype=np.uint8)
    array3 = np.array(l3, dtype=np.uint8)
    array4 = np.array(l4, dtype=np.uint8)
    array5 = np.array(l5, dtype=np.uint8)
    array6 = np.array(l6, dtype=np.uint8)
    array7 = np.array(l7, dtype=np.uint8)

    im1 = Image.fromarray(array1)
    im2 = Image.fromarray(array2)
    im3 = Image.fromarray(array3)
    im4 = Image.fromarray(array4)
    im5 = Image.fromarray(array5)
    im6 = Image.fromarray(array6)
    im7 = Image.fromarray(array7)

    im1 = im1.resize(dimensions, resample=0)
    im2 = im2.resize(dimensions, resample=0)
    im3 = im3.resize(dimensions, resample=0)
    im4 = im4.resize(dimensions, resample=0)
    im5 = im5.resize(dimensions, resample=0)
    im6 = im6.resize(dimensions, resample=0)
    im7 = im7.resize(dimensions, resample=0)

    image_list.append(im1)
    image_list.append(im2)
    image_list.append(im3)
    image_list.append(im4)
    image_list.append(im5)
    image_list.append(im6)
    image_list.append(im7)
    image_list.append(im4)
    image_list.append(im3)
    image_list.append(im2)

    create_gif_from_images(image_list, num)
    create_metadata_file(attributes_list, num)


def generate_alien_smooshies(smooshy_object, smooshy_alien_object, background_flag, background_layers, num, bg, ol, mc, sc, boots, sunglasses, hat, halo,laser_eyes, eyes, attributes_list):
    image_list = []
    attributes_dict5 = {}
    attributes_dict6 = {}
    attributes_dict7 = {}

    i = 2
    for eye_pixel in eyes[2:]:
        if eye_pixel == (0, 0, 0):
            eyes[i] = (255, 255, 255)
        i = i + 1

    attributes_dict5["trait_type"] = "Eyes"
    attributes_dict5["value"] = "Regular"
    l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
    l2 = smooshy_object.get_smooshy_generic_layer_2(bg, ol, mc[1], sc, eyes[1])
    l3 = smooshy_alien_object.get_smooshy_alien_layer3(bg, ol, mc[2], sc, eyes[2])
    l4 = smooshy_alien_object.get_smooshy_alien_layer4(bg, ol, mc[3], sc, eyes[3])
    l5 = smooshy_alien_object.get_smooshy_alien_layer5(bg, ol, mc[4], sc, eyes[4])
    l6 = smooshy_alien_object.get_smooshy_alien_layer6(bg, ol, mc[5], sc, eyes[5])
    l7 = smooshy_alien_object.get_smooshy_alien_layer7(bg, ol, mc[6], sc, eyes[6])

    if sunglasses is True:
        l1 = smooshy_object.get_smooshy_generic_base_sunglasses(bg, ol, mc[0], sc)
        l2 = smooshy_object.get_smooshy_generic_layer_2_sunglasses(bg, ol, mc[1], sc)
        attributes_dict5["value"] = "Sunglasses"

    elif laser_eyes is True:
        if randint(1,1000) > 200:
            lc = (255, 0, 0)
            attributes_dict5["value"] = "Red Laser Eyes"
        else:
            lc = (0, 128, 0)
            attributes_dict5["value"] = "Green Laser Eyes"

        l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
        l2 = smooshy_object.get_smooshy_generic_layer_2_laser(bg, ol, mc[1], sc, eyes[1], lc)
        l3 = smooshy_alien_object.get_smooshy_alien_layer3_laser(bg, ol, mc[2], sc, eyes[2], lc)
        l4 = smooshy_alien_object.get_smooshy_alien_layer4_laser(bg, ol, mc[3], sc, eyes[3], lc)
        l5 = smooshy_alien_object.get_smooshy_alien_layer5_laser(bg, ol, mc[4], sc, eyes[4], lc)
        l6 = smooshy_alien_object.get_smooshy_alien_layer6_laser(bg, ol, mc[5], sc, eyes[5], lc)
        l7 = smooshy_alien_object.get_smooshy_alien_layer7_laser(bg, ol, mc[6], sc, eyes[6], lc)

    attributes_list.append(attributes_dict5)

    attributes_dict6["trait_type"] = "Boots"
    attributes_dict6["value"] = "None"
    if boots is True:
        #Rainbow flashy boots
        if randint(1,1000) > 800:
            l1 = add_boots(smooshy_object, l1, bg, ol,(randint(0, 256), randint(0, 256), randint(0, 256)))
            l2 = add_boots(smooshy_object, l2, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l3 = add_boots(smooshy_object, l3, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l4 = add_boots(smooshy_object, l4, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l5 = add_boots(smooshy_object, l5, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l6 = add_boots(smooshy_object, l6, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l7 = add_boots(smooshy_object, l7, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))

            attributes_dict6["value"] = "Flashing"

        else:
            bc, boot_trait_type = boot_color_picker(randint(1,1000))

            l1 = add_boots(smooshy_object, l1, bg, ol, bc)
            l2 = add_boots(smooshy_object, l2, bg, ol, bc)
            l3 = add_boots(smooshy_object, l3, bg, ol, bc)
            l4 = add_boots(smooshy_object, l4, bg, ol, bc)
            l5 = add_boots(smooshy_object, l5, bg, ol, bc)
            l6 = add_boots(smooshy_object, l6, bg, ol, bc)
            l7 = add_boots(smooshy_object, l7, bg, ol, bc)

            attributes_dict6["value"] = boot_trait_type

    attributes_list.append(attributes_dict6)

    attributes_dict7["trait_type"] = "Headgear"
    attributes_dict7["value"] = "None"
    if hat is True:
        hc = (randint(0, 256), randint(0, 256), randint(0, 256))
        l1[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l2[8:19] = add_ballcap(smooshy_object, bg, ol, hc)
        l3[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l4[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l5[5:16] = add_ballcap(smooshy_object, bg, ol, hc)
        l6[2:13] = add_ballcap(smooshy_object, bg, ol, hc)
        l7[5:16] = add_ballcap(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Ballcap"

    if halo is True:
        hc = (255, 255, 0)
        l1[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l2[6:15] = add_halo(smooshy_object, bg, ol, hc)
        l3[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l4[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l5[3:12] = add_halo(smooshy_object, bg, ol, hc)
        l6[0:9] = add_halo(smooshy_object, bg, ol, hc)
        l7[3:12] = add_halo(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Halo"

    attributes_list.append(attributes_dict7)

    if background_flag is True:
        l1 = add_background(background_layers[0], l1)
        l2 = add_background(background_layers[1], l2)
        l3 = add_background(background_layers[2], l3)
        l4 = add_background(background_layers[3], l4)
        l5 = add_background(background_layers[4], l5)
        l6 = add_background(background_layers[5], l6)
        l7 = add_background(background_layers[6], l7)

    array1 = np.array(l1, dtype=np.uint8)
    array2 = np.array(l2, dtype=np.uint8)
    array3 = np.array(l3, dtype=np.uint8)
    array4 = np.array(l4, dtype=np.uint8)
    array5 = np.array(l5, dtype=np.uint8)
    array6 = np.array(l6, dtype=np.uint8)
    array7 = np.array(l7, dtype=np.uint8)

    im1 = Image.fromarray(array1)
    im2 = Image.fromarray(array2)
    im3 = Image.fromarray(array3)
    im4 = Image.fromarray(array4)
    im5 = Image.fromarray(array5)
    im6 = Image.fromarray(array6)
    im7 = Image.fromarray(array7)

    im1 = im1.resize(dimensions, resample=0)
    im2 = im2.resize(dimensions, resample=0)
    im3 = im3.resize(dimensions, resample=0)
    im4 = im4.resize(dimensions, resample=0)
    im5 = im5.resize(dimensions, resample=0)
    im6 = im6.resize(dimensions, resample=0)
    im7 = im7.resize(dimensions, resample=0)

    image_list.append(im1)
    image_list.append(im2)
    image_list.append(im3)
    image_list.append(im4)
    image_list.append(im5)
    image_list.append(im6)
    image_list.append(im7)
    image_list.append(im4)
    image_list.append(im3)
    image_list.append(im2)

    create_gif_from_images(image_list, num)
    create_metadata_file(attributes_list, num)


def generate_robot_smooshies(smooshy_object, smooshy_robot_object, background_flag, background_layers, num, bg, ol, mc, sc, boots, sunglasses, hat, halo,laser_eyes, eyes, attributes_list):
    image_list = []
    attributes_dict5 = {}
    attributes_dict6 = {}
    attributes_dict7 = {}

    i = 2
    for eye_pixel in eyes[2:]:
        if eye_pixel == (0, 0, 0):
            eyes[i] = (255, 255, 255)
        i = i + 1

    attributes_dict5["trait_type"] = "Eyes"
    attributes_dict5["value"] = "Regular"
    l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
    l2 = smooshy_object.get_smooshy_generic_layer_2(bg, ol, mc[1], sc, eyes[1])
    l3 = smooshy_robot_object.get_smooshy_robot_layer3(bg, ol, mc[2], sc, eyes[2])
    l4 = smooshy_robot_object.get_smooshy_robot_layer4(bg, ol, mc[3], sc, eyes[3])
    l5 = smooshy_robot_object.get_smooshy_robot_layer5(bg, ol, mc[4], sc, eyes[4])
    l6 = smooshy_robot_object.get_smooshy_robot_layer6(bg, ol, mc[5], sc, eyes[5])
    l7 = smooshy_robot_object.get_smooshy_robot_layer7(bg, ol, mc[6], sc, eyes[6])

    if sunglasses is True:
        l1 = smooshy_object.get_smooshy_generic_base_sunglasses(bg, ol, mc[0], sc)
        l2 = smooshy_object.get_smooshy_generic_layer_2_sunglasses(bg, ol, mc[1], sc)

        attributes_dict5["value"] = "Sunglasses"

    elif laser_eyes is True:
        if randint(1,1000) > 200:
            lc = (255, 0, 0)
            attributes_dict5["value"] = "Red Laser Eyes"
        else:
            lc = (0, 128, 0)
            attributes_dict5["value"] = "Green Laser Eyes"

        l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
        l2 = smooshy_object.get_smooshy_generic_layer_2_laser(bg, ol, mc[1], sc, eyes[1], lc)
        l3 = smooshy_robot_object.get_smooshy_robot_layer3_laser(bg, ol, mc[2], sc, eyes[2], lc)
        l4 = smooshy_robot_object.get_smooshy_robot_layer4_laser(bg, ol, mc[3], sc, eyes[3], lc)
        l5 = smooshy_robot_object.get_smooshy_robot_layer5_laser(bg, ol, mc[4], sc, eyes[4], lc)
        l6 = smooshy_robot_object.get_smooshy_robot_layer6_laser(bg, ol, mc[5], sc, eyes[5], lc)
        l7 = smooshy_robot_object.get_smooshy_robot_layer7_laser(bg, ol, mc[6], sc, eyes[6], lc)

    attributes_list.append(attributes_dict5)

    attributes_dict6["trait_type"] = "Boots"
    attributes_dict6["value"] = "None"
    if boots is True:
        #Rainbow flashy boots
        if randint(1,1000) > 800:
            l1 = add_boots(smooshy_object, l1, bg, ol,(randint(0, 256), randint(0, 256), randint(0, 256)))
            l2 = add_boots(smooshy_object, l2, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l3 = add_boots(smooshy_object, l3, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l4 = add_boots(smooshy_object, l4, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l5 = add_boots(smooshy_object, l5, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l6 = add_boots(smooshy_object, l6, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))
            l7 = add_boots(smooshy_object, l7, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))

            attributes_dict6["value"] = "Flashing"

        else:
            bc, boot_trait_type = boot_color_picker(randint(1,1000))

            l1 = add_boots(smooshy_object, l1, bg, ol, bc)
            l2 = add_boots(smooshy_object, l2, bg, ol, bc)
            l3 = add_boots(smooshy_object, l3, bg, ol, bc)
            l4 = add_boots(smooshy_object, l4, bg, ol, bc)
            l5 = add_boots(smooshy_object, l5, bg, ol, bc)
            l6 = add_boots(smooshy_object, l6, bg, ol, bc)
            l7 = add_boots(smooshy_object, l7, bg, ol, bc)

            attributes_dict6["value"] = boot_trait_type

    attributes_list.append(attributes_dict6)

    attributes_dict7["trait_type"] = "Headgear"
    attributes_dict7["value"] = "None"
    if hat is True:
        hc = (randint(0, 256), randint(0, 256), randint(0, 256))
        l1[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l2[8:19] = add_ballcap(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Ballcap"

    if halo is True:
        hc = (255, 255, 0)
        l1[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l2[6:15] = add_halo(smooshy_object, bg, ol, hc)
        l3[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l4[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l5[3:12] = add_halo(smooshy_object, bg, ol, hc)
        l6[0:9] = add_halo(smooshy_object, bg, ol, hc)
        l7[3:12] = add_halo(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Halo"

    attributes_list.append(attributes_dict7)

    if background_flag is True:
        l1 = add_background(background_layers[0], l1)
        l2 = add_background(background_layers[1], l2)
        l3 = add_background(background_layers[2], l3)
        l4 = add_background(background_layers[3], l4)
        l5 = add_background(background_layers[4], l5)
        l6 = add_background(background_layers[5], l6)
        l7 = add_background(background_layers[6], l7)

    array1 = np.array(l1, dtype=np.uint8)
    array2 = np.array(l2, dtype=np.uint8)
    array3 = np.array(l3, dtype=np.uint8)
    array4 = np.array(l4, dtype=np.uint8)
    array5 = np.array(l5, dtype=np.uint8)
    array6 = np.array(l6, dtype=np.uint8)
    array7 = np.array(l7, dtype=np.uint8)

    im1 = Image.fromarray(array1)
    im2 = Image.fromarray(array2)
    im3 = Image.fromarray(array3)
    im4 = Image.fromarray(array4)
    im5 = Image.fromarray(array5)
    im6 = Image.fromarray(array6)
    im7 = Image.fromarray(array7)

    im1 = im1.resize(dimensions, resample=0)
    im2 = im2.resize(dimensions, resample=0)
    im3 = im3.resize(dimensions, resample=0)
    im4 = im4.resize(dimensions, resample=0)
    im5 = im5.resize(dimensions, resample=0)
    im6 = im6.resize(dimensions, resample=0)
    im7 = im7.resize(dimensions, resample=0)

    image_list.append(im1)
    image_list.append(im2)
    image_list.append(im3)
    image_list.append(im4)
    image_list.append(im5)
    image_list.append(im6)
    image_list.append(im7)
    image_list.append(im4)
    image_list.append(im3)
    image_list.append(im2)

    create_gif_from_images(image_list, num)
    create_metadata_file(attributes_list, num)


def generate_monkey_smooshies(smooshy_object, smooshy_monkey_object, background_flag, background_layers, num, bg, ol, mc, sc, boots, sunglasses, hat, halo,laser_eyes, eyes, attributes_list):
    image_list = []
    # m2 is main color 2 (lighter color) maybe tan
    m2 = (210, 180, 140)
    brown = (165, 42, 42)
    yellow = (255, 255, 0)

    attributes_dict5 = {}
    attributes_dict6 = {}
    attributes_dict7 = {}
    monkey_attribute_dict = {}

    monkey_attribute_dict["trait_type"] = "Extra"
    monkey_attribute_dict["value"] = "None"
    l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
    l2 = smooshy_object.get_smooshy_generic_layer_2(bg, ol, mc[1], sc, eyes[1])
    l3 = smooshy_monkey_object.get_smooshy_monkey_layer3(bg, ol, mc[2], sc, eyes[2])
    l4 = smooshy_monkey_object.get_smooshy_monkey_layer4(bg, ol, mc[3], sc, m2, eyes[3])
    l5 = smooshy_monkey_object.get_smooshy_monkey_layer5(bg, ol, mc[4], sc, m2, eyes[4])
    l6 = smooshy_monkey_object.get_smooshy_monkey_layer6(bg, ol, mc[5], sc, m2, eyes[5])
    l7 = smooshy_monkey_object.get_smooshy_monkey_layer7(bg, ol, mc[6], sc, m2, eyes[6])

    if randint(1, 1000) > 500:
        l5 = smooshy_monkey_object.get_smooshy_monkey_layer5_banana(bg, ol, mc[4], sc, m2, eyes[4], yellow, brown)
        l6 = smooshy_monkey_object.get_smooshy_monkey_layer6_banana(bg, ol, mc[5], sc, m2, eyes[5], yellow, brown)
        l7 = smooshy_monkey_object.get_smooshy_monkey_layer7_banana(bg, ol, mc[6], sc, m2, eyes[6], yellow, brown)
        monkey_attribute_dict["value"] = "Banana"


    attributes_dict5["trait_type"] = "Eyes"
    attributes_dict5["value"] = "Regular"
    if sunglasses is True:
        l1 = smooshy_object.get_smooshy_generic_base_sunglasses(bg, ol, mc[0], sc)
        l2 = smooshy_object.get_smooshy_generic_layer_2_sunglasses(bg, ol, mc[1], sc)

        attributes_dict5["value"] = "Sunglasses"

    elif laser_eyes is True:
        if randint(1,1000) > 200:
            lc = (255, 0, 0)
            attributes_dict5["value"] = "Red Laser Eyes"
        else:
            lc = (0, 128, 0)
            attributes_dict5["value"] = "Green Laser Eyes"

        l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
        l2 = smooshy_object.get_smooshy_generic_layer_2_laser(bg, ol, mc[1], sc, eyes[1], lc)
        l3 = smooshy_monkey_object.get_smooshy_monkey_layer3_laser(bg, ol, mc[2], sc, eyes[2], lc)
        l4 = smooshy_monkey_object.get_smooshy_monkey_layer4_laser(bg, ol, mc[3], sc, m2, eyes[3], lc)
        l5 = smooshy_monkey_object.get_smooshy_monkey_layer5_laser(bg, ol, mc[4], sc, m2, eyes[4], lc)
        l6 = smooshy_monkey_object.get_smooshy_monkey_layer6_laser(bg, ol, mc[5], sc, m2, eyes[5], lc)
        l7 = smooshy_monkey_object.get_smooshy_monkey_layer7_laser(bg, ol, mc[6], sc, m2, eyes[6], lc)

    attributes_list.append(attributes_dict5)

    attributes_dict6["trait_type"] = "Boots"
    attributes_dict6["value"] = "None"
    if boots is True:
        #Rainbow flashy boots
        if randint(1,1000) > 800:
            l1 = add_boots(smooshy_object, l1, bg, ol,(randint(0, 256), randint(0, 256), randint(0, 256)))
            l2 = add_boots(smooshy_object, l2, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))

            attributes_dict6["value"] = "Flashing"

        else:
            bc, boot_trait_type = boot_color_picker(randint(1,1000))

            l1 = add_boots(smooshy_object, l1, bg, ol, bc)
            l2 = add_boots(smooshy_object, l2, bg, ol, bc)

            attributes_dict6["value"] = boot_trait_type

    attributes_list.append(attributes_dict6)

    attributes_dict7["trait_type"] = "Headgear"
    attributes_dict7["value"] = "None"
    if hat is True:
        hc = (randint(0, 256), randint(0, 256), randint(0, 256))
        l1[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l2[8:19] = add_ballcap(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Ballcap"

    if halo is True:
        hc = (255, 255, 0)
        l1[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l2[6:15] = add_halo(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Halo"

    attributes_list.append(attributes_dict7)

    if laser_eyes is False:
        attributes_list.append(monkey_attribute_dict)

    if background_flag is True:
        l1 = add_background(background_layers[0], l1)
        l2 = add_background(background_layers[1], l2)
        l3 = add_background(background_layers[2], l3)
        l4 = add_background(background_layers[3], l4)
        l5 = add_background(background_layers[4], l5)
        l6 = add_background(background_layers[5], l6)
        l7 = add_background(background_layers[6], l7)

    array1 = np.array(l1, dtype=np.uint8)
    array2 = np.array(l2, dtype=np.uint8)
    array3 = np.array(l3, dtype=np.uint8)
    array4 = np.array(l4, dtype=np.uint8)
    array5 = np.array(l5, dtype=np.uint8)
    array6 = np.array(l6, dtype=np.uint8)
    array7 = np.array(l7, dtype=np.uint8)

    im1 = Image.fromarray(array1)
    im2 = Image.fromarray(array2)
    im3 = Image.fromarray(array3)
    im4 = Image.fromarray(array4)
    im5 = Image.fromarray(array5)
    im6 = Image.fromarray(array6)
    im7 = Image.fromarray(array7)

    im1 = im1.resize(dimensions, resample=0)
    im2 = im2.resize(dimensions, resample=0)
    im3 = im3.resize(dimensions, resample=0)
    im4 = im4.resize(dimensions, resample=0)
    im5 = im5.resize(dimensions, resample=0)
    im6 = im6.resize(dimensions, resample=0)
    im7 = im7.resize(dimensions, resample=0)

    image_list.append(im1)
    image_list.append(im2)
    image_list.append(im3)
    image_list.append(im4)
    image_list.append(im5)
    image_list.append(im6)
    image_list.append(im7)
    image_list.append(im4)
    image_list.append(im3)
    image_list.append(im2)

    create_gif_from_images(image_list, num)
    create_metadata_file(attributes_list, num)


def generate_punk_smooshies(smooshy_object, smooshy_punk_object, background_flag, background_layers, num, bg, ol, mc, sc, boots, sunglasses, hat, halo,laser_eyes, eyes, attributes_list):
    image_list = []
    attributes_dict5 = {}
    attributes_dict6 = {}
    attributes_dict7 = {}
    punk_attribute_dict = {}

    # skin color
    # mc = (randint(0, 256), randint(0, 256), randint(0, 256))
    # hc, ew, fc (hair color, eye white color, facial hair color)
    hc = (randint(0, 256), randint(0, 256), randint(0, 256))
    ew = (255, 255, 255)
    fc = hc
    orange = (255, 165, 0)
    darkgrey = (169, 169, 169)
    white = (255, 255, 255)

    punk_attribute_dict["trait_type"] = "Extra"
    punk_attribute_dict["value"] = "None"
    l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
    l2 = smooshy_object.get_smooshy_generic_layer_2(bg, ol, mc[1], sc, eyes[1])
    l3 = smooshy_punk_object.get_smooshy_punk_layer3(bg, ol, mc[2], sc, eyes[2])
    l4 = smooshy_punk_object.get_smooshy_punk_layer4(bg, ol, mc[3], sc, hc, eyes[3], ew, fc)
    l5 = smooshy_punk_object.get_smooshy_punk_layer5(bg, ol, mc[4], sc, hc, eyes[4], ew, fc)
    l6 = smooshy_punk_object.get_smooshy_punk_layer6(bg, ol, mc[5], sc, hc, eyes[5], ew, fc)
    l7 = smooshy_punk_object.get_smooshy_punk_layer7(bg, ol, mc[6], sc, hc, eyes[6], ew, fc)

    if randint(1, 1000) > 500:
        l4 = smooshy_punk_object.get_smooshy_punk_layer4_cig(bg, ol, mc[3], sc, hc, eyes[3], ew, fc, orange, white)
        l5 = smooshy_punk_object.get_smooshy_punk_layer5_cig(bg, ol, mc[4], sc, hc, eyes[4], ew, fc, orange, white, darkgrey)
        l6 = smooshy_punk_object.get_smooshy_punk_layer6_cig(bg, ol, mc[5], sc, hc, eyes[5], ew, fc, orange, white, darkgrey)
        l7 = smooshy_punk_object.get_smooshy_punk_layer7_cig(bg, ol, mc[6], sc, hc, eyes[6], ew, fc, orange, white, darkgrey)

        punk_attribute_dict["value"] = "Cig"


    attributes_dict5["trait_type"] = "Eyes"
    attributes_dict5["value"] = "Regular"
    if laser_eyes is True:
        if randint(1,1000) > 200:
            lc = (255, 0, 0)
            attributes_dict5["value"] = "Red Laser Eyes"
        else:
            lc = (0, 128, 0)
            attributes_dict5["value"] = "Green Laser Eyes"

        l1 = smooshy_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
        l2 = smooshy_object.get_smooshy_generic_layer_2_laser(bg, ol, mc[1], sc, eyes[1], lc)
        l3 = smooshy_punk_object.get_smooshy_punk_layer3_laser(bg, ol, mc[2], sc, eyes[2], lc)
        l4 = smooshy_punk_object.get_smooshy_punk_layer4_laser(bg, ol, mc[3], sc, hc, eyes[3], ew, fc, lc)
        l5 = smooshy_punk_object.get_smooshy_punk_layer5_laser(bg, ol, mc[4], sc, hc, eyes[4], ew, fc, lc)
        l6 = smooshy_punk_object.get_smooshy_punk_layer6_laser(bg, ol, mc[5], sc, hc, eyes[5], ew, fc, lc)
        l7 = smooshy_punk_object.get_smooshy_punk_layer7_laser(bg, ol, mc[6], sc, hc, eyes[6], ew, fc, lc)

    if sunglasses is True:
        l1 = smooshy_object.get_smooshy_generic_base_sunglasses(bg, ol, mc[0], sc)
        l2 = smooshy_object.get_smooshy_generic_layer_2_sunglasses(bg, ol, mc[1], sc)

        attributes_dict5["value"] = "Sunglasses"


    attributes_list.append(attributes_dict5)

    attributes_dict6["trait_type"] = "Boots"
    attributes_dict6["value"] = "None"
    if boots is True:
        #Rainbow flashy boots
        if randint(1,1000) > 800:
            l1 = add_boots(smooshy_object, l1, bg, ol,(randint(0, 256), randint(0, 256), randint(0, 256)))
            l2 = add_boots(smooshy_object, l2, bg, ol, (randint(0, 256), randint(0, 256), randint(0, 256)))

            attributes_dict6["value"] = "Flashing"

        else:
            bc, boot_trait_type = boot_color_picker(randint(1,1000))

            l1 = add_boots(smooshy_object, l1, bg, ol, bc)
            l2 = add_boots(smooshy_object, l2, bg, ol, bc)

            attributes_dict6["value"] = boot_trait_type

    attributes_list.append(attributes_dict6)

    attributes_dict7["trait_type"] = "Headgear"
    attributes_dict7["value"] = "None"
    if hat is True:
        hc = (randint(0, 256), randint(0, 256), randint(0, 256))
        l1[6:17] = add_ballcap(smooshy_object, bg, ol, hc)
        l2[8:19] = add_ballcap(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Ballcap"

    if halo is True:
        hc = (255, 255, 0)
        l1[4:13] = add_halo(smooshy_object, bg, ol, hc)
        l2[6:15] = add_halo(smooshy_object, bg, ol, hc)

        attributes_dict7["value"] = "Halo"

    attributes_list.append(attributes_dict7)

    if laser_eyes is False:
        attributes_list.append(punk_attribute_dict)

    if background_flag is True:
        l1 = add_background(background_layers[0], l1)
        l2 = add_background(background_layers[1], l2)
        l3 = add_background(background_layers[2], l3)
        l4 = add_background(background_layers[3], l4)
        l5 = add_background(background_layers[4], l5)
        l6 = add_background(background_layers[5], l6)
        l7 = add_background(background_layers[6], l7)


    array1 = np.array(l1, dtype=np.uint8)
    array2 = np.array(l2, dtype=np.uint8)
    array3 = np.array(l3, dtype=np.uint8)
    array4 = np.array(l4, dtype=np.uint8)
    array5 = np.array(l5, dtype=np.uint8)
    array6 = np.array(l6, dtype=np.uint8)
    array7 = np.array(l7, dtype=np.uint8)

    im1 = Image.fromarray(array1)
    im2 = Image.fromarray(array2)
    im3 = Image.fromarray(array3)
    im4 = Image.fromarray(array4)
    im5 = Image.fromarray(array5)
    im6 = Image.fromarray(array6)
    im7 = Image.fromarray(array7)

    im1 = im1.resize(dimensions, resample=0)
    im2 = im2.resize(dimensions, resample=0)
    im3 = im3.resize(dimensions, resample=0)
    im4 = im4.resize(dimensions, resample=0)
    im5 = im5.resize(dimensions, resample=0)
    im6 = im6.resize(dimensions, resample=0)
    im7 = im7.resize(dimensions, resample=0)

    image_list.append(im1)
    image_list.append(im2)
    image_list.append(im3)
    image_list.append(im4)
    image_list.append(im5)
    image_list.append(im6)
    image_list.append(im7)
    image_list.append(im4)
    image_list.append(im3)
    image_list.append(im2)

    create_gif_from_images(image_list, num)
    create_metadata_file(attributes_list, num)


def generate_0(background_flag, background_layers, num, bg, ol, mc, sc, eyes):
    image_list = []
    attributes_dict5 = {}
    attributes_dict6 = {}
    attributes_dict7 = {}
    punk_attribute_dict = {}

    # skin color
    # mc = (randint(0, 256), randint(0, 256), randint(0, 256))
    # hc, ew, fc (hair color, eye white color, facial hair color)
    hc = (randint(0, 256), randint(0, 256), randint(0, 256))
    ew = (255, 255, 255)
    fc = hc
    orange = (255, 165, 0)
    darkgrey = (169, 169, 169)
    white = (255, 255, 255)
    m2 = (210, 180, 140)

    punk_attribute_dict["trait_type"] = "Extra"
    punk_attribute_dict["value"] = "None"
    l1 = smooshy_generic_object.get_smooshy_generic_base(bg, ol, mc[0], sc, eyes[0])
    l2 = smooshy_generic_object.get_smooshy_generic_layer_2(bg, ol, mc[1], sc, eyes[1])
    l3 = smooshy_wavy_object.get_smooshy_wavy_layer6(bg, ol, mc[2], sc, eyes[2])
    l4 = smooshy_robot_object.get_smooshy_robot_layer6(bg, ol, mc[3], sc, eyes[3])
    l5 = smooshy_alien_object.get_smooshy_alien_layer6(bg, ol, mc[4], sc, eyes[4])
    l6 = smooshy_monkey_object.get_smooshy_monkey_layer6(bg, ol, mc[5], sc, m2, eyes[5])
    l7 = smooshy_punk_object.get_smooshy_punk_layer6(bg, ol, mc[6], sc, hc, eyes[6], ew, fc)

    if background_flag is True:
        l1 = add_background(background_layers[0], l1)
        l2 = add_background(background_layers[1], l2)
        l3 = add_background(background_layers[2], l3)
        l4 = add_background(background_layers[3], l4)
        l5 = add_background(background_layers[4], l5)
        l6 = add_background(background_layers[5], l6)
        l7 = add_background(background_layers[6], l7)


    array1 = np.array(l1, dtype=np.uint8)
    array2 = np.array(l2, dtype=np.uint8)
    array3 = np.array(l3, dtype=np.uint8)
    array4 = np.array(l4, dtype=np.uint8)
    array5 = np.array(l5, dtype=np.uint8)
    array6 = np.array(l6, dtype=np.uint8)
    array7 = np.array(l7, dtype=np.uint8)

    im1 = Image.fromarray(array1)
    im2 = Image.fromarray(array2)
    im3 = Image.fromarray(array3)
    im4 = Image.fromarray(array4)
    im5 = Image.fromarray(array5)
    im6 = Image.fromarray(array6)
    im7 = Image.fromarray(array7)

    im1 = im1.resize(dimensions, resample=0)
    im2 = im2.resize(dimensions, resample=0)
    im3 = im3.resize(dimensions, resample=0)
    im4 = im4.resize(dimensions, resample=0)
    im5 = im5.resize(dimensions, resample=0)
    im6 = im6.resize(dimensions, resample=0)
    im7 = im7.resize(dimensions, resample=0)

    image_list.append(im1)
    image_list.append(im2)
    image_list.append(im3)
    image_list.append(im4)
    image_list.append(im5)
    image_list.append(im6)
    image_list.append(im7)
    image_list.append(im4)
    image_list.append(im3)
    image_list.append(im2)

    create_gif_from_images(image_list, num)



def get_smooshy_chart_background(smooshy_chart_object, ol):
    bg  = (238, 238, 238)
    gc = (0, 128, 0)
    rc = (255, 0, 0)

    background = smooshy_chart_object.get_smooshy_chart(bg, ol, gc, rc)

    return background


def get_smooshy_rainbow_background(smooshy_rainbow_object):
    rc = (255, 0, 0)
    oc = (255, 165, 0)
    yc = (255, 255, 0)
    gc = (0, 128, 0)
    bc = (0, 0, 255)
    vc = (238, 130, 238)

    background = smooshy_rainbow_object.get_raninbow_background(rc, oc, yc, gc, bc, vc)

    return background

def get_smooshy_space_background(smooshy_space_object):
    gold = (255, 215, 0)
    yellow = (255, 255, 0)
    white = (255, 255, 255)
    blue = (0, 0, 139)

    b_list = []

    b1 = smooshy_space_object.get_smooshy_space_background(blue, gold, yellow, white)
    b2 = smooshy_space_object.get_smooshy_space_background(blue, yellow, white, gold)
    b3 = smooshy_space_object.get_smooshy_space_background(blue, white, gold, yellow)
    b4 = smooshy_space_object.get_smooshy_space_background(blue, white, yellow, gold)
    b5 = smooshy_space_object.get_smooshy_space_background(blue, gold, white, yellow)
    b6 = smooshy_space_object.get_smooshy_space_background(blue, yellow, gold, white)
    b7 = smooshy_space_object.get_smooshy_space_background(blue, gold, yellow, white)

    b_list.append(b1)
    b_list.append(b2)
    b_list.append(b3)
    b_list.append(b4)
    b_list.append(b5)
    b_list.append(b6)
    b_list.append(b7)

    return b_list


def get_smooshy_fire_background(smooshy_fire_object):
    black = (0, 0, 0)
    red = (255, 0, 0)
    orange = (255, 165, 0)
    yellow = (255, 255, 0)
    white = (255, 255, 255)

    b_list = []

    b1 = smooshy_fire_object.get_smooshy_fire_background_1(black, red, orange, yellow, white)
    b2 = smooshy_fire_object.get_smooshy_fire_background_2(black, red, orange, yellow, white)
    b3 = smooshy_fire_object.get_smooshy_fire_background_3(black, red, orange, yellow, white)
    b4 = smooshy_fire_object.get_smooshy_fire_background_4(black, red, orange, yellow, white)

    b_list.append(b1)
    b_list.append(b2)
    b_list.append(b3)
    b_list.append(b4)

    return b_list

def get_smooshy_animated_lightning_background(smooshy_lightning_object):
    black = (0, 0, 0)
    lightblue = (173, 216, 230)
    brown = (165, 42, 42)
    green = (0, 128, 0)
    yellow = (255, 255, 0)
    gold = (204,172,0)
    darkgrey = (169, 169, 169)
    grey = (128, 128, 128)

    b_list = []

    b1 = smooshy_lightning_object.get_smooshy_lightning_background_1(lightblue, black, brown, green, yellow, gold, darkgrey)
    b2 = smooshy_lightning_object.get_smooshy_lightning_background_2(lightblue, black, brown, green, yellow, gold, darkgrey)
    b3 = smooshy_lightning_object.get_smooshy_lightning_background_3(grey, black, brown, green, yellow, gold, darkgrey)
    b4 = smooshy_lightning_object.get_smooshy_lightning_background_4(grey, black, brown, green, yellow, gold, darkgrey)
    b5 = smooshy_lightning_object.get_smooshy_lightning_background_5(grey, black, brown, green, yellow, gold, darkgrey)
    b6 = smooshy_lightning_object.get_smooshy_lightning_background_6(grey, black, brown, green, yellow, gold, darkgrey)
    b7 = smooshy_lightning_object.get_smooshy_lightning_background_7(grey, black, brown, green, yellow, gold, darkgrey)

    b_list.append(b1)
    b_list.append(b2)
    b_list.append(b3)
    b_list.append(b4)
    b_list.append(b5)
    b_list.append(b6)
    b_list.append(b7)

    return b_list

def get_smooshy_sunny_background(smooshy_lightning_object):
    black = (0, 0, 0)
    lightblue = (173, 216, 230)
    brown = (165, 42, 42)
    green = (0, 128, 0)
    yellow = (255, 255, 0)
    gold = (204,172,0)
    darkgrey = (169, 169, 169)
    grey = (128, 128, 128)

    background = smooshy_lightning_object.get_smooshy_lightning_background_1(lightblue, black, brown, green, yellow, gold, darkgrey)

    return background




"""
bg: background color
ol: outline color
mc: main color
sc: shadow color

"""
for x in range(1, 2):

    # background color (light grey or random?)
    bg = (238, 238, 238)
    # bg = (randint(0, 256), randint(0, 256), randint(0, 256))
    ol = (0, 0, 0)
    mc = (randint(0, 256), randint(0, 256), randint(0, 256))
    sc = (128, 128, 128)

    # image_list = []
    #
    #
    # background_flag, background_list, sc, bg, background_trait_type = background_picker(randint(1,1000))
    #
    # l1 = background_list[0]
    # l2 = background_list[1]
    # l3 = background_list[2]
    # l4 = background_list[3]
    # l5 = background_list[4]
    # l6 = background_list[5]
    # l7 = background_list[6]
    #
    # array1 = np.array(l1, dtype=np.uint8)
    # array2 = np.array(l2, dtype=np.uint8)
    # array3 = np.array(l3, dtype=np.uint8)
    # array4 = np.array(l4, dtype=np.uint8)
    # array5 = np.array(l5, dtype=np.uint8)
    # array6 = np.array(l6, dtype=np.uint8)
    # array7 = np.array(l7, dtype=np.uint8)
    #
    # im1 = Image.fromarray(array1)
    # im2 = Image.fromarray(array2)
    # im3 = Image.fromarray(array3)
    # im4 = Image.fromarray(array4)
    # im5 = Image.fromarray(array5)
    # im6 = Image.fromarray(array6)
    # im7 = Image.fromarray(array7)
    #
    # im1 = im1.resize(dimensions, resample=0)
    # im2 = im2.resize(dimensions, resample=0)
    # im3 = im3.resize(dimensions, resample=0)
    # im4 = im4.resize(dimensions, resample=0)
    # im5 = im5.resize(dimensions, resample=0)
    # im6 = im6.resize(dimensions, resample=0)
    # im7 = im7.resize(dimensions, resample=0)
    #
    # image_list.append(im1)
    # image_list.append(im2)
    # image_list.append(im3)
    # image_list.append(im4)
    # image_list.append(im5)
    # image_list.append(im6)
    # image_list.append(im7)
    # image_list.append(im4)
    # image_list.append(im3)
    # image_list.append(im2)
    #
    # create_background_from_images(image_list, 5)

    attributes_list = []
    attributes_dict1 = {}
    attributes_dict2 = {}
    attributes_dict3 = {}
    attributes_dict4 = {}

    main_color_list = []
    background_list = []
    eye_list = []
    flashy = False
    boots = False
    sunglasses = False
    hat = False
    halo = False
    laser_eyes = False
    background_flag = False

    randint1 = randint(1,1000)
    randint2 = randint(1,1000)
    randint3 = randint(1,1000)
    randint4 = randint(1,1000)
    randint5 = randint(1,1000)
    randint6 = randint(1,1000)
    randint7 = randint(1,1000)
    randint8 = randint(1,1000)
    randint9 = randint(1,1000)

    # Decide if flashy or normal
    main_color_list, color_trait_type = main_color_picker(randint6)
    attributes_dict1["trait_type"] = "Color"
    attributes_dict1["value"] = color_trait_type
    attributes_list.append(attributes_dict1)

    # Decide what kind of background to use
    background_flag, background_list, sc, bg, background_trait_type = background_picker(randint7)
    attributes_dict2["trait_type"] = "Background"
    attributes_dict2["value"] = background_trait_type
    attributes_list.append(attributes_dict2)

    # Decide on type of Eyes
    eye_list, eye_color_trait_type = eye_picker(randint5)
    attributes_dict3["trait_type"] = "Eye Color"
    attributes_dict3["value"] = eye_color_trait_type
    attributes_list.append(attributes_dict3)

    # Decide on accessories
    # 50% chance it has boots
    if randint2 > 500:
        boots = True
    # 25$ chance it has sunglasses or laser eyes
    if randint3 > 750:
        if randint9 > 200:
            sunglasses = True
        else:
            laser_eyes = True
    # 20% chance it has a hat or halo
    if randint4 > 800:
        if randint8 > 500:
            hat = True
        else:
            halo = True

    # 40% generic base smooshy
    if randint1 > 600:
        attributes_dict4["trait_type"] = "Type"
        attributes_dict4["value"] = "Generic"
        attributes_list.append(attributes_dict4)
        generate_basic_smooshies(smooshy_generic_object, background_flag, background_list, x, bg, ol, main_color_list, sc, boots, sunglasses, hat, halo, laser_eyes, eye_list, attributes_list)

    # 20% wavy smooshy
    elif 600 >= randint1 > 400:
        attributes_dict4["trait_type"] = "Type"
        attributes_dict4["value"] = "Wavy"
        attributes_list.append(attributes_dict4)
        generate_wavy_smooshies(smooshy_generic_object, smooshy_wavy_object, background_flag, background_list, x, bg, ol, main_color_list, sc, boots, sunglasses, hat, halo, laser_eyes, eye_list, attributes_list)

    # 15% robot smooshy
    elif 400 >= randint1 > 250:
        attributes_dict4["trait_type"] = "Type"
        attributes_dict4["value"] = "Robot"
        attributes_list.append(attributes_dict4)
        generate_robot_smooshies(smooshy_generic_object, smooshy_robot_object, background_flag, background_list, x, bg, ol, main_color_list, sc, boots, sunglasses, hat, halo, laser_eyes, eye_list, attributes_list)

    # 12% alien smooshy
    elif 250 >= randint1 > 130:
        attributes_dict4["trait_type"] = "Type"
        attributes_dict4["value"] = "Alien"
        attributes_list.append(attributes_dict4)
        generate_alien_smooshies(smooshy_generic_object, smooshy_alien_object, background_flag, background_list, x, bg, ol, main_color_list, sc, boots, sunglasses, hat, halo, laser_eyes, eye_list, attributes_list)

    # 8% monkey smooshy
    elif 130 >= randint1 > 50:
        attributes_dict4["trait_type"] = "Type"
        attributes_dict4["value"] = "Monkey"
        attributes_list.append(attributes_dict4)
        generate_monkey_smooshies(smooshy_generic_object, smooshy_monkey_object, background_flag, background_list, x, bg, ol, main_color_list, sc, boots, sunglasses, hat, halo,laser_eyes, eye_list, attributes_list)

    # 5% punk smooshy
    elif 50 >= randint1 > 0:
        attributes_dict4["trait_type"] = "Type"
        attributes_dict4["value"] = "Punk"
        attributes_list.append(attributes_dict4)
        generate_punk_smooshies(smooshy_generic_object, smooshy_punk_object, background_flag, background_list, x, bg, ol, main_color_list, sc, boots, sunglasses, hat, halo, laser_eyes, eye_list, attributes_list)
