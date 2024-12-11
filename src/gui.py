import time
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QMessageBox
)
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
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.instruction_label = QLabel("Select a difficulty level:")
        layout.addWidget(self.instruction_label)

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
        layout.addWidget(self.text_area)

        self.submit_button = QPushButton("Submit")
        self.submit_button.setDisabled(True)
        self.submit_button.clicked.connect(self.submit_text)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def start_training(self, difficulty):
        self.current_text = self.texts[difficulty][0]
        self.instruction_label.setText("Type the following text:")
        self.text_area.setPlainText(self.current_text)
        self.text_area.setDisabled(False)
        self.text_area.setFocus()
        self.submit_button.setDisabled(False)
        self.start_time = time.time()

    def submit_text(self):
        user_input = self.text_area.toPlainText()
        elapsed_time = time.time() - self.start_time

        errors = count_errors(self.current_text, user_input)
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
        self.submit_button.setDisabled(True)
        self.instruction_label.setText("Select a difficulty level:")
