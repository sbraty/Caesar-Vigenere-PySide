#!/usr/bin/python
 
# Import PySide classes
import sys
from PySide.QtCore import *
from PySide.QtGui import *
 
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Caesar and Vigenere lab")

#GUI button
ExB = QPushButton("&Exit")
DoB = QPushButton("&Do")
OpenInB = QPushButton("&Open")
OpenOutB = QPushButton("&Open")

#Gui group box
cipheGB = QGroupBox("Ciphe:")
acGB = QGroupBox("Action:")

#GUI check box
CaesarCB = QRadioButton("Caesar");
VigenereCB = QRadioButton("Vigenere");
CCB = QRadioButton("Crypt");
DCB = QRadioButton("Decrypt");

#GUI layout
mainLay = QVBoxLayout()
aLay = QVBoxLayout()
bLay = QVBoxLayout()
cbLay = QHBoxLayout()
cbcdLay = QHBoxLayout()
inLay = QHBoxLayout()
outLay = QHBoxLayout()
keyLay = QHBoxLayout()
btLay = QHBoxLayout()

#GUI lineedit
inLI = QLineEdit()
outLI = QLineEdit()
keyLI = QLineEdit()

#GUI lable
inLable = QLabel("Input file:   ")
outLable = QLabel("Output file: ")
keyLable = QLabel("Enter key: ")

#cbLay
cbLay.addWidget(CaesarCB)
cbLay.addWidget(VigenereCB)
cbLay.addStretch(1)
cipheGB.setLayout(cbLay)
aLay.addWidget(cipheGB)

#cbcdLay
cbcdLay.addWidget(CCB)
cbcdLay.addWidget(DCB)
cbcdLay.addStretch(1)
acGB.setLayout(cbcdLay)
bLay.addWidget(acGB)

#inLay
inLay.addWidget(inLable)
inLay.addWidget(inLI)
inLay.addWidget(OpenInB)


#outLay
outLay.addWidget(outLable)
outLay.addWidget(outLI)
outLay.addWidget(OpenOutB)

#keyLay
keyLay.addWidget(keyLable)
keyLay.addWidget(keyLI)

#btLay
btLay.addWidget(DoB)
btLay.addWidget(ExB)

#mainLay
mainLay.addLayout(aLay)
mainLay.addLayout(bLay)
mainLay.addLayout(inLay)
mainLay.addLayout(outLay)
mainLay.addLayout(keyLay)
mainLay.addLayout(btLay)

window.setLayout(mainLay)
window.setFixedHeight(270)
window.setFixedWidth(350)

def main():
	CaesarCB.setChecked(True)
	CCB.setChecked(True)

	OpenInB.clicked.connect(infile)	
	OpenOutB.clicked.connect(outfile)
	DoB.clicked.connect(make)
	ExB.clicked.connect(quit)

	window.show()

	sys.exit(app.exec_())


def infile():
	fname, _ = QFileDialog.getOpenFileName()
	inLI.setText(fname)


def outfile():
	fname, _ = QFileDialog.getOpenFileName()
	outLI.setText(fname)


def make():
	f1 = open(inLI.text(),"r");
	text = f1.read();
	f1.close;
	f2 = open(outLI.text(), 'w')

	if CaesarCB.isChecked():
		if CCB.isChecked():
			f2.write(Caesar(text, int(keyLI.text()), 1))	
		elif DCB.isChecked():
			f2.write(Caesar(text, int(keyLI.text()), 0))
	elif VigenereCB.isChecked():
		if CCB.isChecked():
			f2.write(Vigenere(text, str(keyLI.text()), 1))	
		elif DCB.isChecked():
			f2.write(Vigenere(text, str(keyLI.text()), 0))


def Caesar(text, key, flag):
    code = ''
    for c in text:
	if flag:
            code += chr((ord(c) + key) % 128)
	else:
	    code += chr((ord(c) - key) % 128)            
    return code


def Vigenere(text, key, flag):
    iter = 0
    code = ''
    for c in text:
	    if flag:
                code += chr((ord(c) + ord(key[iter])) % 128)
            else:
                code += chr((ord(c) - ord(key[iter])) % 128)
	    iter = (iter + 1) % len(key)             
    return code		

	
def test():
	msgBox = QMessageBox()
        msgBox.setText("Enter audio file!");
	msgBox.exec_();


if __name__ == '__main__':
    main()


