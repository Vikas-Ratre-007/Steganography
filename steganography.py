from PIL import Image
import binascii

def text_to_bin(text):
    """Convert text to binary"""
    binary = ''.join(format(ord(c), '08b') for c in text)
    return binary

def encode_image(image_path, text, output_image_path):
    # Convert the text to binary
    binary_text = text_to_bin(text)
    message_length = len(binary_text)  # Get the length of the message
    
    # Convert the message length to binary (16 bits for length)
    binary_length = format(message_length, '016b')
    
    # Add the length at the start of the binary text
    binary_text = binary_length + binary_text

    # Open the image
    image = Image.open(image_path)
    data_index = 0

    # Get image data
    pixels = image.load()

    for i in range(image.width):
        for j in range(image.height):
            # Get the pixel value (R, G, B)
            pixel = list(pixels[i, j])

            for color in range(3):  # Iterate over Red, Green, and Blue channels
                if data_index < len(binary_text):
                    # Modify the least significant bit (LSB)
                    pixel[color] = pixel[color] & ~1 | int(binary_text[data_index])
                    data_index += 1

            # Update the pixel
            pixels[i, j] = tuple(pixel)

            # Stop if the message has been encoded
            if data_index >= len(binary_text):
                break
        else:
            continue
        break

    # Save the modified image
    image.save(output_image_path)
    print(f"Image saved to {output_image_path}")

def decode_image(image_path):
    # Open the image
    image = Image.open(image_path)
    pixels = image.load()
    binary_message = ""

    for i in range(image.width):
        for j in range(image.height):
            # Get the pixel value (R, G, B)
            pixel = pixels[i, j]

            for color in range(3):  # Iterate over Red, Green, and Blue channels
                # Extract the least significant bit (LSB)
                binary_message += str(pixel[color] & 1)

    # Get the length of the hidden message (first 16 bits)
    message_length = int(binary_message[:16], 2)
    binary_message = binary_message[16:]  # Remove the length part

    # Extract the actual message (based on the length of the message)
    message_binary = binary_message[:message_length]
    message = ""

    # Convert the binary message back to text
    for i in range(0, len(message_binary), 8):
        byte = message_binary[i:i + 8]
        if len(byte) < 8:
            break
        message += chr(int(byte, 2))

    return message

if __name__ == "__main__":
    image_path = input("Enter the image path: ")
    text_to_hide = input("Enter the text to hide: ")
    output_image_path = input("Enter the output image path: ")

    encode_image(image_path, text_to_hide, output_image_path)
    print("Text encoded in the image.")

    # To test decoding
    decoded_message = decode_image(output_image_path)
    print("Decoded message:", decoded_message)