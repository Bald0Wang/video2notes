import os
import subprocess
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

class VideoClipperApp:
    def __init__(self, root):
        self.root = root
        self.root.title("基于FFmpeg的视频剪辑工具")

        # 视频文件路径
        self.video_path = ""
        Label(root, text="视频文件:").grid(row=0, column=0)
        self.video_entry = Entry(root, width=50)
        self.video_entry.grid(row=0, column=1)
        Button(root, text="上传视频", command=self.upload_video).grid(row=0, column=2)

        # 剪辑开始时间
        Label(root, text="开始时间 (格式: HH:MM:SS):").grid(row=1, column=0)
        self.start_entry = Entry(root, width=10)
        self.start_entry.grid(row=1, column=1)

        # 剪辑结束时间
        Label(root, text="结束时间 (格式: HH:MM:SS):").grid(row=2, column=0)
        self.end_entry = Entry(root, width=10)
        self.end_entry.grid(row=2, column=1)

        # 输出位置
        Label(root, text="输出位置:").grid(row=3, column=0)
        self.output_entry = Entry(root, width=50)
        self.output_entry.grid(row=3, column=1)
        Button(root, text="选择输出位置", command=self.select_output).grid(row=3, column=2)

        # 输出文件名
        Label(root, text="输出文件名:").grid(row=4, column=0)
        self.filename_entry = Entry(root, width=50)
        self.filename_entry.grid(row=4, column=1)

        # 剪辑按钮
        Button(root, text="剪辑视频", command=self.clip_video).grid(row=5, column=1)

    def upload_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("视频文件", "*.mp4 *.avi *.mov *.mkv")])
        self.video_entry.delete(0, 'end')
        self.video_entry.insert(0, self.video_path)

    def select_output(self):
        output_dir = filedialog.askdirectory()
        self.output_entry.delete(0, 'end')
        self.output_entry.insert(0, output_dir)

    def clip_video(self):
        video_path = self.video_path
        start_time = self.start_entry.get()
        end_time = self.end_entry.get()
        output_dir = self.output_entry.get()
        filename = self.filename_entry.get()

        if not video_path:
            messagebox.showerror("错误", "请先上传视频文件")
            return

        if not output_dir:
            messagebox.showerror("错误", "请选择输出位置")
            return

        if not filename:
            base_name = os.path.splitext(os.path.basename(video_path))[0]
            filename = f"{base_name}_剪辑.mp4"

        output_path = os.path.join(output_dir, filename)

        try:
            # 构建FFmpeg命令
            command = [
                "ffmpeg",
                "-i", video_path,          # 输入文件
                "-ss", start_time,         # 开始时间
                "-to", end_time,           # 结束时间
                "-c", "copy",              # 直接复制流，无需重新编码
                output_path                # 输出文件
            ]

            # 执行FFmpeg命令
            subprocess.run(command, check=True)
            messagebox.showinfo("成功", f"视频已成功剪辑并保存到 {output_path}")
        except subprocess.CalledProcessError as e:
            messagebox.showerror("错误", f"剪辑视频时出错: {e}")
        except Exception as e:
            messagebox.showerror("错误", f"发生未知错误: {e}")

if __name__ == "__main__":
    root = Tk()
    app = VideoClipperApp(root)
    root.mainloop()