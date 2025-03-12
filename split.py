import os
import shutil
from sklearn.model_selection import train_test_split

# 原始图片和标签目录
image_dir = "D:/游戏/脚本/data/frames"
label_dir = "D:/游戏/脚本/data/yolo"

# 目标目录
dataset_dir = "dataset"
os.makedirs(os.path.join(dataset_dir, "images/train"), exist_ok=True)
os.makedirs(os.path.join(dataset_dir, "images/val"), exist_ok=True)
os.makedirs(os.path.join(dataset_dir, "labels/train"), exist_ok=True)
os.makedirs(os.path.join(dataset_dir, "labels/val"), exist_ok=True)

# 获取所有图片文件名
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
train_files, val_files = train_test_split(image_files, test_size=0.2, random_state=42)

# 复制训练集
for file in train_files:
    label_file = file.replace(".jpg", ".txt")
    label_path = os.path.join(label_dir, label_file)
    
    if not os.path.exists(label_path):
        print(f"警告：标签文件 {label_file} 不存在，跳过图片 {file}")
        continue
    
    shutil.copy(os.path.join(image_dir, file), os.path.join(dataset_dir, "images/train", file))
    shutil.copy(label_path, os.path.join(dataset_dir, "labels/train", label_file))

# 复制验证集
for file in val_files:
    label_file = file.replace(".jpg", ".txt")
    label_path = os.path.join(label_dir, label_file)
    
    if not os.path.exists(label_path):
        print(f"警告：标签文件 {label_file} 不存在，跳过图片 {file}")
        continue
    
    shutil.copy(os.path.join(image_dir, file), os.path.join(dataset_dir, "images/val", file))
    shutil.copy(label_path, os.path.join(dataset_dir, "labels/val", label_file))