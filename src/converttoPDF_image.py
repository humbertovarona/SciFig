def converttoPDF_image(image_path, output_path, output_format):
    if not os.path.isfile(image_path):
        raise FileNotFoundError(f"The input image file '{image_path}' does not exist.")
    if output_format.lower() not in ["pdf"]:
        raise ValueError("Invalid output format. Only PDF and PS formats are supported.")
    with Image.open(image_path) as image:
        with warnings.catch_warnings():
            warnings.simplefilter("error")
            try:
                image.save(output_path, format=output_format.upper())
                print(f"Image converted successfully to {output_format.upper()}: {output_path}")
            except Warning as warning:
                print(f"Warning: {str(warning)}")
            except OSError as e:
                raise OSError(f"Error encountered when writing the image file: {str(e)}") from e

