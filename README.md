# Image_Steganography

Steganography applied to conceal audio files inside a PNG image.

-------
## Description
This script allows to conceal audio files inside png images, using a well known steganographic method: hide the data in the least significant bits of an image pixels.
This produces little changes to the image that usually aren't noticed by just looking at the image.

## Usage

The script usage:

```
usage: main.py [-h] [-e | -d] [-i IMAGE] [-f FILE] [-o OUTPUT] [-t] [-k]

Conceal audio files inside a PNG image and extract them back

optional arguments:
  -h, --help            show this help message and exit
  -e, --encode          If present the script will conceal the file in the
                        image and produce a new encoded image
  -d, --decode          If present the script will decode the concealed data
                        in the image and produce a new file with this data
  -i IMAGE, --image IMAGE
                        Path to an image to use for concealing or file
                        extraction
  -f FILE, --file FILE  Path to the audio file to conceal or to extract
  -t                    Type of decoder (wav or mp3)
  -k			Key used to decode file
  

```

## Example

We could encode a simple audio file like `taunt.wav`:
```
This script is working!!!
```

Running the script like:
```
$ python3 main.py -e -i EncodingSamples/Images/test.jpg -f EncodingSamples/Sound/taunt.wav


```

The result is an encoded image which looks identical to the original:

![Original Image](EncodingSamples/Images/test.jpg) | ![Encoded Image](EncodedSamples/Encoded.png)
Original Audio File:-(EncodingSamples/Sound/taunt.wav) | Decoded Audio File:-(DecodedSamples/Decode.wav)
|:---:|:---:|
| Original | Encoded |

From the encoded image we can extract the Audio file:
```
$ python3 main.py -d -i EncodedSamples/Encoded.png -k 729928 -t wav
```

## Future developements
Maybe implement a GUI.
