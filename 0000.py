from PIL import Image, ImageDraw, ImageFont, ImageEnhance

FONT = 'Arial.ttf'

def addTextWaterMark(imgFile, wmText, fontSize, pos, output='watermarked.jpg', angle=23, opacity=0.25, fg_color=(255,0,0)):
    img = Image.open(imgFile).convert('RGB')
    mark = Image.new('RGBA', img.size, (0,0,0,0))
    n_font = ImageFont.truetype(FONT, fontSize)
    n_width, n_height = n_font.getsize(wmText)
    w, h = img.size
    
    if pos == 'top-right':
        box = (w-n_width, 0, w, n_height)
    elif pos == 'top-left':
        box = (0, 0, n_width, n_height)
    elif pos == 'bottom-right':
        box = (w-n_width, h-n_height, n_width, n_height)
    else:
        box = (0, height-n_height, n_width, height)
    
    draw = ImageDraw.Draw(mark, 'RGBA')
    draw.text(box, wmText, fill=fg_color, font = n_font)
    mark = mark.rotate(angle, Image.BICUBIC)
    alpha = mark.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    mark.putalpha(alpha)
    Image.composite(mark, img, mark).save(output, 'JPEG')

addTextWaterMark("20151002223149.png", "4", 30, "top-right","watermarked.jpg", 0, 1)
