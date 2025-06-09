import os
from common.config import VERSION, AUTHOR

app_name = 'StudentGradeTracker'
build_command = "nuitka --standalone --enable-plugin=pyside6 "
build_command += "--assume-yes-for-downloads "
build_command += "--output-dir=out "
build_command += "--follow-import-to=common,components,view "
build_command += "--include-data-dir=./resource=resource "  # 包含资源文件
# build_command += "--remove-output "  # 移除调试信息减小体积
build_command += "--lto=yes "  # 启用链接时优化（可选）
build_command += "entry.py"

# 运行资源打包脚本
os.system("python pack_resources.py")
print(build_command)
os.system(build_command)  # 执行打包