from PIL import Image, ImageDraw, ImageFont
import click
import pytesseract

__fonts = {
    'normal': 'Dwemer',
    'bold': 'Dwemer Bold',
    'italic': 'Dwemer Italic',
    'italic bold': 'Dwemer Bold Italic',
    'bold italic': 'Dwemer Bold Italic'
}

@click.command()
@click.option('--write', 'text', default=None, type=str, help='the text to translate.')
@click.option('--font-type', 'font_type', type=click.Choice(__fonts.keys()), default='normal')
@click.option('--font-size', 'font_size', type=int, default=15)
@click.option('--read', 'image_file', default=None, type=str, help='the path to your dwemer image.')
@click.option('--output', 'output_file', default='dwemer', type=str, help='the output file.')
def main(text, font_type, font_size, image_file, output_file):
    if text:
        img = Image.new('RGB', (((font_size * len(text)) // 2) + font_size, font_size), color = (255, 255, 255))
        fnt = ImageFont.truetype(f'font/{__fonts[font_type]}.otf', font_size)
        d = ImageDraw.Draw(img)
        d.text((font_size // 2,0), text, font=fnt, fill=(0, 0, 0))
        img.save(f'{output_file}.png')
    if image_file:
        text = pytesseract.image_to_string(Image.open(image_file), lang='Dwemer', config=r'--tessdata-dir tesseract_data')
        with open(f'{output_file}.txt', 'w') as of:
            of.write(text)

if __name__ == "__main__":
    main()