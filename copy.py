import os
import shutil

# Source and destination directories
source_dir = r"D:\College\Year 2\CV_ITA0505\Practical\ComputerVision_12to40"
target_root = r"D:\College\Year 2\CV_ITA0505\Practical\Programs\ITA0505"

# Loop through program numbers 12–40
for i in range(12, 41):
    file_name = f"{i}.py"
    src = os.path.join(source_dir, file_name)
    dst_folder = os.path.join(target_root, f"Program {i}")
    dst = os.path.join(dst_folder, file_name)

    if os.path.exists(src) and os.path.isdir(dst_folder):
        shutil.copy2(src, dst)  # copy2 keeps timestamps
        print(f"✅ Copied {file_name} → {dst_folder}")
    else:
        print(f"⚠️ Missing file or folder for Program {i}")
