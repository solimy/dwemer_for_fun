from PIL import Image, ImageDraw, ImageFont
import click
import re
import pytesseract


__fonts = {
    'normal': 'Dwemer',
    'bold': 'Dwemer Bold',
    'italic': 'Dwemer Italic',
    'italic bold': 'Dwemer Bold Italic',
    'bold italic': 'Dwemer Bold Italic'
}


__chars = ''.join(set(map(chr, [*range(ord('a'), ord('z')+1)] + [*range(ord('A'), ord('Z')+1)])) | set('\n'))


@click.command()
@click.option('--write', 'text_file', default=None, type=str, help='the text to translate.')
@click.option('--font-type', 'font_type', type=click.Choice(__fonts.keys()), default='normal')
@click.option('--font-size', 'font_size', type=int, default=15)
@click.option('--read', 'image_file', default=None, type=str, help='the path to your dwemer image.')
@click.option('--output', 'output_file', default='dwemer', type=str, help='the output file.')
def main(text_file, font_type, font_size, image_file, output_file):
    if text_file:
        text = ''
        with open(text_file) as tf:
            text = tf.read()
        text = re.sub(f'[^{__chars}]', ' ', text)[:-1].split('\n')
        img_width = ((font_size * max(set(map(len, text)))) // 2) + font_size
        img_height = font_size * len(text)
        img = Image.new('RGB', (img_width, img_height), color = (255, 255, 255))
        fnt = ImageFont.truetype(f'font/{__fonts[font_type]}.otf', font_size)
        for line in range(len(text)):
            d = ImageDraw.Draw(img)
            d.text((font_size // 2, line * font_size), text[line], font=fnt, fill=(0, 0, 0))
        img.save(f'{output_file}.png')
    if image_file:
        text = pytesseract.image_to_string(Image.open(image_file), lang='Dwemer', config=r'--tessdata-dir tesseract_data')
        with open(f'{output_file}.txt', 'w') as of:
            of.write(text)


if __name__ == "__main__":
    main()