# python code for encryption

#take path of image as a input
path = r'C:\Users\vijay\Desktop\image encryption\image.avif'

#taking encrption key as input
key = int(input('Enter key for encrptionn of image : '))

#print path of image file and encrption key that we are using
print('The path of file : ',path)
print('key for encryption : ',key)

#open file for reading purpose
fin = open(path, 'rb')

#storing image data in variable "image"
image = fin.read()
fin.close()

#converting image into byte array to perform encryption easily on numeric data
image = bytearray(image)

#performing xor operation on each value of bytearray
for index, values in enumerate(image):
        image [index] = values ^ key

#opening file for writing purpose
fin = open(path, 'wb')

#writing encrpted sata in image
fin.write(image)
fin.close()
print('encryption done...')
