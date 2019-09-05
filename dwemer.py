from PIL import Image, ImageDraw, ImageFont
import click

__fonts = {
    'normal': 'Dwemer',
    'bold': 'Dwemer Bold',
    'italic': 'Dwemer Italic',
    'italic bold': 'Dwemer Bold Italic',
    'bold italic': 'Dwemer Bold Italic'
}

@click.command()
@click.option('--write', 'text', default=None)
@click.option('--font-type', 'font_type', type=click.Choice(__fonts.keys()), default='normal')
@click.option('--font-size', 'font_size', type=int, default=15)
def main(text, font_type, font_size):
    if not text:
        return
    img = Image.new('RGB', (((font_size * len(text)) // 2) + font_size, font_size), color = (255, 255, 255))
    fnt = ImageFont.truetype(f'font/{__fonts[font_type]}.otf', font_size)
    d = ImageDraw.Draw(img)
    d.text((font_size // 2,0), text, font=fnt, fill=(0, 0, 0))
    img.save('dwemer.png')

if __name__ == "__main__":
    main()