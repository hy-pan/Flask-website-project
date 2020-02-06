from PIL import Image
import os
import sys

print(sys.argv[1])
img = Image.open(os.path.join('/root','web_project_phy','static','processed','picture_processed'))
img.save(os.path.join('/root','web_project_phy','static','storage','0000' + format(str(sys.argv[1]), '0>3s') + '.jpg'))

