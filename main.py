import Files.audioObj as au
import Files.imgObj as im
import argparse
import os


def main(args):
    """Main fuction of the script"""
    if args.image is not None and args.file is not None:
        if args.encode:
            img_path = args.image
            file_path = args.file
            if not os.path.isfile(img_path):
                print("Image file does not exist")
                return
            if not os.path.isfile(file_path):
                print("File does not exist")
                return

            conv = au.audioObj()

            # unpacking the tuple
            file_name, file_extension = os.path.splitext(file_path)
            if file_extension == '.wav':
                bits_array = conv.wavtobits(file_path)


            elif file_extension == '.mp3':
                bits_array = conv.mp3tobits(file_path)

            print(len(bits_array))
            img = im.imgObj()
            img.encode(img_path,bits_array)
            
            return

    if args.image:
        if args.decode:
            if args.type:
                img_path = args.image
                if not os.path.isfile(img_path):
                    print("Image file does not exist")
                    return
                key = int(args.key)
                img = im.imgObj()
                s = img.decode(img_path,key)
                conv = au.audioObj()
                if args.type == 'wav':

                    conv.bitstowav(s)
                    print("Image decoded")
                    return

                elif args.type == 'mp3':

                    conv.bitstomp3(s)
                    print("Image decoded")
                    return
            else:
                print("Error,Type of decoder not specified.")



        print("Error, no action specified!")
        return

    print("Error, image or file not specified")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Conceal small files inside a PNG image and extract them back')
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-e',
        '--encode',
        help='If present the script will conceal the file in the image and produce a new encoded image',
        action="store_true")
    group.add_argument(
        '-d',
        '--decode',
        help='If present the script will decode the concealed data in the image and produce a new file with this data',
        action="store_true")
    parser.add_argument(
        '-i',
        '--image',
        help='Path to an image to use for concealing or file extraction')
    parser.add_argument(
        '-f',
        '--file',
        help='Path to the file to conceal or to extract')
    parser.add_argument(
        '-k',
        '--key',
        help='Key needed for decoding the encoded file.',
        )
    parser.add_argument(
        '-t',
        '--type',
        help='Decide type of decoder',
        )

    main(parser.parse_args())




#python3 main.py -e -i EncodingSamples/Images/pic1.jpg -f EncodingSamples/Sound/taunt.wav
#python3 main.py -d -i EncodedSamples/Encoded.png -k 729928 -t wav

#python3 main.py -e -i EncodingSamples/Images/pic1.jpg -f EncodingSamples/Sound/PinkPanther30.wav
#python3 main.py -d -i EncodedSamples/Encoded.png -k 5292008 -t wav

#python3 main.py -e -i EncodingSamples/Images/pic1.jpg -f EncodingSamples/Sound/sample-6s.mp3
#python3 main.py -d -i EncodedSamples/Encoded.png -k 4509704 -t mp3

#python3 main.py -e -i EncodingSamples/Images/pic3.png -f EncodingSamples/Sound/taunt.wav
#python3 main.py -d -i EncodedSamples/Encoded.png -k 729928 -t wav

#python3 main.py -e -i EncodingSamples/Images/pic3.png -f EncodingSamples/Sound/sample-6s.mp3