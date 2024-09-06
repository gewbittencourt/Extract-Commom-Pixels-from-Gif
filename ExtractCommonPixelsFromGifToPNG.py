from PIL import Image, ImageChops
def main(gif_path, output_png_path):
    gif = Image.open(gif_path)
    frames = []
    try:
        while True:
            frames.append(gif.convert("RGBA").copy())
            gif.seek(len(frames))
    except EOFError:
        pass

    width, height = frames[0].size

    common_pixels_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    pixels_common = common_pixels_image.load()

    for x in range(width):
        for y in range(height):
            first_pixel = frames[0].getpixel((x, y))
            is_common = True
            for frame in frames[1:]:
                if frame.getpixel((x, y)) != first_pixel:
                    is_common = False
                    break
            if is_common:
                pixels_common[x, y] = first_pixel


    common_pixels_image.save(output_png_path, "PNG")
    print(f"PNG successfully created: {output_png_path}")


gif_path = 'C:/test/Alicorn_Ring.gif'  #
output_bmp_path = 'C:/test/output.png'
main(gif_path, output_bmp_path)
