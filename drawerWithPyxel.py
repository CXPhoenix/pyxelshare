import pyxel
import os
import sys

class App:
    def __init__(self,w = 160,h = 120):
        pyxel.init(w,h,caption = 'Drawer With Pyxel')
        pyxel.cls(7)
        pyxel.mouse(True)
        
#        畫畫像素大小
        self.rectW, self.rectH = 1, 1
        
#        初始化滑鼠位置
        self.mx, self.my = 0, 0
        
#        初始化畫面
        self.currentPic = []
        for i in range(pyxel.height):
            self.currentPic.append([7 for j in range(pyxel.width)])
        
#        初始化flag
        self.isChange = False
        self.once = False
        
        pyxel.run(self.update, self.draw)
        
    def update(self):
#        設定滑鼠位置與事件布林值變數
        self.isPenDown = pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON,1,1)
        self.mx, self.my = pyxel.mouse_x, pyxel.mouse_y
        
#        設定關閉按鈕 Q
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        
#        設定存擋按鈕 ctr+s
        if pyxel.btnp(pyxel.KEY_S) and pyxel.btnp(pyxel.KEY_LEFT_CONTROL,1,1):
            self.saveCurrentPic()
        
        if not self.isPenDown:
            if self.isChange:
                self.tmpCurrentPic()
                self.isChange = False
        else:
            if not self.isChange:
                self.isChange = True
            
    
#    設定暫存圖形
    def tmpCurrentPic(self):
        self.currentPic = []
        for i in range(pyxel.height):
            self.currentPic.append([pyxel.image(4,system=True).data[i][j] for j in range(pyxel.width)])
    
#    設定圖形儲存
    def saveCurrentPic(self):
        i = 1
        if sys.platform.startswith('win32'):
            while (os.path.exists(f'.\\savePic{i}.txt')):
                i += 1
        elif sys.platform.startswith('darwin'):
            while (os.path.exists(f'./savePic{i}.txt')):
                i += 1
        
        with open(f'savePic{i}.txt','w') as pic:
            for i in range(pyxel.height):
                for j in range(pyxel.width):
                    pic.write(str(self.currentPic[i][j]))
                pic.write('\n')
    
    def draw(self):
        if not self.isPenDown:
            pyxel.cls(7)
            pyxel.text(2,2,'nono',0)
            pyxel.mouse(True)
            self.loadPic()
            self.once = False
        else:
            if not self.once:
                pyxel.mouse(False)
                pyxel.cls(7)
                self.loadPic()
                self.once = True
            self.tmpCurrentPic()
            pyxel.rect(self.mx,self.my,self.rectW,self.rectH,0)
    
#    設定讀取圖片
    def loadPic(self):
        for i in range(pyxel.height):
            for j in range(pyxel.width):
                pyxel.image(4,system=True).data[i][j] = self.currentPic[i][j]
        

if __name__ == '__main__':
    if len(sys.argv) < 2:
        App()
    elif len(sys.argv) == 3:
        App(sys.argv[1], sys.argv[2])
    else:
        print("not a good command..")
