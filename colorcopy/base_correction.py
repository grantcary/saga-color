import media_parse

image_path = 'D:/Pix/Favorite/IMG_7669.JPEG'
w, h, rgb, luma = media_parse.imageparse(image_path)
print(w, h)
print(rgb, len(rgb))
print(luma, len(luma))