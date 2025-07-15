# 📊 学生成绩跟踪工具

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-6.0+-green.svg)

一个 Fluent Design 风格 UI 的学生成绩跟踪分析工具，提供成绩可视化、趋势分析和班级对比等功能。

模板来自 [Cheukfung/pyqt-fluent-widgets-template](https://github.com/Cheukfung/pyqt-fluent-widgets-template)

## ✨ 功能特性

| 功能 | 状态 |
|------|------|
| 📁 原始文件 | ✅ 已实现 |
| 📈 成绩曲线 | ✅ 已实现 |
| 📋 个人成绩 | ✅ 已实现 |
| 🎎 班级成绩 | ✅ 已实现 |
| 👑 班单科王 | ✅ 已实现 |
| 🔍 第一对比 | ✅ 已实现 |
| ⚙️ 系统设置 | ✅ 已实现 |

|  原始文件  |  成绩曲线  |  个人成绩  |
|-----------|-----------|------------|
| ![原始文件](docs/screen_shot/raw_data.png "原始文件") | ![成绩曲线](docs/screen_shot/trend_chart.png "成绩曲线") | ![个人成绩](docs/screen_shot/score_table.png "个人成绩") |

|  班级成绩  |  班单科王  |  第一对比  |
|-----------|-----------|------------|
| ![班级成绩](docs/screen_shot/class_compare.png "班级成绩") | ![班单科王](docs/screen_shot/top_in_class.png "班单科王") | ![第一对比](docs/screen_shot/top_in_grade.png "第一对比") |

## 🚀 快速开始

### 环境要求

- Python 3.8+
- PySide6

### 安装与运行

```bash
# 克隆仓库
git clone https://github.com/fengyec2/StudentGradeTracker.git
cd StudentGradeTracker

# 安装依赖
pip install -r requirements.txt

# 打包资源
python pack_resources.py

# 运行程序
python entry.py
```

## 🏗 项目结构

```plaintext
├── api/                    # API接口层
├── common/                 # 通用工具库
├── components/             # 自定义组件库
├── data/                   # 考试数据存储
├── resource/               # 资源文件
├── ui_page/                # Qt Designer UI文件
├── view/                   # 视图层
├── worker/                 # 异步任务管理
├── build_xxx.py            # 打包脚本
├── entry.py                # 程序入口
└── pack_resources.py       # 资源编译脚本
```

## 🛠 开发指南

### UI 设计流程

1. 使用 Qt Designer 编辑 `ui_page/` 目录下的 .ui 文件
2. 保存修改后运行资源打包脚本：
   ```bash
   python pack_resources.py
   ```

### 添加新页面

1. 在 `ui_page/` 添加新 .ui 文件
2. 运行资源打包脚本
3. 在 `view/pages/` 创建对应的 .py 和 _handler.py 文件

### 数据存储规范

```bash
data/
├── exams/                  # 所有考试原始文件
│   ├── 期中_2023-04.xlsx   # 文件名包含关键信息
│   └── 月考_2023-05.xlsx
│
├── students/               # 按学生归档
│   ├── 张三.json           # 结构见下文
│   └── 李四.json
│
└── exam_meta.json          # 考试顺序管理
```

**`exam_meta.json` - 考试顺序控制**:
```json
{
  "exams_order": [
    {
      "filename": "期中_2023-04.xlsx",
      "display_name": "高二下期中考试",
      "real_date": "2023-04-15"
    }
  ]
}
```

**`students/张三.json` - 学生数据**:
```json
{
  "student": "张三",
  "class": "5",
  "exams": [
    {
      "filename": "期中_2023-04.xlsx",
      "real_date": "2023-04-15",
      "subjects": [
        {
          "subject": "数学",
          "score": 85,
          "rank": 12
        }
      ],
      "rank": 171
    }
  ]
}
```

## 💻 开发实践

- **分层架构**：UI 与业务逻辑分离
- **异步处理**：使用 QRunnable 处理耗时操作
- **配置管理**：通过 config.json 管理用户设置
- **日志系统**：内置 Logger 模块记录运行日志
