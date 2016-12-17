# project GenieGUI
# author Toni Marquez

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QDir
from PyQt4.QtGui import QFileDialog
from ui_geniegui import Ui_GenieGUI

class GenieGUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(GenieGUI, self).__init__(parent)
        self.ui = Ui_GenieGUI()
        self.ui.setupUi(self)

        # output attributes
        self.solution_name = ""
        self.debug = False
        self.release = False
        self.x32 = False
        self.x64 = False
        self.project_name = ""
        self.kind = 1
        self.include_dirs = ""
        self.files = ""
        self.debug_target_dir = ""
        self.debug_flags = ""
        self.debug_links = ""
        self.debug_defines = ""
        self.release_target_dir = ""
        self.release_flags = ""
        self.release_links = ""
        self.release_defines = ""

        # helper attributes
        self.include_index = 0
        self.file_index = 0
        self.include_array = []
        self.file_array = []

        # signal connections
        self.ui.solutionLineEdit.textChanged.connect(self.textChanged_solutionLineEdit)
        self.ui.configurationsDebugCheckBox.stateChanged.connect(self.stateChanged_configurationsDebugCheckBox)
        self.ui.configurationsReleaseCheckBox.stateChanged.connect(self.stateChanged_configurationsReleaseCheckBox)
        self.ui.platformsX32CheckBox.stateChanged.connect(self.stateChanged_platformsX32CheckBox)
        self.ui.platformsX64CheckBox.stateChanged.connect(self.stateChanged_platformsX64CheckBox)
        self.ui.projectLineEdit.textChanged.connect(self.textChanged_projectLineEdit)
        self.ui.kindConsoleRadioButton.toggled.connect(self.toggled_kindConsoleRadioButton)
        self.ui.kindStaticRadioButton.toggled.connect(self.toggled_kindStaticRadioButton)
        self.ui.createButton.clicked.connect(self.clicked_createButton)
        self.ui.includeComboBox.currentIndexChanged.connect(self.currentIndexChanged_includeComboBox)
        self.ui.includeAddPushButton.clicked.connect(self.clicked_includeAddPushButton)
        self.ui.includeRemovePushButton.clicked.connect(self.clicked_includeRemovePushButton)
        self.ui.fileComboBox.currentIndexChanged.connect(self.currentIndexChanged_fileComboBox)
        self.ui.fileAddPushButton.clicked.connect(self.clicked_fileAddPushButton)
        self.ui.fileRemovePushButton.clicked.connect(self.clicked_fileRemovePushButton)
        self.ui.debugTargetLineEdit.textChanged.connect(self.textChanged_debugTargetLineEdit)
        self.ui.debugTargetPushButton.clicked.connect(self.clicked_debugTargetPushButton)
        self.ui.debugFlagsLineEdit.textChanged.connect(self.textChanged_debugFlagsLineEdit)
        self.ui.debugLinkLineEdit.textChanged.connect(self.textChanged_debugLinkLineEdit)
        self.ui.debugDefinesLineEdit.textChanged.connect(self.textChanged_debugDefinesLineEdit)
        self.ui.releaseTargetLineEdit.textChanged.connect(self.textChanged_releaseTargetLineEdit)
        self.ui.releaseTargetPushButton.clicked.connect(self.clicked_releaseTargetPushButton)
        self.ui.releaseFlagsLineEdit.textChanged.connect(self.textChanged_releaseFlagsLineEdit)
        self.ui.releaseLinkLineEdit.textChanged.connect(self.textChanged_releaseLinkLineEdit)
        self.ui.releaseDefinesLineEdit.textChanged.connect(self.textChanged_releaseDefinesLineEdit)

    # connected methods
    def textChanged_solutionLineEdit(self, string):
        self.solution_name = string

    def stateChanged_configurationsDebugCheckBox(self, checked):
        if checked:
            self.debug = True
        else:
            self.debug = False
        self.ui.debugFrame.setEnabled(checked)
        self.ui.debugTargetLineEdit.setEnabled(checked)
        self.ui.debugFlagsLineEdit.setEnabled(checked)
        self.ui.debugLinkLineEdit.setEnabled(checked)
        self.ui.debugDefinesLineEdit.setEnabled(checked)

    def stateChanged_configurationsReleaseCheckBox(self, checked):
        if checked:
            self.release = True
        else:
            self.release = False
        self.ui.releaseFrame.setEnabled(checked)
        self.ui.releaseTargetLineEdit.setEnabled(checked)
        self.ui.releaseFlagsLineEdit.setEnabled(checked)
        self.ui.releaseLinkLineEdit.setEnabled(checked)
        self.ui.releaseDefinesLineEdit.setEnabled(checked)

    def stateChanged_platformsX32CheckBox(self, checked):
        if checked:
            self.x32 = True
        else:
            self.x32 = False

    def stateChanged_platformsX64CheckBox(self, checked):
        if checked:
            self.x64 = True
        else:
            self.x64 = False

    def textChanged_projectLineEdit(self, string):
        self.project_name = string

    def toggled_kindConsoleRadioButton(self, checked):
        if checked:
            self.kind = 1

    def toggled_kindStaticRadioButton(self, checked):
        if checked:
            self.kind = 2

    def currentIndexChanged_includeComboBox(self, index):
        self.include_index = index

    def clicked_includeAddPushButton(self):
        path = QFileDialog.getExistingDirectory(self, "Select Include Path")
        dir = QDir(QDir.currentPath())
        path = dir.relativeFilePath(path)
        self.ui.includeComboBox.addItem(path)
        self.include_array.append(path)

    def clicked_includeRemovePushButton(self):
        self.ui.includeComboBox.removeItem(self.include_index)
        if self.include_array:
            self.include_array.pop(self.include_index)

    def currentIndexChanged_fileComboBox(self, index):
        self.file_index = index

    def clicked_fileAddPushButton(self):
        path = QFileDialog.getExistingDirectory(self, "Select File Path") + "/*.*"
        dir = QDir(QDir.currentPath())
        path = dir.relativeFilePath(path)
        self.ui.fileComboBox.addItem(path)
        self.file_array.append(path)

    def clicked_fileRemovePushButton(self):
        self.ui.fileComboBox.removeItem(self.file_index)
        if self.file_array:
            self.file_array.pop(self.file_index)

    def textChanged_debugTargetLineEdit(self, string):
        self.debug_target_dir = string

    def clicked_debugTargetPushButton(self):
        self.debug_target_dir = QFileDialog.getExistingDirectory(self, "Select Debug Path")
        dir = QDir(QDir.currentPath())
        self.debug_target_dir = dir.relativeFilePath(self.debug_target_dir)
        self.ui.debugTargetLineEdit.setText(self.debug_target_dir)

    def textChanged_debugFlagsLineEdit(self, string):
        self.debug_flags = string

    def textChanged_debugLinkLineEdit(self, string):
        self.debug_links = string

    def textChanged_debugDefinesLineEdit(self, string):
        self.debug_defines = string

    def textChanged_releaseTargetLineEdit(self, string):
        self.release_target_dir = string

    def clicked_releaseTargetPushButton(self):
        self.release_target_dir = QFileDialog.getExistingDirectory(self, "Select Release Path")
        dir = QDir(QDir.currentPath())
        self.release_target_dir = dir.relativeFilePath(self.release_target_dir)
        self.ui.releaseTargetLineEdit.setText(self.release_target_dir)

    def textChanged_releaseFlagsLineEdit(self, string):
        self.release_flags = string

    def textChanged_releaseLinkLineEdit(self, string):
        self.release_links = string

    def textChanged_releaseDefinesLineEdit(self, string):
        self.release_defines = string

    def clicked_createButton(self):
        string = "solution \"" + self.solution_name + "\"\n"
        if self.debug is True or self.release is True:
            string += "  configurations {\n"
            if self.debug is True:
                string += "    \"Debug\""
                if self.release is True:
                    string += ",\n    \"Release\""
            else:
                if self.release is True:
                    string += "    \"Release\""
            string += "\n  }\n"
        if self.x32 is True or self.x64 is True:
            string += "  platforms {\n"
            if self.x32 is True:
                string += "    \"x32\""
                if self.x64 is True:
                    string += ",\n    \"x64\""
            else:
                if self.x64 is True:
                    string += "    \"x64\""
            string += "\n  }\n\n"
        string += "project \"" + self.project_name + "\"\n"
        if self.kind is 1:
            string += "  kind \"ConsoleApp\"\n"
        elif self.kind is 2:
            string += "  kind \"StaticLib\"\n"
        string += "  language \"C++\"\n\n"
        string += "  includedirs {\n"
        for i in self.include_array:
            string += "    \"" + i + "\",\n"
        string += "  }\n\n"
        string += "  files {\n"
        for i in self.file_array:
            string += "    \"" + i + "\",\n"
        string += "  }\n\n"
        if self.debug is True:
            string += "  configuration \"Debug\"\n"
            string += "    targetdir \"" + self.debug_target_dir + "\"\n"
            string += "    flags { " + self.debug_flags + " }\n"
            string += "    links { " + self.debug_links + " }\n"
            string += "    defines { " + self.debug_defines + " }\n"
            string += "  }\n\n"
        if self.release is True:
            string += "  configuration \"Release\"\n"
            string += "    targetdir \"" + self.release_target_dir + "\"\n"
            string += "    flags { " + self.release_flags + " }\n"
            string += "    links { " + self.release_links + " }\n"
            string += "    defines { " + self.release_defines + " }\n"
            string += "  }\n\n"

        if self.solution_name and self.project_name:
            self.ui.logLabel.setText("file succesfully created!")
            self.ui.logLabelError.setText("")
            file = open('genie.lua', 'w')
            file.write(string)
            file.close()
        else:
            self.ui.logLabel.setText("")
            self.ui.logLabelError.setText("error, missed fields!")

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)
    window = GenieGUI()
    window.show()
    sys.exit(app.exec_())
