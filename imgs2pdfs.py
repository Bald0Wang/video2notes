import os
import img2pdf

# 指定图片文件夹路径
folder_path = 'main_output'  # 替换为你的图片文件夹路径

# 获取文件夹中所有文件
files = os.listdir(folder_path)

# 按文件名排序
sorted_files = sorted(files)

# 构建图片文件的完整路径列表
image_paths = [os.path.join(folder_path, file) for file in sorted_files]

# 生成PDF文件
with open("output.pdf", "wb") as f:
    f.write(img2pdf.convert(image_paths))

print("PDF生成完成！")