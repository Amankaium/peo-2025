cat_image = [
    [[255, 0, 0], [130, 130, 130], [255, 255, 255]],
    [[255, 0, 0], [130, 130, 130], [255, 255, 255]],
    [[255, 0, 0], [130, 130, 130], [255, 255, 255]],
    [[255, 0, 0], [130, 130, 130], [255, 255, 255]],
    [[255, 0, 0], [130, 130, 130], [255, 255, 255]],
]

for i in range(5):
    for m in range(3):
        for n in range(3):
            print(cat_image[i][m][n])

for ryad in cat_image:
    for pixel in ryad:
        for lamp in pixel:
            print(lamp)
