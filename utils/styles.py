#UI styling for the stock analysis application

from PyQt5.QtWidgets import QApplication, QStyleFactory
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtCore import Qt

def set_app_style(style_name="Fusion", dark_mode=False):
    """
    Set application styling
    
    Args:
        style_name: Name of the Qt style to use
        dark_mode: Whether to use dark mode styling
    """
    QApplication.setStyle(QStyleFactory.create(style_name))
    
    #Light Version Style
    light_palette = QPalette()
    light_palette.setColor(QPalette.Window, QColor(240, 240, 240))
    light_palette.setColor(QPalette.WindowText, Qt.black)
    light_palette.setColor(QPalette.Base, QColor(255, 255, 255))
    light_palette.setColor(QPalette.AlternateBase, QColor(230, 230, 230))
    light_palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))
    light_palette.setColor(QPalette.ToolTipText, Qt.black)
    light_palette.setColor(QPalette.Text, Qt.black)
    light_palette.setColor(QPalette.Button, QColor(220, 220, 220))
    light_palette.setColor(QPalette.ButtonText, Qt.black)
    light_palette.setColor(QPalette.Highlight, QColor(61, 174, 233))
    light_palette.setColor(QPalette.HighlightedText, Qt.white)
    light_palette.setColor(QPalette.BrightText, Qt.red)
    QApplication.setPalette(light_palette)