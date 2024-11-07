
import cv2
import pandas as pd
import requests

img_path = 'classified_fits/top/shirt_1.jpg'

img = cv2.imread(img_path)

clicked = False

r = g = b = x_pos = y_pos = 0

index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
csv = pd.read_csv('colors.csv', names=index, header=None)

'''
def get_color(R, G, B):
    minimun = 1000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i,'R'])) + abs(R - int(csv.loc[i,'G'])) + abs(R - int(csv.loc[i,'B']))
        if d <= minimun:
            minimun = d
            color = csv.loc[i, 'color_name']
    return color
'''
def get_color(r,g,b):
    # API URL (this is an example, check the documentation for any specific API you want to use)
    url = f'https://www.thecolorapi.com/id?rgb=rgb({r},{g},{b})'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        color_name = data['name']['value']
        return color_name
    else:
        return "Color name not found"
def draw(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b , g, r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw)

while True:
    
    cv2.imshow('image',img)
    
    if clicked:

        cv2.rectangle(img, (20,20), (750, 60), (b,g,r), -1)
        print(r,g,b)
        
        text = get_color(r,g,b)

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

print(text)
cv2.destroyAllWindows()

