########################################################################
## 
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
import os,threading
########################################################################
# IMPORT GUI FILE
from ui_interface import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar
########################################################################

########################################################################
## IMPORT CUSTOM WIDGETS
########################################################################
from Widgets import *
from maps import MapCreator
import pytube
from pytube import YouTube
from pytube.cli import on_progress
import psutil
########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)

        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "output.html"))
        local_url = QUrl.fromLocalFile(file_path)

        # self.ui.webEngineView.setUrl(QUrl(u"https://www.google.com/"))
        self.ui.webEngineView_mt.load(QUrl("output.html"))
        self.ui.webEngineView.load(QUrl(u"http://localhost/felix/"))

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.ui.pushButton_down.clicked.connect(self.downt)
        self.show()
        self.nt=0
        self.cpu_percentage={}
        self.t=[3000,100,1000]
        self.st={}
        self.TT={}
        self.b=self.a=50

    def sv(self):
        for i in range(3):
            self.a+=1
        self.b-=1
        if i==0:
            self.cpu_percentage[i].rpb_setValue(psutil.cpu_percent())
        elif i==1:
            self.cpu_percentage[i].rpb_setValue(self.a)
        else:
            self.cpu_percentage[i].rpb_setValue(self.b)

    def speak(self,texte):
        import pyttsx3
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('rate', 130)
        engine.setProperty('voices', voices[0].id)
        engine.say(texte)
        engine.runAndWait()
    

    def sv(self):
        for i in range(3):
            self.a+=1
        self.b-=1
        if i==0:
            self.cpu_percentage[i].rpb_setValue(psutil.cpu_percent())
        elif i==1:
            self.cpu_percentage[i].rpb_setValue(self.a)
        else:
            self.cpu_percentage[i].rpb_setValue(self.b)

    def downt(self):
        self.nt+=1

        self.ui.lineEdit2.setEchoMode(QLineEdit.Normal)
        link= self.ui.lineEdit2.displayText()

        for i in range(3):
            self.cpu_percentage[i] = roundProgressBar(self.ui.cpu_frame)
            self.cpu_percentage[i].setObjectName(u"cpu_percentage")
            self.cpu_percentage[i].setMinimumSize(QSize(100, 100))
            self.cpu_percentage[i].setMaximumSize(QSize(100, 100))
            # SET PROGRESS BAR VALUE
            self.cpu_percentage[i].rpb_setMaximum(100) 
            # SET PROGRESS BAR STYLE
            self.cpu_percentage[i].rpb_setBarStyle('Hybrid2')
            # SET PROGRESS BAR LINE COLOR
            self.cpu_percentage[i].rpb_setLineColor((255, 30, 99))
            # SET PROGRESS BAR LINE COLOR
            # self.cpu_percentage[i].rpb_setCircleColor((45, 74, 83))
            # SET PROGRESS BAR LINE COLOR
            self.cpu_percentage[i].rpb_setPieColor((45, 74, 83))
            #CHANGING THE PATH COLOR
            # self.cpu_percentage[i].rpb_setPathColor((45, 74, 83))
            #SET PROGRESS BAR TEXT COLOR
            self.cpu_percentage[i].rpb_setTextColor((255, 255, 255)) 
            # SET PROGRESS BAR STARTING POSITION
            # North, East, West, South
            self.cpu_percentage[i].rpb_setInitialPos('West')
            #SET PROGRESS BAR TEXT TYPE : VALUE OR PERCENTAGE
            # Value, Percentage
            self.cpu_percentage[i].rpb_setTextFormat('Percentage')

            #SET PROGRESS BAR FONT
            self.cpu_percentage[i].rpb_setTextFont('Arial')        
            #TEXT HIDDEN
            # self.cpu_percentage[i].rpb_enableText(False) 
            #SET PROGRESS BAR LINE WIDTH 
            self.cpu_percentage[i].rpb_setLineWidth(7)
            #PATH WIDTH
            self.cpu_percentage[i].rpb_setPathWidth(7)
            #SET PROGRESS BAR LINE CAP
            # RoundCap, SquareCap
            self.cpu_percentage[i].rpb_setLineCap('RoundCap')

            self.ui.hlayout_5.addWidget(self.cpu_percentage[i],0,Qt.AlignRight)
                
        self.Tm = QTimer(self)
        self.Tm.timeout.connect(self.sv)
        self.Tm.start(1000)

        def progress_callback(stream, chunk, bytes_remaining):

            global inc
            total_size = stream.filesize
            bytes_downloaded = total_size - bytes_remaining
            percentage_of_completion = bytes_downloaded / total_size * 100
            inc=int(percentage_of_completion)
            print(inc)
            import psutil
            inc = psutil.cpu_percent()

        def complete_callback(stream, file_handle):
            self.speak("downloading finished")
            self.ui.pushButton_down.show()
            # progress bar stop call from GUI here


        try:
                # object creation using YouTube
                # which was imported in the beginning
            if link!='':
                yt = YouTube(link)
                self.val=True
            else:
                self.speak("link is null!!")
                self.val=False
        except:
            self.speak("Connection Error") #to handle exception
            self.val=False

            # filters out all the files with "mp4" extension
            #to set the name of the file
            # get the video with the extension and
            # resolution passed in the get() function
        try:
                # downloading the video
            # where to save
            if self.val:
                self.speak("Select save Directory")
                SAVE_PATH = str(QFileDialog.getExistingDirectory(None, "Select Directory"))  #to_do
                self.speak("Starting")
                self.ui.pushButton_down.hide()
                yt.register_on_progress_callback(progress_callback)
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
                yt.register_on_complete_callback(complete_callback)
        except:
            self.speak("download Error Some Error!")


########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
