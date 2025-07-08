# 视频处理工具集 (Video Tools)

这是一个基于Python的视频处理工具集，提供视频剪辑、帧提取和图片转PDF等功能。

本项目意在将学习类视频文件拆分为关键帧，然后将关键帧分析处理，并结合语音工具生成笔记。

## 功能特性

### 1. 视频剪辑工具 (`jianji.py`)
- 基于FFmpeg的GUI视频剪辑工具
- 支持多种视频格式 (MP4, AVI, MOV, MKV)
- 精确的时间控制 (HH:MM:SS格式)
- 快速剪辑，无需重新编码

### 2. 视频帧提取工具 (`test.py`)
- 多线程视频帧提取
- 智能场景检测，只保存有变化的帧
- 支持大视频文件的高效处理
- 自动创建输出目录

### 3. 图片转PDF工具 (`imgs2pdfs.py`)
- 将图片序列转换为PDF文档
- 按文件名自动排序
- 支持批量处理

## 环境要求

- Python 3.6+
- FFmpeg (用于视频剪辑)
- OpenCV (`cv2`)
- NumPy
- img2pdf
- tkinter (Python内置)

## 安装依赖

```bash
pip install opencv-python numpy img2pdf
```

### FFmpeg安装

#### Windows:
1. 下载FFmpeg: https://ffmpeg.org/download.html
2. 解压到任意目录
3. 将FFmpeg的bin目录添加到系统PATH环境变量

#### macOS:
```bash
brew install ffmpeg
```

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install ffmpeg
```

## 使用方法

### 视频剪辑
```bash
python jianji.py
```
1. 点击"上传视频"选择要剪辑的视频文件
2. 输入开始时间和结束时间 (格式: HH:MM:SS)
3. 选择输出位置和文件名
4. 点击"剪辑视频"开始处理

### 视频帧提取
```bash
python test.py
```
- 程序会自动处理 `main.mp4` 文件
- 提取的帧会保存到 `main_output/` 目录
- 使用多线程处理，提高效率

### 图片转PDF
```bash
python imgs2pdfs.py
```
- 将 `main_output/` 目录中的图片转换为 `output.pdf`
- 图片按文件名自动排序

## 项目结构

```
video_tools/
├── jianji.py          # 视频剪辑GUI工具
├── test.py            # 视频帧提取工具
├── imgs2pdfs.py       # 图片转PDF工具
├── main.mp4           # 示例视频文件
├── test.mp4           # 测试视频文件
├── output.pdf         # 生成的PDF文件
├── main_output/       # 提取的视频帧
├── test_output/       # 测试输出目录
└── README.md          # 项目说明文档
```

## 注意事项

1. **大文件处理**: 处理大视频文件时，确保有足够的磁盘空间
2. **FFmpeg依赖**: 视频剪辑功能需要正确安装FFmpeg
3. **内存使用**: 帧提取工具会占用较多内存，建议处理大文件时关闭其他程序
4. **文件格式**: 支持的视频格式取决于FFmpeg的安装配置

## 故障排除

### 常见问题

1. **FFmpeg未找到错误**
   - 确保FFmpeg已正确安装并添加到PATH
   - 重启命令行/IDE

2. **内存不足错误**
   - 减少同时处理的线程数
   - 关闭其他占用内存的程序

3. **视频格式不支持**
   - 检查FFmpeg是否支持该格式
   - 尝试转换视频格式

## 开发说明

- 项目使用Python标准库和常用第三方库
- 代码结构清晰，易于扩展
- 支持多线程处理，提高性能

## 许可证

本项目仅供学习和个人使用。

## 贡献

欢迎提交Issue和Pull Request来改进这个项目。 