from PIL import Image, ImageDraw, ImageFilter

PATH_TO_IMAGE = "image.jpg"
LINE_COLOR = (255, 255, 0, 150)
LINE_SIZE = 500
BLUR_RADIUS = 5


image = Image.open(PATH_TO_IMAGE)

mask = Image.new("L", image.size)
draw = ImageDraw.Draw(mask)
draw.line(((0, 0), image.size), 255, LINE_SIZE)

blur_image = image.filter(ImageFilter.GaussianBlur(BLUR_RADIUS))

final_image = Image.new("RGB", image.size)
final_image.paste(blur_image)
final_image.paste(image, mask=mask)
draw = ImageDraw.Draw(final_image, 'RGBA')
draw.line(((0, 0), image.size), LINE_COLOR, LINE_SIZE)

final_image.show()
