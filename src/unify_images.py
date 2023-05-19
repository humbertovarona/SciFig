def unify_images(directory, output_image_name, tile_size):
    try:
        image_files = [file for file in os.listdir(directory) if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        if not image_files:
            raise ValueError("No image files found in the directory.")
        image_files.sort(key=lambda x: int(x[:2]))
        first_image_path = os.path.join(directory, image_files[0])
        first_image = Image.open(first_image_path)
        image_format = first_image.format
        image_mode = first_image.mode
        tile_width, tile_height = tile_size
        num_images = len(image_files)
        output_width = first_image.width * tile_width
        output_height = first_image.height * tile_height
        output_image = Image.new(image_mode, (output_width, output_height), (255, 255, 255))
        for i, image_file in enumerate(image_files):
            image_path = os.path.join(directory, image_file)
            image = Image.open(image_path)
            x = (i % tile_width) * first_image.width
            y = (i // tile_width) * first_image.height
            output_image.paste(image, (x, y))
        output_image.save(output_image_name, format=image_format)
        if num_images < tile_width * tile_height:
            remaining_space = (num_images % tile_width, num_images // tile_width)
            remaining_x = remaining_space[0] * first_image.width
            remaining_y = remaining_space[1] * first_image.height
            remaining_box = (remaining_x, remaining_y, output_width, output_height)
            remaining_image = Image.new(image_mode, (output_width - remaining_x, output_height - remaining_y), (255, 255, 255))
            output_image.paste(remaining_image, remaining_box)
        print("Unified image saved successfully.")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except (IOError, OSError) as e:
        print(f"Error encountered when processing the image: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        raise

