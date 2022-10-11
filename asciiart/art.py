from PIL import Image
import argparse


def make_art():
    #img_arg = "../../../Sandbox/ascii-art/dog.jpeg"
    img_arg = get_input()
    pixels, size = open_image(img_arg)

    ascii_chars = "@%#&%*+=>:-.` "
    len_ac = len(ascii_chars)
    i = 0
    d = 2

    for y in range(0, size[1], d*2):
        for x in range(0, size[0], d):
            i += 1
            pixel = pixels[x, y]
            print(ascii_chars[int(len_ac * (pixel / 256))], end="")
        print()


def open_image(img_arg):
    image = Image.open(img_arg).convert("L")
    pixels = image.load()
    size = image.size
    return (pixels, size)


def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_image', nargs=1)
    args = parser.parse_args()
    return args.input_image[0]

if __name__ == "__main__":
    make_art()


