# IMPORT PACKAGES AND MODULES
from gui.uis.windows.main_window.functions_main_window import *
# IMPORT QT CORE

# IMPORT SETTINGS
from gui.core.functions import Functions

# IMPORT PY ONE DARK WINDOWS
# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS

#import dependencies of Transcoder
from apps.Transcoder.main import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
os.environ["QT_FONT_DPI"] = "96"
os.environ["QT_SCALE_FACTOR"] = "1.5"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips

        SetupMainWindow.setup_gui(self)

        #setup transcoder
        self.Transcoder=Transcoder(self.ui.load_pages)
        #font = QFont()
        #font.setFamilies([u"Segoe UI Black"])
        #self.ui.load_pages.label_2.setFont(font)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////



    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        
        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        # LEFT MENU
        # ///////////////////////////////////////////////////////////////

        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        if btn.objectName() == "btn_page2":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)
        if btn.objectName() == "btn_page3":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
        # BOTTOM INFORMATION
        if btn.objectName() == "btn_info":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                #if btn.objectName() == "btn_close_left_column":
                self.ui.left_menu.deselect_all_tab()
                # Show / Hide
                MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Info tab",
                    icon_path=Functions.set_svg_icon("icon_info.svg")
                )

        # SETTINGS LEFT
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                self.ui.left_menu.deselect_all_tab()
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=Functions.set_svg_icon("icon_settings.svg")
                )

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

class MySplashScreen(QSplashScreen):
    # ??????????????????
    def mousePressEvent(self, event):
        pass

# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)

    splash = MySplashScreen()
    # ????????????
    splash.setPixmap(QPixmap("E:\Smartcoder\Resources\startImage.gif"))  # ??????????????????
    # ????????????
    #splash.showMessage("??????... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    # ????????????
    splash.setFont(QFont('????????????', 10))
    # ??????????????????
    splash.show()

    app.processEvents()
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    window.show()

    splash.finish(window)  # ??????????????????
    splash.deleteLater()
    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec())
