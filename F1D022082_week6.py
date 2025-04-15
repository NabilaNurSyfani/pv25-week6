import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QSlider, QHBoxLayout,
    QVBoxLayout, QSizePolicy, QSpacerItem
)

class FontAdjuster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font Size and Color Adjuster")
        self.setFixedSize(600, 400)
        self.setStyleSheet("background-color: #2c2c2c; color: white;")

        # untuk bagian NIM
        self.label_nim = QLabel("F1D022082")
        self.label_nim.setAlignment(Qt.AlignCenter)
        self.label_nim.setFont(QFont("Arial", 32))
        self.label_nim.setStyleSheet("background-color: #ffffff; color: #000000;")
        self.label_nim.setFixedHeight(120)
        self.label_nim.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)

        # font size
        self.font_size_label = QLabel("Font Size")
        self.font_size_slider = QSlider(Qt.Horizontal)
        self.font_size_slider.setMinimum(20)
        self.font_size_slider.setMaximum(60)
        self.font_size_slider.setTickInterval(10)
        self.font_size_slider.setTickPosition(QSlider.TicksBelow)
        self.font_size_slider.setValue(32)
        self.font_size_slider.valueChanged.connect(self.font_size)

        # background color
        self.bg_label = QLabel("Background Color")
        self.bg_slider = QSlider(Qt.Horizontal)
        self.bg_slider.setMinimum(0)
        self.bg_slider.setMaximum(255)
        self.bg_slider.setTickPosition(QSlider.TicksBelow)
        self.bg_slider.setValue(255)
        self.bg_slider.valueChanged.connect(self.background_color)

        # font color
        self.font_color_label = QLabel("Font Color")
        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setMinimum(0)
        self.font_slider.setMaximum(255)
        self.font_slider.setTickPosition(QSlider.TicksBelow)
        self.font_slider.setValue(0)
        self.font_slider.valueChanged.connect(self.font_color)

        # untuk identitas
        self.label_info = QLabel("Nama: Nabila  |  NIM: F1D022082")
        self.label_info.setAlignment(Qt.AlignCenter)
        self.label_info.setStyleSheet("color: white;")

        # layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label_nim)
        main_layout.addSpacerItem(QSpacerItem(0, 20))
        main_layout.addLayout(self.slider_layout(self.font_size_label, self.font_size_slider))
        main_layout.addSpacerItem(QSpacerItem(0, 20))
        main_layout.addLayout(self.slider_layout(self.bg_label, self.bg_slider))
        main_layout.addSpacerItem(QSpacerItem(0, 20))
        main_layout.addLayout(self.slider_layout(self.font_color_label, self.font_slider))
        main_layout.addSpacerItem(QSpacerItem(0, 20))
        main_layout.addWidget(self.label_info)

        self.setLayout(main_layout)

    def slider_layout(self, label, slider):
        layout = QHBoxLayout()
        label.setFixedWidth(120)
        layout.addWidget(label)
        layout.addWidget(slider)
        return layout

    def font_size(self):
        size = self.font_size_slider.value()
        self.label_nim.setFont(QFont("Arial", size))

    def background_color(self):
        val = self.bg_slider.value()
        text_color = self.font_slider.value()
        self.label_nim.setStyleSheet(
            f"background-color: rgb({val},{val},{val}); color: rgb({text_color},{text_color},{text_color});"
        )

    def font_color(self):
        val = self.font_slider.value()
        bg_color = self.bg_slider.value()
        self.label_nim.setStyleSheet(
            f"background-color: rgb({bg_color},{bg_color},{bg_color}); color: rgb({val},{val},{val});"
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FontAdjuster()
    window.show()
    sys.exit(app.exec_())