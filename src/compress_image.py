def compress_image(image_path, quality=80):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"The image file '{image_path}' does not exist.")
    if not image_path.lower().endswith(('.png', '.tiff')):
        raise ValueError("Unsupported image format. Only PNG and TIFF formats are supported.")
    with Image.open(image_path) as image:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            try:
                compressed_image_path = os.path.splitext(image_path)[0] + "_compressed" + os.path.splitext(image_path)[1]
                image.save(compressed_image_path, format=image.format, optimize=True, quality=quality)
            except Warning as warning:
                print(f"Warning: {str(warning)}")

