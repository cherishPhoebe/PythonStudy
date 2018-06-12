import pytesseract
from PIL import Image

path = "E:\\SourceCode\\Python\\PythonStudy\\Spider\\test\\"
text = pytesseract.image_to_string(Image.open(path +'image.png'))
print(text)
