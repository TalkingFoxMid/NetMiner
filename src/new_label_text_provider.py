from typing import List
import os
import re
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

from config import SLASH_REPLACER


class NewLabelTextProvider:
    @staticmethod
    def get_normalized_labels(labels: List[str]):
        return [ (str(labels.index(label)+1)+":  " + label.replace(SLASH_REPLACER, "/")) for label in labels]

    def update_label_text(self, current_directory,
                          label,
                          image_label: QLabel,
                          move_sections):
        if os.path.isdir(current_directory):
            labels = self.get_normalized_labels(move_sections)
            label.setText("\n".join(labels))
        else:
            with open(current_directory, "r", encoding="utf-8") as doc:
                txt = doc.read()
            image_matches = re.findall("\[img_src\]\((.+?)\)", txt)
            if image_matches:
                img = image_matches[0]
                image_label.setPixmap(QPixmap(f"images/{img}").scaled(
                    image_label.width(),
                    image_label.height()
                ))

            label.setText(txt)
