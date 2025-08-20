import os
from common.config import VERSION, AUTHOR

app_name = 'StudentGradeTracker'
build_command = "nuitka --standalone --enable-plugin=pyside6 "
build_command += "--assume-yes-for-downloads "
build_command += "--mode=app "
build_command += "--macos-app-icon=resource/images/logo.png --output-dir=out "
build_command += f"--macos-app-name={app_name} "
build_command += f"--macos-app-version={VERSION} "
build_command += f"--macos-sign-identity=- "
build_command += "--follow-import-to=common,components,view entry.py"

# 运行资源打包脚本
os.system("python pack_resources.py")
print(build_command)
os.system(build_command)  # 执行打包