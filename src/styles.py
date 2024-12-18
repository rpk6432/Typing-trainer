MAIN_STYLE = """
    QWidget {
        background-color: #2b2b2b;
        color: #f0f0f0;
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    QPushButton {
        background-color: #444;
        color: #f0f0f0;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
    }
    QPushButton:hover {
        background-color: #555;
    }
    QPushButton:pressed {
        background-color: #333;
    }
    QTextEdit {
        background-color: #3a3a3a;
        color: #f0f0f0;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 5px;
        font-size: 16px;
    }
    QLabel {
        color: #f0f0f0;
    }
    QLabel#targetText {
        font-size: 18px;
        font-weight: bold;
        color: #f0f0f0;
        background-color: #444;
        border: 2px solid #555;
        border-radius: 5px;
        padding: 10px;
        text-align: center;
    }
"""

INCORRECT_INPUT_STYLE = """
    QTextEdit {
        background-color: #553333;
        color: #f0f0f0;
        border: 1px solid #ff5555;
        border-radius: 5px;
        padding: 5px;
        font-size: 16px;
    }
"""

CORRECT_INPUT_STYLE = """
    QTextEdit {
        background-color: #3a3a3a;
        color: #f0f0f0;
        border: 1px solid #444;
        border-radius: 5px;
        padding: 5px;
        font-size: 16px;
    }
"""

HIGHLIGHTED_TARGET_TEXT_STYLE = """
    QLabel#targetText {
        font-size: 18px;
        font-weight: bold;
        color: #b3ffb3;
        background-color: #444;
        border: 2px solid #555;
        border-radius: 5px;
        padding: 10px;
        text-align: center;
    }
"""

SYSTEM_MENU_STYLE = """
    QPushButton#closeButton, QPushButton#minimizeButton, QPushButton#maximizeButton {
        border: none;
        border-radius: 6px;
    }

    QPushButton#closeButton {
        background-color: #FF605C;
    }
    QPushButton#closeButton:hover {
        background-color: #FF3B30;
    }

    QPushButton#minimizeButton {
        background-color: #FFBD44;
    }
    QPushButton#minimizeButton:hover {
        background-color: #F4AF41;
    }

    QPushButton#maximizeButton {
        background-color: #28C940;
    }
    QPushButton#maximizeButton:hover {
        background-color: #1F9E33;
    }
"""



