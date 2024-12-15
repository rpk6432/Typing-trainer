import time
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt
from logic import load_texts, calculate_speed
from styles import MAIN_STYLE, INCORRECT_INPUT_STYLE, CORRECT_INPUT_STYLE, HIGHLIGHTED_TARGET_TEXT_STYLE


class TypingTrainerGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.texts = load_texts("data/texts.json")
        self.current_text = ""
        self.remaining_text = ""
        self.start_time = None

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Typing Trainer")
        self.setGeometry(100, 100, 600, 400)
        self.setStyleSheet(MAIN_STYLE)

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

        self.speed_label = QLabel("Typing Speed: 0 CPM")
        layout.addWidget(self.speed_label, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def start_training(self, difficulty):
        self.current_text = self.texts[difficulty][0]
        self.remaining_text = self.current_text
        self.target_text_label.setText(self.current_text)
        self.instruction_label.setText("Type the text shown above:")
        self.text_area.setDisabled(False)
        self.text_area.setFocus()
        self.start_time = None

    def check_input(self):
        user_input = self.text_area.toPlainText()
        target_text = self.current_text

        if target_text.startswith(user_input):
            self.text_area.setStyleSheet(CORRECT_INPUT_STYLE)
            self.remaining_text = target_text[len(user_input):]
            self.update_target_text_display()

            if self.remaining_text == "":
                self.show_result()
        else:
            self.text_area.setStyleSheet(INCORRECT_INPUT_STYLE)

        if self.start_time is not None:
            elapsed_time = time.time() - self.start_time
            speed = calculate_speed(len(user_input), elapsed_time)
            self.speed_label.setText(f"Typing Speed: {speed:.2f} CPM")

        if not user_input and self.start_time is not None:
            self.start_time = None

        if self.start_time is None and user_input:
            self.start_time = time.time()

    def update_target_text_display(self):
        self.target_text_label.setStyleSheet(HIGHLIGHTED_TARGET_TEXT_STYLE)
        self.target_text_label.setText(self.remaining_text)

    def show_result(self):
        elapsed_time = time.time() - self.start_time
        speed = calculate_speed(len(self.current_text), elapsed_time)

        QMessageBox.information(
            self,
            "Result",
            f"Speed: {speed:.2f} characters per minute"
        )
        self.reset_ui()

    def reset_ui(self):
        self.text_area.setPlainText("")
        self.text_area.setDisabled(True)
        self.target_text_label.setText("")
        self.instruction_label.setText("Select a difficulty level:")
        self.speed_label.setText("Typing Speed: 0 CPM")
        self.current_text = ""
        self.remaining_text = ""
