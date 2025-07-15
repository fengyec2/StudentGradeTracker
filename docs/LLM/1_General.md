## 学生成绩跟踪工具

## 🚀 快速开始

### 环境要求

1. Python 3.8+
2. PySide6

### 快速上手

```bash
# 克隆仓库
git clone https://github.com/Cheukfung/pyqt-fluent-widgets-template.git
cd pyqt-fluent-widgets-template
# 安装依赖
pip install -r requirements.txt
# 打包资源
python pack_resources.py
# 运行
python entry.py
```

### 开发流程

#### UI 设计

1. 使用 Qt Designer 打开 `ui_page/` 目录下的 .ui 文件
2. 添加/修改需要的控件
3. 保存修改后运行资源打包脚本：

```bash
python pack_resources.py
```

#### 业务逻辑开发

- 控件事件绑定：在 `view/pages/` 对应的handler文件中添加逻辑
- 新增页面：
    1. 在 `ui_page/` 添加新.ui文件
    2. 运行资源打包脚本
    3. 在 `view/pages/` 创建对应的.py和_handler.py文件（参考现有页面结构）


## 🛠 项目结构

```
├── common/                 # 通用工具库
│   ├── config.py           # 配置管理
│   ├── my_logger.py        # 日志系统
│   └── utils.py            # 通用工具类
├── components/             # 自定义组件库
├── data/                   # 考试数据
│   ├── exams/              # 功能页面
│   │   └── 三月月考_2025-02.xlsx          # 考试成绩源文件
│   ├── students            # 主窗口控制器
│   │   └── 同学1.json                     # 个人各次考试成绩
│   └── exam_meta.json      # 历次考试元数据
├── resource/               # 资源文件目录
├── ui_page/                # 页面UI文件目录
├── view/                   # 视图层
│   ├── pages/              # 功能页面
│   │   ├── page_one.py                    # 页面1视图（原始文件）
│   │   ├── page_one_handler.py            # 页面1业务逻辑（原始文件）
│   │   ├── page_two.py                    # 页面2视图（折线图）
│   │   ├── page_two_handler.py            # 页面2业务逻辑（折线图）
│   │   ├── page_three.py                  # 页面3视图（成绩单）
│   │   ├── page_three_handler.py          # 页面3业务逻辑（成绩单）
│   │   ├── page_class_grade.py            # 页面3视图（成绩单）
│   │   ├── page_class_grade_handler.py    # 页面3业务逻辑（成绩单）
│   │   └── setting_page.py                # 设置页面
│   └── main_window.py      # 主窗口控制器
├── worker/                 # 异步任务管理
│   └── TaskManager.py      # 任务管理器
├── build_xxx.py            # 打包脚本
├── entry.py                # 程序入口
└── pack_resources.py       # 资源编译脚本
```

## 💡 最佳实践

- 使用 **Handler分层架构** 分离UI与业务逻辑
- 通过 **QRunnable** 实现耗时操作异步化
- 利用 **config.json** 管理用户配置
- 使用预置的 **Logger** 模块进行日志记录



### 功能设计

1. 原始文件（查看导入的原始xlsx文件）（已实现）
2. 成绩曲线（选择同学，显示该同学历次考试的年纪排名折线图）（已实现）
3. 个人成绩（选择同学，汇总该同学历次考试的成绩表格）（已实现）
4. 班级成绩（选择考试，选择班级，计算选择的这次考试中各个班级各个学科的平均分，并以列表/图标显示）（已实现）
5. 班级单科王表现（选择考试，选择班级，以图表的方式显示所选择的班级各科第一与年级对应科目第一的分数情况）（已实现）
6. 班级第一与年级第一对比（选择考试，选择班级，以图表的方式显示所选择的班级总分第一的同学各科成绩与年级总分第一的同学各科成绩的分数情况）（已实现）

---

### **简化版数据存储设计**
#### 📂 文件结构（仅保留必要部分）
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

#### 📝 关键文件说明
1. **`exam_meta.json` - 考试顺序控制**
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

2. **`students/张三.json` - 学生数据**
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

请你先理解我的项目设计书，稍后我会需要你协助完成这个项目的代码编写