import re
from pathlib import Path
from typing import List

from config import IMG_HEIGHT, IMG_WIDTH, SLASH_REPLACER
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
                content = f"{current_path.stem}\n\n{text}"
            image_matches = re.findall(r"\[img_src\]\((.+?)\)", text)
            if image_matches:
                img = image_matches[0]
                image_label.setPixmap(
                    QPixmap(f"images/{img}").scaled(IMG_WIDTH, IMG_HEIGHT)
                )
            label.setText(content)
