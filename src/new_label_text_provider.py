import re
from pathlib import Path
from typing import List

from config import (
    IMAGES_DIR,
    IMG_HEIGHT,
    IMG_WIDTH,
    SLASH_REPLACER,
    WND_HEIGHT,
    WND_WIDTH,
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from src.scrollable_label import ScrollableLabel


class NewLabelTextProvider:
    @staticmethod
    def get_normalized_labels(labels: List[str]):
        return [
            (
                str(labels.index(label) + 1)
                + ":  "
                + label.replace(SLASH_REPLACER, "/").replace(".txt", "")
            )
            for label in labels
        ]

    def update_label_text(
        self,
        pathname,
        label: ScrollableLabel,
        image_label: QLabel,
        move_sections,
    ):
        current_path = Path(pathname).absolute()
        if current_path.is_dir():
            labels = self.get_normalized_labels(move_sections)
            label.setText("\n".join(labels))
        else:
            with current_path.open("r", encoding="utf-8") as doc:
                text = doc.read()
            image_matches = re.findall(r"(\[img_src\]\((.+?)\))", text)
            if image_matches:
                match = image_matches[0]
                img = match[1]
                text = text.replace(match[0], "")
                img_path = Path(f"{IMAGES_DIR}/{img}")
                if img_path.exists() and img_path.is_file():
                    image_label.show()
                    image_label.setPixmap(
                        QPixmap(img_path.as_posix()).scaled(
                            IMG_WIDTH,
                            IMG_HEIGHT,
                            aspectRatioMode=Qt.KeepAspectRatio,
                        )
                    )
            content = f"{current_path.stem}\n\n{text}"
            label.setText(content)
