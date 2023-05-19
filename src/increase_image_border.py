def increase_image_border(image_path, output_path, color, border_width):
    try:
        with Image.open(image_path) as image:
            width, height = image.size
            new_width = width + 2 * border_width
            new_height = height + 2 * border_width
            if image.mode == "RGBA":
                image = image.convert("RGB")
            new_image = Image.new("RGB", (new_width, new_height), color)
            new_image.paste(image, (border_width, border_width))
            new_image.save(output_path, format="JPEG")  # Save as JPEG
            print(f"Image with increased border saved successfully: {output_path}")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except (IOError, OSError) as e:
        print(f"Error encountered when processing the image: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        raise

