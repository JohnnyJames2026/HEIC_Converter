from PIL import Image
import pillow_heif


fileName = input("Insert file name here: ")
fileType = input("Type 'JPEG' or 'PNG' for what file type you would like to convert to: ")

while fileType != "JPEG" and fileType != "PNG":
    print("Incorrect answer format. Try again and follow the answer format stated.")
    fileType = input("Type 'JPEG' or 'PNG' for what file type you would like to convert to: ")
    if fileType == "JPEG" or fileType == "PNG":
        break

#converts the HEIC into readable data for Pillow
heif = pillow_heif.open_heif(fileName)

#pillowImage is now an Image object from PIL
pillowImage = heif.to_pillow()

#image is now saved as another file format
pillowImage.save(f"{fileName[:-5]}.{fileType.lower()}", fileType)
