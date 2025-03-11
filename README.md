# Python Steganography

This Python project allows you to hide a text message inside an image file using steganography techniques. The text message is encoded into the least significant bits (LSB) of the image pixels, making the change imperceptible to the human eye. The code also provides a method to decode the hidden message from the image.

## Features

- **Hide Text in an Image**: Encode any text into an image by altering the least significant bits of the pixel values.
- **Retrieve Hidden Message**: Extract the hidden message from the image with the provided decoding function.
- **Message Length Encoding**: The length of the hidden message is stored in the image to ensure correct decoding, preventing the extraction of garbage data.

## Requirements

To run this code, you need Python and the `Pillow` library installed. You can install Pillow with the following command:

```bash
pip install Pillow
```

## How to Use
**1. Encoding Text into an Image**

The encode_image function takes an input image file and a text string and generates a new image with the hidden message. The length of the message is encoded into the image to help with decoding later.

Inputs:
- `image_path`: Path to the input image where you want to hide the text.
- `text`: The text message you want to hide.
- `output_image_path`: Path where the modified image with the hidden message will be saved.
Run the script:
```bash
python steganography.py
```
You will be prompted to enter:

- Image path (e.g., `input_image.png`).
- The text to hide (e.g., `"This is a secret message!"`).
- Output image path (e.g., `output_image.png`).

**2. Decoding the Hidden Message**

The decode_image function extracts the hidden message from the modified image. It first reads the encoded length of the message and then decodes the actual hidden message.
After running the encoding script, you can test the decoding by loading the image you just created:
```bash
python steganography.py
```
The script will automatically decode the message from the image and print the result.

## Example Usage

**Encoding Example:**

```bash
Enter the image path: input_image.png
Enter the text to hide: This is a secret message!
Enter the output image path: output_image.png
```

**Decoding Example:**

```bash
Decoded message: This is a secret message!
```
##How It Works

**Encoding:**

- Convert the input text into a binary string.
- Store the length of the binary string (in 16 bits) at the beginning of the binary message.
- Embed the binary message into the least significant bits (LSB) of the image pixels.
- Save the new image with the embedded message.

**Decoding:**

- Extract the first 16 bits to determine the length of the hidden message.
- Extract the corresponding number of bits from the image.
- Convert the binary string back into the original text message.
  
**Limitations**
  
- The text message's size must be small enough to fit within the image. If the image doesn't have enough pixels to hide the message, you will encounter errors or truncation.
- The quality of the image may be slightly altered due to the modifications in pixel values, but it will be imperceptible to the human eye.
