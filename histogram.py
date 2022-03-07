from PIL import Image


def generate_histogram(image_file_path):
    test_image = Image.open(image_file_path)
    test_image_pixels = list(test_image.getdata())
    gray_value_frequencies = [0 for _ in range(256)]
    for pixel in test_image_pixels:
        gray_value_frequencies[sum(pixel) // 3] += 1
    return gray_value_frequencies


if __name__ == '__main__':
    histogram = generate_histogram('TestImage.jpg')
    print(sum(histogram))
