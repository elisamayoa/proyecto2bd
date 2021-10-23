import base64

def byteas():
    foto = 'C:\\Users\\elisa\\Desktop\\UVG\\Semestre IV\\Bases de datos\\Proyecto 2\\womanpic.jpg'
    with open(foto, 'rb') as f:
        filedata = base64.b64encode(f.read())
    return filedata

def foto_women():
    fotobytes=byteas()
    x=base64.b64decode(fotobytes)
    with open('imgw.png','wb') as f:
        f.write(x)

foto_women()
cv2.imshow('Logo OpenCV',imagen)