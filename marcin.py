import tkinter as tk
import tkinter.filedialog
import pygame as pg
import random, cv2, pyglet
import copy
SCREENSIZE = (400, 400) #def screen size
pyglet.font.add_file('Senobi-Gothic-Bold.ttf') #font
FONTNAME = 'Senobi-Gothic-Bold.ttf'
DATA_SIZE = (300,250)
FILE = r'C:\select_file.jpg'
class Menu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x260")
        self.window.title("Put-45")
        self.window.resizable(False,False)
        #menu
        self.menu = tk.Menu(self.window)
        self.menu.add_command(label="Open", command=self.open_file)
        self.menu.add_command(label="Convert", command=self.convert)
        #self.menu.add_command(label="Save", command=self.save_file)
        #entry text 1-number of disruptions, 2-sign size, 3-area width, 4-area height
        self.var1 = tk.StringVar()
        self.var2 = tk.StringVar()
        self.var3 = tk.StringVar()
        self.var4 = tk.StringVar()
        self.var5 = tk.StringVar()
        self.var6 = tk.StringVar()
        self.var7 = tk.StringVar()
        self.var8 = tk.StringVar()
        self.var11 = tk.StringVar()
        self.var12 = tk.StringVar()
        #self.var9 = tk.StringVar()
        # preset values in inserts
        self.var1.set("green")
        self.var2.set("True")
        self.var3.set("green")
        self.var4.set("20")
        self.var5.set("12")
        self.var6.set("7")
        self.var7.set("11")
        self.var8.set("True")
        self.var9 = "File director"
        self.var11.set("23.98")
        self.var12.set("10")
        #variables
        self.var1btn1 = tk.Radiobutton(self.window, variable=self.var1, value="green", text="Green").grid(row=0, column=1)
        self.var1btn2 = tk.Radiobutton(self.window, variable=self.var1, value="pink", text="Pink").grid(row=0, column=2)

        self.var2btn1 = tk.Radiobutton(self.window, variable=self.var2, value="True", text="Enable").grid(row=1, column=1)
        self.var2btn2 = tk.Radiobutton(self.window, variable=self.var2, value="False", text="Disable").grid(row=1, column=2)

        self.var3btn1 = tk.Radiobutton(self.window, variable=self.var3, value="green", text="Green").grid(row=2, column=1)
        self.var3btn2 = tk.Radiobutton(self.window, variable=self.var3, value="pink", text="Pink").grid(row=2, column=2)

        self.entry4 = tk.Entry(self.window, textvariable=self.var4).grid(row=3, column=1)
        self.entry5 = tk.Entry(self.window, textvariable=self.var5).grid(row=4, column=1) 
        self.entry6 = tk.Entry(self.window, textvariable=self.var6).grid(row=5, column=1)
        self.entry7 = tk.Entry(self.window, textvariable=self.var7).grid(row=6, column=1)
        self.var8btn1 = tk.Radiobutton(self.window, variable=self.var8, value="True", text="Enable").grid(row=7, column=1)
        self.entry11 = tk.Entry(self.window, textvariable=self.var11).grid(row=8, column=1)
        self.entry12 = tk.Entry(self.window, textvariable=self.var12).grid(row=9, column=1)
        self.labelvar9 = tk.Label(self.window, text=self.var9).place(x=0,y=235)
        #labels
        self.label1 = tk.Label(self.window, text="Sign color").grid(row=0, column=0)
        self.label2 = tk.Label(self.window, text="Disruption").grid(row=1, column=0)
        self.label3 = tk.Label(self.window, text="Dis. color").grid(row=2, column=0)
        self.label4 = tk.Label(self.window, text="Dis. number").grid(row=3, column=0)
        self.label5 = tk.Label(self.window, text="Sign size").grid(row=4, column=0)
        self.label6 = tk.Label(self.window, text="Sign width").grid(row=5, column=0)
        self.label7 = tk.Label(self.window, text="Sign height").grid(row=6, column=0)
        self.label8 = tk.Label(self.window, text="Tag").grid(row=7, column=0)
        self.label9 = tk.Label(self.window, text="Video FPS").grid(row=8, column=0)
        self.label10 = tk.Label(self.window, text="JPG -> AVI").grid(row=9, column=0)

        self.window.config(menu=self.menu, width=100, height=35)
        self.window.mainloop()

    def open_file(self): #upload graphic file function
        self.filename = tk.filedialog.askopenfilename(filetypes=[("Graphic and Video file", "*.jpg;*.png;*.mp4")])  # open file command
        self.var9 = str(self.filename) + "                                 "
        self.var10 = str(self.filename).split('.')[-1]
        self.filetype = self.var10.lower()
        self.labelvar9 = tk.Label(self.window, text=self.var9).place(x=0,y=235)
        print(self.filename)
        print(self.var10)

    def convert(self): #calling converting function
        print("Converting file, please wait.")
        self.maker = Maker(self)
        self.maker.new()
        self.maker.run()
        

    def save_file(self): #save file function
        self.maker.playing = False
        self.filename2 = tk.filedialog.asksaveasfilename(filetypes=[("Graphic file", "*.jpg;*.png")],defaultextension="*.jpg")  # wywołanie okna dialogowego save file
        pg.image.save(self.maker.screen, self.filename2)
        #print(self.filename2)

class Maker(object):
    def __init__(self, menu):
        self.menu = menu
        self.color = self.menu.var1.get()
        self.var2 = self.menu.var2.get()
        self.var3 = self.menu.var3.get()
        self.raindrop = int(self.menu.var4.get())
        self.fontsize = int(self.menu.var5.get())
        self.fontwidth = int(self.menu.var6.get())
        self.fontheight = int(self.menu.var7.get())
        self.fps = float(self.menu.var11.get())
        self.frames = float(self.menu.var12.get())
        self.var8 = self.menu.var8.get()
        self.filename = self.menu.filename
        self.filetype = self.menu.filetype
        self.count = 0
        self.counting = 0
        self.raingen = True

        if self.filetype == "mp4":
            self.var8 = "False"
            self.vidcap = cv2.VideoCapture(self.filename)
            success,image = self.vidcap.read()
            while success:
                cv2.imwrite("%d.jpg" % self.count, image)     # save frame as JPEG file
                success,image = self.vidcap.read()
                print ('Read a new frame: ', success)
                self.count += 1
        else:
            self.count = 1

        #definiting value of colors
        if self.var3 == "green":
            self.raincolor = (100, 250, 100)
        if self.var3 == "pink":
            self.raincolor = (250, 120, 220)

        if self.var2 == "True":
            self.makegif = True
        if self.var2 == "False":
            self.makegif = False

        if self.var8 == "True":
            self.tagval = True
        if self.var8 == "False":
            self.tagval = False

        pg.init()
        pg.font.init()
        pg.display.set_caption('Preview - do not close')

        self.clock = pg.time.Clock()
        self.gamefont = pg.font.Font(FONTNAME, self.fontsize)
        self.charlist = [
            "あ", "ぃ", "い", "ぅ", "う", "ぇ", "え", "ぉ", "お", "か", "が", "き", "ぎ", "く", "ぐ", "け", "げ", "こ", "ご", "さ",
            "ざ", "し", "じ", "す", "ず", "せ", "ぜ", "そ", "ぞ", "た", "だ", "ち", "ぢ", "っ", "つ", "づ", "て", "で", "と", "ど",
            "な", "に", "ぬ", "ね", "の", "は", "ば", "ぱ", "ひ", "び", "ぴ", "ふ", "ぶ", "ぷ", "へ", "べ", "ぺ", "ほ", "ぼ", "ぽ",
            "ま", "み", "む", "め", "も", "ゃ", "や", "ゅ", "ゆ", "ょ", "よ", "ら", "り", "る", "れ", "ろ", "ゎ", "わ", "ゐ", "ゑ",
            "を", "ん", "ゔ", "ゕ", "ゖ", "ゞ", "ゟ", "ァ", "ア", "ィ", "イ", "ゥ", "ウ", "ェ", "エ", "ォ", "オ", "カ", "ガ", "キ",
            "ギ", "ク", "グ", "ケ", "ゲ", "コ", "ゴ", "サ", "ザ", "シ", "ジ", "ス", "ズ", "セ", "ゼ", "ソ", "ゾ", "タ", "ダ", "チ",
            "ヂ", "ッ", "ツ", "ヅ", "テ", "デ", "ト", "ド", "ナ", "ニ", "ヌ", "ネ", "ホ", "ぁ"]
        self.newtext = []
        self.scrdis = []
        self.img = []
        self.imgold = []
        self.imgvalue = []
        self.droplist = []
        self.rend = 0
        self.load_data()
        print(self.count)

    def load_file(self):
        self.imgvalue = []
        self.scrdis = []
        if self.filetype == "mp4":
            self.image = cv2.imread(str(self.counting) + ".jpg")
        else: 
            self.image = cv2.imread(self.filename)

        self.height, self.width = self.image.shape[:2]
        self.x = self.width // self.fontwidth
        self.y = self.height // self.fontheight
        self.resize = (self.x, self.y)
        self.image2 = cv2.resize(self.image, self.resize)
        self.imgy, self.imgx = self.image2.shape[:2]

        print(self.counting)

        for y in range(self.imgy):
            self.imgvalue.append([])
            for x in range(self.imgx):
                self.imgvalue[y].append([])
                for z in range(2):
                    self.imgvalue[y][x].append([])

        for a in range(self.imgy):
            for b in range(self.imgx):
                self.imgvalue[a][b][0] = int(self.image2[a][b][0]*0.30 + self.image2[a][b][1]*0.59 + self.image2[a][b][2]*0.11)

        if len(self.imgold) == 0:
            for c in range(self.imgy):
                for d in range(self.imgx):
                    self.imgvalue[c][d][1] = random.choice(self.newtext)
                    #print(self.imgvalue[c][d][1])


        if len(self.imgold) != 0:
            for e in range(self.imgy):
                if e <= 2:
                    for f in range(self.imgx):
                        self.imgvalue[e][f][1] = random.choice(self.newtext)
                        #print(self.imgvalue[e][f])
                else:
                    for f in range(self.imgx):
                        self.imgvalue[e][f][1] = self.imgold[e-1][f][1]
                        #print(self.imgvalue[e][f])
                        #print(random.choice(self.newtext))

        print('Photo width:', len(self.image[0]), 'converted to width: ', (self.imgx) * self.fontwidth, 'sign in row',self.imgx)
        print('Photo height:', len(self.image), 'conwerted to height: ', (self.imgy) * self.fontheight,'sign in column', self.imgy)

        self.screensize = ((self.imgx + 1) * self.fontwidth, (self.imgy + 1) * self.fontheight)
        self.screen = pg.display.set_mode(self.screensize)
        self.fill_data_arrays(self.imgx, self.imgy)
        self.v = 0
        self.imgold = copy.deepcopy(self.imgvalue)
        self.counting += 1

    def load_data(self):
        for letter in self.charlist:
            self.newtext.append(letter.encode("utf-8").decode("utf-8"))
            self.rend += 1

    def new(self):
        self.playing = True
        self.all_sprites = pg.sprite.Group()
        self.drops = pg.sprite.Group()


    def printing(self, sign, x, y, color):
        self.screen.blit(self.gamefont.render(sign, True, color), (x, y))

    def run(self):
        #self.rain_generator(self.raindrop)
        for a in range(self.count):
            self.new()
            self.load_file()
            if self.tagval == True:
                self.tag()
            if self.raingen == True:
                self.rain_generator(self.raindrop)

            while self.playing:
                self.loop()
        
            pg.image.save(self.screen, str(a) + ".jpg")
            #self.screen.fill((0, 0, 0))
            pg.display.flip()

        #converting to video
        if self.filetype == "mp4":
            self.writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), self.fps,((self.imgx + 1) * self.fontwidth, (self.imgy + 1) * self.fontheight))
            for frame in range(self.count):
                self.fra = cv2.imread(str(int(frame) - 1) + '.jpg')
                self.writer.write(self.fra)
            self.writer.release()


            #for a in range(10):



    def newcolor(self, value):
        if self.color == 'green':
            return[20, value, 20]
        if self.color == 'pink':
            return[value, 20, value//2]

    def fill_data_arrays(self, dx, dy):
        for y in range(dy):
            for x in range(dx):
                #val = sum(self.imgvalue[y][x])//(self.fontheight*self.fontwidth)
                self.scrdis.append([self.imgvalue[y][x][1], x, y, self.newcolor(self.imgvalue[y][x][0])])

    def rain_generator(self, dropnum):
        for x in range(dropnum):
            Drop(self,  (random.randint(0,self.x - 1)*self.fontwidth),
                        (random.randint(0,self.y)*self.fontheight),
                        (self.gamefont.render(random.choice(self.newtext), True, self.raincolor)),
                        self.fontwidth, self.fontheight)

    def loop(self):
        self.dt = self.clock.tick(60) / 1000
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
        self.screen.fill((0, 0, 0))
        pg.display.update()
        pg.display.flip()
        #self.screen.fill((0, 0, 0))
        #pg.display.flip()

        for all in self.scrdis:
            self.printing(all[0], all[1] * self.fontwidth, all[2] * self.fontheight, all[3])
        if self.makegif == True:
            self.drops.draw(self.screen)
            self.drops.update()
        
        if self.filetype == "jpg" or self.filetype == "png":
            if self.v < self.frames:
                pg.image.save(self.screen, str(self.v) + ".jpg")
                pg.display.flip()
            else:
                self.writer = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), self.fps,((self.imgx + 1) * self.fontwidth, (self.imgy + 1) * self.fontheight))
                for frame in range(self.v - 1):
                    self.newvar = int(frame) - 1
                    print(frame)
                    self.fra = cv2.imread(str(self.newvar) + '.jpg')
                    #print(self.fra)
                    self.writer.write(self.fra)
                self.writer.release()
                self.playing = False
        
        self.v = self.v + 1

        if self.filetype == "mp4":
            self.playing = False

    def tag(self):
        self.scrdis[0][0] = str("M")
        self.scrdis[1][0] = str("A")
        self.scrdis[2][0] = str("U")
        self.scrdis[3][0] = str("C")
        self.scrdis[4][0] = str("I")
        self.scrdis[5][0] = str("N")
        self.scrdis[6][0] = str("9")
        self.scrdis[7][0] = str("0")

class Drop(pg.sprite.Sprite):
    def __init__(self, plain, x, y, sign, width, height):
        self.height = height
        self.groups = plain.drops
        pg.sprite.Sprite.__init__(self, self.groups)
        self.sign = sign
        self.plain = plain
        self.image = sign
        self.rect = [x, y, width, self.height]

    def draw(self):
        self.plain.screen.blit(self.sign, (self.rect[0], self.rect[1]))

    def update(self):
        self.rect[1] = self.rect[1] + self.height
        if self.rect[1] > ((self.plain.y - 2) * self.height):
            self.rect[1] = 0

apl = Menu()