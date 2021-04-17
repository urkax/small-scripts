import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit
from PyQt5.QtCore import pyqtSlot, QMetaObject

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI() #界面绘制交给InitUi方法
        
        
    def initUI(self):
        #设置窗口的位置和大小
        basic = 1500
        self.setGeometry(300, 300, basic, int(basic*0.4))  
        #设置窗口的标题
        self.setWindowTitle('Icon')
        
        self.text_edit = QTextEdit(self)
        self.text_edit.setObjectName("edit")
        self.text_edit.setGeometry(5, 5, int(basic*0.48), int(basic*0.4))

        self.output_edit = QTextEdit(self)
        self.output_edit.setGeometry(int(basic*0.5), 5, int(basic*0.48), int(basic*0.4))

        QMetaObject.connectSlotsByName(self)

        #显示窗口
        self.show()
    
    @pyqtSlot()
    def on_edit_textChanged(self):
        text = self.text_edit.toPlainText()
        # text_list = []
        # for i in text:
        #     if i=='\n':
        #         text_list.append(' ')
        #     else:
        #         text_list.append(i)
        # text.replace('\n','')
        text=re.sub(r'[\n]*', '', text, count=0, flags=0)
        text=re.sub(r'[$](.*?)[$]', 'A', text, count=0, flags=0) #公式 $xxx$
        text = re.sub(r'\\emph{.*?}', lambda x:x[0][6:-1], text, count=0, flags=0)
        text=re.sub(r'~\\.*?{.*?}', '', text, count=0, flags=0) # ~\xxx{xx}
        text=re.sub(r'\\.*?{.*?}', '', text, count=0, flags=0) # \xxx{xx}
        # text=re.sub(r'\\.*?\[.*?\]', '', text, count=0, flags=0) # \xxx[xx]

        # print(text_list)
        # self.output_edit.setPlainText(''.join(text_list))
        self.output_edit.setPlainText(text)
        
if __name__ == '__main__':
    #创建应用程序和对象

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
