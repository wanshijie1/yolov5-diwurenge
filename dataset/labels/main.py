import os

label_dir = r"train"  # 修改为你的训练集路径
max_class_id = 13  # 允许的最大类别索引（0-13）

# 遍历所有标签文件
for file in os.listdir(label_dir):
    if file.endswith(".txt"):
        file_path = os.path.join(label_dir, file)
        with open(file_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            parts = line.strip().split()
            if int(parts[0]) > max_class_id:  # 发现超过 13 的类别
                print(f"⚠️ 发现错误类别: {file_path} -> {line.strip()}")
