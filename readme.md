# 📌 YOLOv5 目标检测完整流程

---

## **第一步 🎥 OBS 录制视频**
使用 OBS 进行屏幕录制，生成视频数据。

---

## **第二步 ✂️ Python 脚本切片**
使用 脚本对录制的视屏 进行视频切片：
```bash
python cut.py
```

---

## **第三步 🏷️ LabelImg 框选**
安装 `labelImg` 并进行标注：
```bash
pip install labelImg
labelImg
```
labelImg 标注完成后，默认保存的是XML文件，需要装换成txt文件，使用 `xml-txt.py` 脚本进行转换：


## **第四步 🏗️ 划分训练集和验证集**
创建 `data.yaml`：，在yolov5环境下创建一个 `data.yaml` 文件，
目录结构如下：
```plaintext
yolov5/
└──data/
    └── data.yaml
```

内容如下：
这里给定一个模板，根据自己数据集进行修改
```yaml
train: ./train/images  # 训练集图片路径
val: ./val/images       # 验证集图片路径
nc: 6                   # 类别数量
names: ['class1', 'class2', 'class3', 'class4', 'class5', 'class6'] # 类别名称
```


## **第五步 ⚙️ 配置 YOLOv5**
克隆 YOLOv5 仓库并安装依赖：
```bash
git clone https://github.com/ultralytics/yolov5.git
cd yolov5
pip install -r requirements.txt
```

---

## **🔥 开始训练**
运行训练命令：
```bash
python train.py --img 640 --batch 16 --epochs 50 --data dataset.yaml --weights yolov5s.pt
```
📌 **参数说明**：
- `--img 640`：输入图片大小
- `--batch 16`：批量大小
- `--epochs 50`：训练轮数
- `--data dataset.yaml`：数据集配置文件
- `--weights yolov5s.pt`：预训练模型权重

---

## **📊 训练结果**
训练完成后，结果存放在 `runs/train/exp` 目录：
```plaintext
weights/               # 最终模型权重
├── last.pt            # 训练最后一次的模型
├── best.pt            # 训练效果最好的模型
results.png            # 训练曲线可视化
labels_correlogram.jpg # 训练集中类别分布热力图
F1_curve.png           # F1 指标曲线
PR_curve.png           # 精确率-召回率曲线
```

---

## **🚀 第六步 测试**
使用最佳模型测试：
```bash
python detect.py --weights runs/train/exp/weights/best.pt --source "D:\dataset\text\hujingcun.mkv" --device cpu
```

📌 **参数说明**：
- `--weights`：指定训练好的模型 (`best.pt`)
- `--source`：输入文件路径（可以是图片/视频）
- `--device`：选择运行设备（`cpu` 或 `cuda`）
- `--conf-thres 0.3`：置信度阈值
- `--iou-thres 0.5`：IoU 阈值

---

## **📌 运行结果**
检测结果会保存在 `runs/detect/exp/` 目录下。

**🎯 你可以在 `runs/detect/exp/` 中查看带有目标检测框的输出视频！**
