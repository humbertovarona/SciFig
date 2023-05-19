def remove_white_borders(image_path, output_path):
    try:
        with Image.open(image_path) as image:
            image = image.convert("RGBA")
            width, height = image.size
            left = width
            right = 0
            top = height
            bottom = 0
            for y in range(height):
                for x in range(width):
                    pixel = image.getpixel((x, y))
                    if pixel[:3] != (255, 255, 255):  # Non-white pixel found
                        if x < left:
                            left = x
                        if x > right:
                            right = x
                        if y < top:
                            top = y
                        if y > bottom:
                            bottom = y
            image = image.crop((left, top, right + 1, bottom + 1))
            new_image = Image.new("RGB", image.size)
            new_image.paste(image, (0, 0))
            output_format = image.format if image.format != "JPEG" else "PNG"
            new_image.save(output_path, format=output_format)
            print(f"Image with removed white borders saved successfully: {output_path}")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except (IOError, OSError) as e:
        print(f"Error encountered when processing the image: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        raise

