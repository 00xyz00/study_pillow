from PIL import Image, ImageDraw, ImageFont
img1 = "001.jpg"
img2 = "002.jpg"
im1 = Image.open(img1)
im2 = Image.open(img2)
width, height = im1.size
#wi, he = im2.size
#print(im1.size, width, height)
#print(im2.size, wi, he)
#print(im1.mode)
# 生成白底图片，并添加文字
image_wh = Image.new('RGBA', im1.size, 'white')
image_wh.show()
# image_wh.save('005.png','PNG')
print(image_wh.mode)
draw = ImageDraw.Draw(image_wh)
ft = ImageFont.truetype('Arial.ttf', 30)
draw.text((100, 100), u"LYP", font=ft, fill='red')
image_wh.save('006.png','PNG')
# 判断图片类型改变第一张图片的类型
if im1.mode != 'RGBA':
    im1 = im1.convert('RGBA')
# 合并图片
img_out = Image.blend(im1, image_wh, 0.3)
img_out.save('007.png', 'PNG')