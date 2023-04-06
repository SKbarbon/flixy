






def rgb2hex(r,g,b):
	return "#{:02x}{:02x}{:02x}".format(r,g,b)


def hex_to_rgb(hex_code):
    """
    Converts a hexadecimal color code to its corresponding RGB value.

    Parameters:
    hex_code (str): A string representing a hexadecimal color code (e.g. "#FF0000").

    Returns:
    tuple: A tuple containing the RGB values as floats in the range [0, 1] (e.g. (1.0, 0.0, 0.0)).
    """

    # Remove the "#" symbol if it exists
    if hex_code.startswith("#"):
        hex_code = hex_code[1:]

    # Convert the hexadecimal digits to integers
    red = int(hex_code[0:2], 16) / 255.0
    green = int(hex_code[2:4], 16) / 255.0
    blue = int(hex_code[4:6], 16) / 255.0

    # Return the RGB values as a tuple
    return (red, green, blue)
