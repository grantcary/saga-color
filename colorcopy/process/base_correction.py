import parse.media_parse as mp

image_path = 'D:/Pix/Favorite/IMG_7669.JPEG'
w, h, rgb, luma = mp.imageparse(image_path)
print(w, h)
print(rgb, len(rgb))
print(luma, len(luma))