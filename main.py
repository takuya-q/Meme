from PIL import Image, ImageDraw, ImageFont
print("Генератор мемов запущен!")
top_text = input("Введите верхний текст мема:")
bottom_text = input("Введите нижний текст мема:")
print(top_text, bottom_text)

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")
x = input("Введите цифру изображения:")
if x == "1":
    ImageFile = "Кот в ресторане.png"
elif x == "2":
    ImageFile = "Кот в очках.png"

image = Image.open(ImageFile)
width, height = image.size

draw = ImageDraw.Draw(image)

font = ImageFont.truetype("arial.ttf", size=70)

text = draw.textbbox((0, 0), top_text, font)
text_width = text[2]

draw.text(((width - text_width) / 2, 10), top_text, font=font, fill="black")

text = draw.textbbox((0, 0), bottom_text, font)
text_width = text[2]
text_height = text[3]

draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, font=font, fill="black")

image.save("new.meme.jpg")