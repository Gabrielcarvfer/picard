# -*- coding: utf-8 -*-

# Automatically generated - don't edit.
# Use `python setup.py build_ui` to update it.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ScriptingOptionsPage(object):
    def setupUi(self, ScriptingOptionsPage):
        ScriptingOptionsPage.setObjectName("ScriptingOptionsPage")
        ScriptingOptionsPage.resize(605, 551)
        self.vboxlayout = QtWidgets.QVBoxLayout(ScriptingOptionsPage)
        self.vboxlayout.setContentsMargins(9, 9, 9, 9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")
        self.enable_tagger_scripts = QtWidgets.QGroupBox(ScriptingOptionsPage)
        self.enable_tagger_scripts.setCheckable(True)
        self.enable_tagger_scripts.setObjectName("enable_tagger_scripts")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.enable_tagger_scripts)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.enable_tagger_scripts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.script_list = ScriptListWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.script_list.sizePolicy().hasHeightForWidth())
        self.script_list.setSizePolicy(sizePolicy)
        self.script_list.setMinimumSize(QtCore.QSize(120, 0))
        self.script_list.setObjectName("script_list")
        self.formWidget = QtWidgets.QWidget(self.splitter)
        self.formWidget.setObjectName("formWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.formWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tagger_script = QtWidgets.QTextEdit(self.formWidget)
        self.tagger_script.setAcceptRichText(False)
        self.tagger_script.setObjectName("tagger_script")
        self.verticalLayout_2.addWidget(self.tagger_script)
        self.verticalLayout.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_button = QtWidgets.QToolButton(self.enable_tagger_scripts)
        self.add_button.setObjectName("add_button")
        self.horizontalLayout.addWidget(self.add_button)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.move_up_button = QtWidgets.QToolButton(self.enable_tagger_scripts)
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-up.png")
        self.move_up_button.setIcon(icon)
        self.move_up_button.setObjectName("move_up_button")
        self.horizontalLayout.addWidget(self.move_up_button)
        self.move_down_button = QtWidgets.QToolButton(self.enable_tagger_scripts)
        icon = QtGui.QIcon.fromTheme(":/images/16x16/go-down.png")
        self.move_down_button.setIcon(icon)
        self.move_down_button.setObjectName("move_down_button")
        self.horizontalLayout.addWidget(self.move_down_button)
        self.remove_button = QtWidgets.QToolButton(self.enable_tagger_scripts)
        self.remove_button.setObjectName("remove_button")
        self.horizontalLayout.addWidget(self.remove_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.script_error = QtWidgets.QLabel(self.enable_tagger_scripts)
        self.script_error.setText("")
        self.script_error.setAlignment(QtCore.Qt.AlignCenter)
        self.script_error.setObjectName("script_error")
        self.verticalLayout.addWidget(self.script_error)
        self.hlayout_doc = QtWidgets.QHBoxLayout()
        self.hlayout_doc.setObjectName("hlayout_doc")
        self.scripting_doc_link = QtWidgets.QLabel(self.enable_tagger_scripts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scripting_doc_link.sizePolicy().hasHeightForWidth())
        self.scripting_doc_link.setSizePolicy(sizePolicy)
        self.scripting_doc_link.setText("")
        self.scripting_doc_link.setWordWrap(True)
        self.scripting_doc_link.setOpenExternalLinks(True)
        self.scripting_doc_link.setObjectName("scripting_doc_link")
        self.hlayout_doc.addWidget(self.scripting_doc_link)
        self.scriptfuncdoc_button = QtWidgets.QPushButton(self.enable_tagger_scripts)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scriptfuncdoc_button.sizePolicy().hasHeightForWidth())
        self.scriptfuncdoc_button.setSizePolicy(sizePolicy)
        self.scriptfuncdoc_button.setObjectName("scriptfuncdoc_button")
        self.hlayout_doc.addWidget(self.scriptfuncdoc_button)
        self.verticalLayout.addLayout(self.hlayout_doc)
        self.vboxlayout.addWidget(self.enable_tagger_scripts)

        self.retranslateUi(ScriptingOptionsPage)
        self.add_button.clicked.connect(self.script_list.add_script)
        self.tagger_script.textChanged.connect(ScriptingOptionsPage.live_update_and_check)
        self.script_list.itemSelectionChanged.connect(ScriptingOptionsPage.script_selected)
        self.remove_button.clicked.connect(self.script_list.remove_selected_script)
        QtCore.QMetaObject.connectSlotsByName(ScriptingOptionsPage)
        ScriptingOptionsPage.setTabOrder(self.enable_tagger_scripts, self.add_button)
        ScriptingOptionsPage.setTabOrder(self.add_button, self.script_list)
        ScriptingOptionsPage.setTabOrder(self.script_list, self.tagger_script)

    def retranslateUi(self, ScriptingOptionsPage):
        _translate = QtCore.QCoreApplication.translate
        self.enable_tagger_scripts.setTitle(_("Tagger Script(s)"))
        self.add_button.setToolTip(_("Add new script"))
        self.add_button.setText(_("Add new script"))
        self.move_up_button.setToolTip(_("Move script up"))
        self.move_down_button.setToolTip(_("Move script down"))
        self.remove_button.setText(_("Remove script"))
        self.scriptfuncdoc_button.setText(_("Script functions documentation"))

from picard.ui.widgets.scriptlistwidget import ScriptListWidget
