try:
    #take path of image as a input
    path = r'C:\Users\vijay\Desktop\image encryption\image.avif'
    #taking decryption key as input
    key =int(input('Enter key for decryption of image :'))

    #print path of image file and decrption key that we are using
    print('The path of file :',path)
    print('Note : Encryption and decryption keys must be same.')
    print('key for decryption:',key)

    #open file for reading purpose
    fin = open(path,'rb')

    #storing image data in variable "image"
    image = fin.read()
    fin.close()

    #converting image into byte array to perform decrtption easily on numeric data
    image = bytearray(image)

    #performing xor operation on each value of bytearray
    for index, values in enumerate(image):
        image[index]= values ^ key

        
    #opening file for writing purposee
    fin = open(path, 'wb')

    #writing decryption data in image
    fin.write(image)
    fin.close()
    print('decryption done....')


except Exception:
    print('Error caught: ', exception.__name__)
    
