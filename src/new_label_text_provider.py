from typing import List
import os
from config import SLASH_REPLACER


class NewLabelTextProvider:
    @staticmethod
    def get_normalized_labels(labels: List[str]):
        return [ (str(labels.index(label)+1)+":  " + label.replace(SLASH_REPLACER, "/")) for label in labels]

    def update_label_text(self, current_directory,
                          label,
                          move_sections):
        if os.path.isdir(current_directory):
            labels = self.get_normalized_labels(move_sections)
            label.setText("\n".join(labels))
        else:
            with open(current_directory, "r", encoding="utf-8") as doc:
                label.setText(doc.read())