import time
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from logic import load_texts, count_errors, calculate_speed


class TypingTrainerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.texts = load_texts("data/texts.json")
        self.current_text = ""
        self.start_time = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Typing Trainer")
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("""
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
        """)

        layout = QVBoxLayout()

        self.instruction_label = QLabel("Select a difficulty level:")
        layout.addWidget(self.instruction_label, alignment=Qt.AlignCenter)

        self.target_text_label = QLabel("")
        self.target_text_label.setObjectName("targetText")  # Apply the custom style
        self.target_text_label.setWordWrap(True)  # Allow text wrapping
        self.target_text_label.setAlignment(Qt.AlignCenter)  # Center the text
        layout.addWidget(self.target_text_label)

        self.easy_button = QPushButton("Easy")
        self.medium_button = QPushButton("Medium")
        self.hard_button = QPushButton("Hard")

        self.easy_button.clicked.connect(lambda: self.start_training("easy"))
        self.medium_button.clicked.connect(lambda: self.start_training("medium"))
        self.hard_button.clicked.connect(lambda: self.start_training("hard"))

        layout.addWidget(self.easy_button)
        layout.addWidget(self.medium_button)
        layout.addWidget(self.hard_button)

        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("Start typing here...")
        self.text_area.setDisabled(True)
        self.text_area.textChanged.connect(self.check_input)
        layout.addWidget(self.text_area)

        self.setLayout(layout)

    def start_training(self, difficulty):
        self.current_text = self.texts[difficulty][0]
        self.target_text_label.setText(self.current_text)  # Display text in a label
        self.instruction_label.setText("Type the text shown above:")
        self.text_area.setDisabled(False)
        self.text_area.setFocus()
        self.start_time = time.time()

    def check_input(self):
        user_input = self.text_area.toPlainText()
        target_text = self.current_text

        if not target_text.startswith(user_input):
            self.text_area.setStyleSheet("""
                QTextEdit {
                    background-color: #553333;
                    color: #f0f0f0;
                    border: 1px solid #ff5555;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 16px;
                }
            """)
        else:
            self.text_area.setStyleSheet("""
                QTextEdit {
                    background-color: #3a3a3a;
                    color: #f0f0f0;
                    border: 1px solid #444;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 16px;
                }
            """)

        if user_input == target_text:
            elapsed_time = time.time() - self.start_time
            errors = count_errors(target_text, user_input)
            speed = calculate_speed(len(user_input), elapsed_time)

            QMessageBox.information(
                self,
                "Results",
                f"Errors: {errors}\nSpeed: {speed:.2f} characters per minute"
            )
            self.reset_ui()

    def reset_ui(self):
        self.text_area.setPlainText("")
        self.text_area.setDisabled(True)
        self.target_text_label.setText("")
        self.instruction_label.setText("Select a difficulty level:")
