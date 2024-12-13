import time
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer
from logic import load_texts, calculate_speed


class TypingTrainerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.texts = load_texts("data/texts.json")
        self.current_text = ""
        self.start_time = None
        self.typing_started = False
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_speed)

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
        self.target_text_label.setObjectName("targetText")
        self.target_text_label.setWordWrap(True)
        self.target_text_label.setAlignment(Qt.AlignCenter)
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

        self.speed_label = QLabel("Typing speed: 0 CPM")
        layout.addWidget(self.speed_label)

        self.setLayout(layout)

    def start_training(self, difficulty):
        self.current_text = self.texts[difficulty][0]
        self.target_text_label.setText(self.current_text)
        self.instruction_label.setText("Type the text shown above:")
        self.text_area.setDisabled(False)
        self.text_area.setFocus()
        self.typing_started = False
        self.speed_label.setText("Typing speed: 0 CPM")

    def check_input(self):
        user_input = self.text_area.toPlainText()
        target_text = self.current_text

        if not self.typing_started and user_input:
            self.typing_started = True
            self.start_time = time.time()
            self.timer.start(500)  # Update speed every 500 ms

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
            self.complete_training()

    def complete_training(self):
        self.timer.stop()
        elapsed_time = time.time() - self.start_time
        speed = calculate_speed(len(self.current_text), elapsed_time)

        QMessageBox.information(
            self,
            "Result",
            f"Speed: {speed:.2f} characters per minute"
        )
        self.reset_ui()

    def update_speed(self):
        if self.typing_started:
            elapsed_time = time.time() - self.start_time
            user_input = self.text_area.toPlainText()
            speed = calculate_speed(len(user_input), elapsed_time)
            self.speed_label.setText(f"Typing speed: {speed:.2f} CPM")

    def reset_ui(self):
        self.text_area.setPlainText("")
        self.text_area.setDisabled(True)
        self.target_text_label.setText("")
        self.instruction_label.setText("Select a difficulty level:")
        self.speed_label.setText("Typing speed: 0 CPM")
