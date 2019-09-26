def create_map(students):
    from PIL import Image, ImageDraw, ImageFont
 
    img = Image.new('RGB', (1000, 400), color = (255, 255, 255))
    fnt = ImageFont.truetype(r'C:\Users\roykc\Anaconda3\Lib\site-packages\matplotlib\mpl-data\fonts\ttf\cmr10.ttf', 15)
    d = ImageDraw.Draw(img)
    
    #draws the unused table
    x = 410
    y = 10
    d.rectangle([x, y, x+180, y+80], fill=None, outline=(0, 0, 0))
    d.line([x, y, x+180, y+80], fill="black", width=1)
    d.line([x, y+80, x+180, y], fill="black", width=1)

    #draws the rest of the tables and names
    x = 10
    y = 10
    counter = 0
    while (y < 400):
        x = 10
        while (x < 1000):
            if not((y == 310 and x == 10) or (x == 410 and y == 10)): #skips on the un used tables
                try:
                    name = students[counter].split(" ")
                    name = name[0] + '\n' + name[1]
                except:
                    name = ''
                d.rectangle([x, y, x+180, y+80], fill=None, outline=(0, 0, 0))
                d.text([x+5, y+5], name, fill = (0,0,0), font=fnt)

                x += 100
                counter += 1

                try:
                    name = students[counter].split(" ")
                    name = name[0] + '\n' + name[1]
                except:
                    name = ''
                d.text([x+5, y+5], name, fill = (0,0,0), font=fnt)

                counter += 1
                x += 100
            else: x += 200
        y += 100
    
        
    img.save('pil_text_font.png')
