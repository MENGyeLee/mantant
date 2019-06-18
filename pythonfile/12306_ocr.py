from PIL import Image
import pytesseract


im = Image.open('captcha.jpg')
gray = im.convert('L')
gray.show()
gray.save("captcha_gray.jpg")
threshold = 150
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = gray.point(table, '1')
out.show()
out.save("captcha_thresholded.jpg")

th = Image.open('captcha_thresholded.jpg')
print(pytesseract.image_to_string(th))

