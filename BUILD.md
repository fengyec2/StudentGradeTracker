一个基于 [PyQt-Fluent-Widgets](https://github.com/zhiyiYo/PyQt-Fluent-Widgets/) 的现代化UI模板，适配Qt
Designer使用，专为PySide6开发者打造的快速开发解决方案。

## ✨ 主要特性

- 🎨 内置Fluent Design风格组件库
- 📝 Qt Designer友好，支持可视化设计
- 🔄 预置主界面切换逻辑
- ⚡ QRunnable异步任务封装
- 📦 开箱即用的项目模板结构
- 🌙 支持亮/暗主题切换
- 📌 内置配置管理和日志模块

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

#### UI设计

1. 使用Qt Designer打开 `ui_page/` 目录下的.ui文件
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

## 📦 项目打包

### 使用Nuitka打包

```bash
# 安装打包工具
pip install nuitka

# 执行打包脚本
python build.py
```

### 生成安装包

推荐使用 [Inno Setup](https://jrsoftware.org/isinfo.php) 创建Windows安装程序

## 🛠 项目结构

```
├── api/                    # API接口层
│   └── api.py              # 接口主模块
├── common/                 # 通用工具库
│   ├── aes.py              # AES加密模块
│   ├── config.py           # 配置管理
│   ├── my_logger.py        # 日志系统
│   └── utils.py            # 通用工具类
├── components/             # 自定义组件库
├── resource/               # 资源文件目录
├── ui_page/                # 页面UI文件目录
├── ui_view/                # 登录界面UI文件
├── view/                   # 视图层
│   ├── login_window/       # 登录窗口模块
│   │   ├── handler.py      # 登录逻辑处理
│   │   └── window.py       # 登录窗口实现
│   ├── pages/              # 功能页面
│   │   ├── page_one.py              # 页面1视图
│   │   ├── page_one_handler.py      # 页面1业务逻辑
│   │   ├── page_two.py              # 页面2视图
│   │   └── setting_page.py          # 设置页面
│   └── main_window.py      # 主窗口控制器
├── worker/                 # 异步任务管理
│   └── TaskManager.py      # 任务管理器
├── build.py                # 打包脚本
├── entry.py                # 程序入口
└── pack_resources.py       # 资源编译脚本
```

## 💡 最佳实践

- 使用 **Handler分层架构** 分离UI与业务逻辑
- 通过 **QRunnable** 实现耗时操作异步化
- 利用 **config.json** 管理用户配置
- 使用预置的 **Logger** 模块进行日志记录



### 功能设计

1. 原始文件（查看导入的原始xlsx文件）
2. 折线图（选择同学，显示该同学历次考试的年纪排名折线图）
3. 成绩单（选择同学，汇总该同学历次考试的成绩表格）
4. 设置

---

### **简化版数据存储设计**
#### 📂 文件结构（仅保留必要部分）
```bash
data/
├── exams/                  # 所有考试原始文件
│   ├── 期中_数学_2023-04.xlsx   # 文件名包含关键信息
│   └── 月考_英语_2023-05.xlsx
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
    {"filename": "期中_2023-04.xlsx", "display_name": "高二下期中考试", "real_date": "2023-04-15"},
    {"filename": "月考_2023-05.xlsx", "display_name": "五月月考", "real_date": "2023-05-12"}
  ]
}
```

2. **`students/张三.json` - 学生数据**
```json
{
  "student": "张三",
  "exams": [
    {
      "filename": "期中_2023-04.xlsx",
      "real_date": "2023-04-15",
      "subjects": [
        {
          "subject": "数学",
          "score": 85,
          "rank": 12
        },
        {
          "subject": "语文",
          "score": 92,
          "rank": 5
        },
        {
          "subject": "英语",
          "score": 78,
          "rank": 20
        }
      ],
      "rank": 171,
    }
  ]
}

```


---

### **⚡ 动态加载简化方案**
#### 1. 折线图数据加载流程
```python
def load_student_trend(student_name):
    # 1. 读取学生所有成绩
    with open(f"data/students/{student_name}.json") as f:
        all_scores = json.load(f)["scores"]
    
    # 2. 关联考试顺序
    with open("data/exam_meta.json") as f:
        exams_order = {e["filename"]: idx for idx, e in enumerate(json.load(f)["exams_order"])}
    
    # 3. 按考试顺序排序
    sorted_scores = sorted(all_scores, key=lambda x: exams_order[x["exam"]])
    
    return {
        "labels": [score["exam"] for score in sorted_scores],
        "rank_data": [score["rank"] for score in sorted_scores]
    }
```

#### 2. Excel导入处理
```python
def import_exam(filepath, exam_date, display_name):
    # 1. 生成规范文件名
    filename = f"{display_name}_{exam_date.strftime('%Y-%m')}.xlsx"
    
    # 2. 保存原始文件
    shutil.copy(filepath, f"data/exams/{filename}")
    
    # 3. 更新学生数据
    df = pd.read_excel(filepath)
    for _, row in df.iterrows():
        student_file = f"data/students/{row['姓名']}.json"
        if not os.path.exists(student_file):
            init_student_file(student_file)  # 创建新学生文件
        
        update_student_scores(student_file, filename, row)  # 添加本次成绩
    
    # 4. 更新考试顺序
    update_exam_meta(filename, display_name, exam_date)
```

---

### **🛠️ 实现建议（分步聚焦核心）**
1. **先完成单次考试处理**
   - 实现Excel导入 → 学生JSON更新

2. **再开发基础查询**
   - 读取单个学生所有成绩
   - 控制台打印简单折线图（用`*`字符绘制）

---

### **💡 示例：完整导入流程（教师视角）**
1. 点击"导入"按钮选择Excel文件
2. 弹出表单填写：
   - 考试日期（日期选择器）
   - 考试别名（如"四月月考"）
3. 程序自动生成预览：
   - 检测到的学生人数
   - 科目列表确认
4. 点击确认后完成存储
