# 📊 学生成绩跟踪工具

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-6.0+-green.svg)

一个基于PySide6开发的现代化学生成绩跟踪分析工具，提供成绩可视化、趋势分析和班级对比功能。

模板来自 [Cheukfung](https://github.com/Cheukfung/pyqt-fluent-widgets-template)

## ✨ 功能特性

- 📈 学生个人成绩趋势折线图
- 📊 班级学科平均分对比
- 📂 Excel原始数据导入
- 🎨 Fluent Design风格UI
- ⚡ 异步任务处理

## 🚀 快速开始

### 环境要求

- Python 3.8+
- PySide6

### 安装与运行

```bash
# 克隆仓库
git clone https://github.com/Cheukfung/pyqt-fluent-widgets-template.git
cd pyqt-fluent-widgets-template

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
├── build.py                # 打包脚本
├── entry.py                # 程序入口
└── pack_resources.py       # 资源编译脚本
```

## 🛠 开发指南

### UI设计流程

1. 使用Qt Designer编辑`ui_page/`目录下的.ui文件
2. 保存修改后运行资源打包脚本：
   ```bash
   python pack_resources.py
   ```

### 添加新页面

1. 在`ui_page/`添加新.ui文件
2. 运行资源打包脚本
3. 在`view/pages/`创建对应的.py和_handler.py文件

### 数据存储规范

```plaintext
data/
├── exams/                  # 考试原始Excel文件
├── students/               # 学生成绩JSON数据
└── exam_meta.json          # 考试元数据
```

**exam_meta.json示例**:
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

**学生数据示例**:
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

## 📝 功能模块

| 功能 | 状态 |
|------|------|
| 原始文件查看 | ✅ 已实现 |
| 成绩趋势折线图 | ✅ 已实现 |
| 个人成绩汇总 | ✅ 已实现 |
| 班级成绩对比 | ✅ 已实现 |
| 系统设置 | ✅ 已实现 |

## 💻 开发实践

- **分层架构**：UI与业务逻辑分离
- **异步处理**：使用QRunnable处理耗时操作
- **配置管理**：通过config.json管理用户设置
- **日志系统**：内置Logger模块记录运行日志
