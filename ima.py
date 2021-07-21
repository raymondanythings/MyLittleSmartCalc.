from PIL import Image

image1 = Image.open('covid.png')

image1 = image1.resize((20, 20))

image1.save("covid_1.png")
