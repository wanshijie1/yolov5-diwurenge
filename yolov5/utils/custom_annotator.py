import numpy as np
import cv2
from ultralytics.utils.plotting import Annotator as OriginalAnnotator
from PIL import Image, ImageDraw, ImageFont

class ChineseAnnotator(OriginalAnnotator):
    def box_label(self, box, label='', color=(128, 128, 128), txt_color=(255, 255, 255)):
        """
        重写 box_label 方法以支持中文
        """
        # 确保 self.im 不是 None
        if self.im is None:
            raise ValueError("Error: self.im is None in ChineseAnnotator!")

        # 确保 self.im 是 NumPy 数组
        if isinstance(self.im, Image.Image):  # 如果是 PIL.Image，则转换
            self.im = np.array(self.im)
        elif not isinstance(self.im, np.ndarray):
            raise TypeError(f"Error: self.im is not a numpy array, but {type(self.im)}")

        # 画出矩形框
        p1, p2 = (int(box[0]), int(box[1])), (int(box[2]), int(box[3]))
        cv2.rectangle(self.im, p1, p2, color, thickness=self.lw, lineType=cv2.LINE_AA)

        if label:
            # 计算文本大小
            tf = max(self.lw - 1, 1)  # 字体粗细
            font_path = "D:/游戏/脚本/yolov5/utils/fonts/SimHei.ttf"  # 替换为有效的中文字体路径
            font = ImageFont.truetype(font_path, size=int(self.lw * 10))  # 调整字体大小
            pil_image = Image.fromarray(self.im)
            draw = ImageDraw.Draw(pil_image)
            
            # 使用 textbbox 获取文本框的宽高
            bbox = draw.textbbox((0, 0), label, font=font)  # 获取文本的边界框
            w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]  # 计算文本宽高
            
            outside = p1[1] - h >= 3  # 判断文字是否显示在框外
            p2 = (p1[0] + w, p1[1] - h - 3) if outside else (p1[0] + w, p1[1] + h + 3)

            # 画背景框
            cv2.rectangle(self.im, p1, p2, color, -1, cv2.LINE_AA)

            # 使用 Pillow 绘制中文标签
            draw.text((p1[0], p1[1] - 2 if outside else p1[1] + h + 2), label, font=font, fill=txt_color)
            self.im = np.array(pil_image)
