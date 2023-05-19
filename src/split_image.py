def split_image(image_path, output_dir, num_parts):
    try:
        image = Image.open(image_path)
        width, height = image.size
        if num_parts % 2 != 0:
            raise ValueError("Number of parts must be even.")
        part_width = width // (num_parts // 2)
        part_height = height // 2
        for i in range(num_parts):
            left = (i % (num_parts // 2)) * part_width
            upper = (i // (num_parts // 2)) * part_height
            right = left + part_width
            lower = upper + part_height
            part = image.crop((left, upper, right, lower))
            extension = image_path.split(".")[-1]
            part_number = str(i + 1).zfill(2)
            output_filename = f"{part_number}_part.{extension}"
            output_path = os.path.join(output_dir, output_filename)
            part.save(output_path)
        print(f"Image split into {num_parts} parts successfully.")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except (IOError, OSError) as e:
        print(f"Error encountered when processing the image: {str(e)}")
    except ValueError as e:
        print(f"Invalid input: {str(e)}")
    except Exception as e:
        print(f"Unexpected error occurred: {str(e)}")
        raise

