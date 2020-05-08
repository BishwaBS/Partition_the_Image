import PIL
from PIL import Image
import numpy as np
import os

class slicer:
    def __init__(self):
        self.row_parts=None
        self.col_parts=None
    def partition(self, image, partitionsize, outputfolder):
        img=Image.open(image)
        img=np.array(img)
        dim_image= partitionsize
        self.row_parts= np.int(img.shape[0]/dim_image)
        self.col_parts=np.int(img.shape[1]/dim_image)
        for i in range(self.row_parts-1):
            for j in range(self.col_parts-1):
                part= img[i*dim_image : (i+1)*dim_image, j*dim_image : (j+1)*dim_image, :]
                initial= i
                final=j
                name= str(initial)+ "_" + str(final)+".JPG"
                part=Image.fromarray(part, mode="RGB")
                path=os.path.join(outputfolder, name)
                part.save(path, "JPEG")
        print("Successfully completed")

