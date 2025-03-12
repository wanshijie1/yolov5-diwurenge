import os
import xml.etree.ElementTree as ET

# 类别列表（根据你的标注顺序）
classes = ["狂欢之椅", "木板", "密码机", "求生者",  "脚印", "技能", "设置", "退出游戏", "大厅", "自由匹配", "监管者", "开始游戏", "准备案件还原", "准备开始"]

def convert_xml_to_yolo(xml_path, output_dir):
    # 解析XML文件
    tree = ET.parse(xml_path)
    root = tree.getroot()
    
    # 获取图片尺寸
    size = root.find("size") 
    width = int(size.find("width").text)
    height = int(size.find("height").text)
    
    # 创建YOLO格式的标签文件
    yolo_lines = []
    for obj in root.findall("object"):
        class_name = obj.find("name").text
        if class_name not in classes:
            print(f"警告：类别 '{class_name}' 不在classes列表中，请检查！")
            continue
        class_id = classes.index(class_name)  # 获取类别ID
        bndbox = obj.find("bndbox")
        xmin = int(bndbox.find("xmin").text)
        ymin = int(bndbox.find("ymin").text)
        xmax = int(bndbox.find("xmax").text)
        ymax = int(bndbox.find("ymax").text)
        
        # 计算中心点和宽高（归一化）
        x_center = (xmin + xmax) / 2 / width
        y_center = (ymin + ymax) / 2 / height
        box_width = (xmax - xmin) / width
        box_height = (ymax - ymin) / height
        
        # 添加到YOLO格式
        yolo_lines.append(f"{class_id} {x_center} {y_center} {box_width} {box_height}")
    
    # 保存YOLO格式标签文件
    output_path = os.path.join(output_dir, os.path.basename(xml_path).replace(".xml", ".txt"))
    with open(output_path, "w") as f:
        f.write("\n".join(yolo_lines))

# 批量转换
xml_dir = "data/log"  # XML文件目录
output_dir = "data/yolo"  # 输出YOLO标签目录
os.makedirs(output_dir, exist_ok=True)

for xml_file in os.listdir(xml_dir):
    if xml_file.endswith(".xml"):
        convert_xml_to_yolo(os.path.join(xml_dir, xml_file), output_dir)