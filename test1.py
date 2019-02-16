from PIL import Image

'''
改变图片尺寸方法1，这个方法会直接将图片的尺寸输出为400*400，改变图片的纵横比
'''
image = Image.open('001.jpg')
print(image.size)   #输出图片大小
new_image = image.resize((400, 400))
new_image.save('001_400.jpg') # 改变图片尺寸为400*400


'''
改变图片尺寸方法2，这个方法会保持图片的纵横比，比较好看
'''
image = Image.open('001.jpg')
print(image.size)   #输出图片大小
new_image2 = image.thunbnail((400, 400))
image.save('new_image2.jpg')


'''
将logo张贴到图片上
'''
image = Image.open('002.jpg')
logo = Image.open('logo.jpg')
image_copy = image.copy()
position = ((image_copy.width - logo.width), (image_copy.height - logo.height))
image_copy.paste(logo, position, logo)
image_copy.save('002_logo.jpg')
