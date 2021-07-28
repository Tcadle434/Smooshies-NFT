import json

dirname = str(r"C:\Users\thoma\Documents\Blog\TopShot and NFTs\Smooshies\Smooshies_App")

image_url = "https://gateway.pinata.cloud/ipfs/QmbRYMbDcJuw6623hRQQRPucmxB5LwpHMQYnD1n6knHoxP/"


for x in range(1, 10000):
    with open(dirname + '/metadata/' + str(x) + '.json') as f:
        data = json.load(f)

    data['image'] = image_url + str(x) + '.gif'

    with open(dirname + '/metadata-final/' + str(x), 'w') as f:
        json.dump(data, f, indent=2)