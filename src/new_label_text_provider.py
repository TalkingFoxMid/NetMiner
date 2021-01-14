from pathlib import Path
from typing import List

from config import SLASH_REPLACER


class NewLabelTextProvider:
    @staticmethod
    def get_normalized_labels(labels: List[str]):
        return [label.replace(SLASH_REPLACER, "/") for label in labels]

    def update_label_text(self, pathname, label, move_sections):
        current_path = Path(pathname)
        if current_path.is_dir():
            labels = self.get_normalized_labels(move_sections)
            label.setText("\n".join(labels))
        else:
            with current_path.open("r", encoding="utf-8") as doc:
                content = f"{current_path.stem}\n\n{doc.read()}"
                label.setText(content)
