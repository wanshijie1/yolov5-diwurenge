import cv2
import os
import time

# 视频文件夹路径
video_folder = "视屏"

# 设置截取间隔（秒）
interval_seconds = 2  # 每隔2秒截取一张图片

# 创建保存图片的文件夹
output_folder = "data/frames"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 全局计数器，用于生成唯一的图片文件名
global_frame_count = 0

# 记录开始时间
start_time = time.time()

# 遍历文件夹中的所有视频文件
for video_name in os.listdir(video_folder):
    video_path = os.path.join(video_folder, video_name)
    
    # 打开视频
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"无法打开视频文件: {video_name}")
        continue

    # 获取视频帧率
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        print(f"无法获取视频帧率: {video_name}")
        cap.release()
        continue

    # 计算间隔帧数
    interval_frames = int(fps * interval_seconds)

    # 初始化计数器
    frame_count = 0

    # 开始提取
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        # 每隔interval_frames帧保存一张图片
        if frame_count % interval_frames == 0:
            output_path = os.path.join(output_folder, f"frame_{global_frame_count:06d}.jpg")
            cv2.imwrite(output_path, frame)
            global_frame_count += 1  # 全局计数器递增
        
        frame_count += 1

    cap.release()
    print(f"视频 {video_name} 处理完成，共保存 {global_frame_count} 帧图片。")

# 记录结束时间
end_time = time.time()

# 计算总用时
total_time = end_time - start_time

# 输出总用时和处理的图片数量
print(f"所有视频处理完成，共保存 {global_frame_count} 帧图片。")
print(f"总用时: {total_time:.2f} 秒")