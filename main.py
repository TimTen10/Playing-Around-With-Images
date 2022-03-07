class JPEG:

    def __init__(self, image_file_path):
        with open(image_file_path, 'rb') as image:
            # read all bytes into data
            self.data = image.read()


def main():
    test_image = JPEG('TestImage.jpg')
    print(test_image.data[:2])


if __name__ == '__main__':
    main()
