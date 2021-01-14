from pathlib import Path
from typing import List

from config import CONTENT_DIR, WND_HEIGHT, WND_WIDTH
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget

from src.new_label_text_provider import NewLabelTextProvider
from src.scrollable_label import ScrollableLabel


class MoveWidget(QWidget):
    def __init__(self, pathname: str):
        super().__init__()
        self.current_pathname = pathname
        self.ESCAPE_KEY = 16777216
        self.new_label_text_provider = NewLabelTextProvider()
        self.lt = QVBoxLayout()

        self.init_font()
        self.init_palette()
        self.init_header_label()
        self.init_image_label()
        self.init_scrollable_label()

        self.update_all()

        self.setLayout(self.lt)
        self.setMinimumSize(WND_WIDTH, WND_HEIGHT)
        self.setAutoFillBackground(True)

    def init_font(self):
        font = self.font()
        font.setPixelSize(20)
        self.setFont(font)

    def init_palette(self):
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.white)
        self.setPalette(palette)

    def init_header_label(self):
        self.header_label = QLabel()
        self.lt.addWidget(self.header_label)

    def init_image_label(self):
        self.image_label = QLabel()
        self.lt.addWidget(self.image_label)
        self.image_label.hide()

    def init_scrollable_label(self):
        self.label = ScrollableLabel()
        self.lt.addWidget(self.label)

    def update_all(self):
        self._update_move_sections()
        self._update_header_text()
        self._update_label_text()

    def _update_move_sections(self):
        current_path = Path(self.current_pathname).absolute()
        self.image_label.hide()
        if current_path.is_dir():
            self.move_sections: List[str] = [
                path.name for path in current_path.iterdir()
            ]
        else:
            self.move_sections = []

    def _update_label_text(self):
        self.new_label_text_provider.update_label_text(
            self.current_pathname,
            self.label,
            self.image_label,
            self.move_sections,
        )

    def _update_header_text(self):
        self.header_label.setText(
            self.current_pathname.removeprefix(CONTENT_DIR)
        )

    def key_press(self, key_id):
        index = key_id - 49 if key_id - 49 != -1 else 9
        if key_id == self.ESCAPE_KEY:
            if self.current_pathname == "content":
                return
            self.current_pathname = "/".join(
                self.current_pathname.split("/")[:-1]
            )
        else:
            try:
                self.current_pathname += "/" + self.move_sections[index]
            except IndexError:  # HACK
                pass
        self.update_all()
