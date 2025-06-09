import os
from common.config import VERSION, AUTHOR

app_name = 'StudentGradeTracker'
build_command = "nuitka --standalone --mingw64 --enable-plugin=pyside6 "
build_command += "--assume-yes-for-downloads "
build_command += "--windows-console-mode=disable "
build_command += "--windows-icon-from-ico=resource/images/logo.png --output-dir=out "
build_command += f"--windows-company-name={AUTHOR}  --windows-product-name={app_name} "
build_command += f"--windows-product-version={VERSION} "
build_command += "--follow-import-to=common,components,view entry.py"

# 运行资源打包脚本
os.system("python pack_resources.py")
print(build_command)
os.system(build_command)  # 执行打包
