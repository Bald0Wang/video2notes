import cv2
import numpy as np
import os
import threading

# 视频路径
video_path = 'main.mp4'

# 创建输出目录
video_name = os.path.splitext(os.path.basename(video_path))[0]  # 获取视频文件名（不含扩展名）
output_dir = f'{video_name}_output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 打开视频文件
cap = cv2.VideoCapture(video_path)

# 获取视频的帧率和总帧数
fps = cap.get(cv2.CAP_PROP_FPS)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 将视频切成 n 份
n = 4  # 切成 4 份
frames_per_part = total_frames // n

# 线程处理函数
def process_video_part(start_frame, end_frame, thread_id):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)  # 设置起始帧

    # 初始化前一帧
    ret, prev_frame = cap.read()
    prev_frame_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    frame_count = start_frame
    saved_frame_count = 0

    while frame_count < end_frame:
        # 读取下一帧
        ret, curr_frame = cap.read()
        if not ret:
            break

        # 转换为灰度图
        curr_frame_gray = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY)

        # 计算帧间差异
        frame_diff = cv2.absdiff(curr_frame_gray, prev_frame_gray)
        diff_percentage = np.sum(frame_diff > 25) / (curr_frame_gray.shape[0] * curr_frame_gray.shape[1])

        # 如果差异度高于10%，保存当前帧
        if diff_percentage > 0.05:
            # 计算当前时间（秒数）
            current_time_seconds = int(frame_count / fps)
            frame_filename = os.path.join(output_dir, f'{current_time_seconds:04d}_thread{thread_id}.jpg')
            cv2.imwrite(frame_filename, curr_frame)
            saved_frame_count += 1

            # 更新前一帧
            prev_frame_gray = curr_frame_gray

        frame_count += 1

        # 跳过帧以达到每秒1帧的效果
        for _ in range(int(fps) - 1):
            cap.read()

    # 释放视频对象
    cap.release()

    print(f"Thread {thread_id}: Frames processed: {frame_count - start_frame}, Frames saved: {saved_frame_count}")

# 创建并启动线程
threads = []
for i in range(n):
    start_frame = i * frames_per_part
    end_frame = (i + 1) * frames_per_part if i < n - 1 else total_frames
    thread = threading.Thread(target=process_video_part, args=(start_frame, end_frame, i))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

print("All threads finished processing.")