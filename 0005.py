from PIL import Image
import os, glob

def resizeImgInFolder(folder, maxHeight = 1136 , maxWidth = 640):
    try:
        for file in glob.glob(folder):
            fullPath = os.path.join(folder, file)
            if os.path.isfile(fullPath):
                im = Image.open(fullPath)
                width, height = im.size
                if height > maxHeight or width > maxWidth:
                    heightRate = height / maxHeight
                    widthRate = width / maxWidth
                    finalRate = max(heightRate, widthRate)
                    newHeight = int(height / finalRate)
                    newWidth = int(width / finalRate)
                    im = im.resize((newWidth, newHeight))
                    im.save(fullPath)
        print("Done!")
    except:
        pass
