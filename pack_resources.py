# -*- coding: utf-8 -*-
# 用于运行前编译pyside的资源文件和ui文件，并自动更新qrc文件中的qss资源和svg图标
import os
import site
import xml.etree.ElementTree as ET
from pathlib import Path

def format_xml_without_empty_lines(element, level=0):
    """
    手动格式化XML，避免minidom产生的空行问题
    """
    indent = "    " * level
    if len(element):
        if not element.text or not element.text.strip():
            element.text = f"\n{indent}    "
        if not element.tail or not element.tail.strip():
            element.tail = f"\n{indent}"
        for child in element:
            format_xml_without_empty_lines(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = f"\n{indent}"
    else:
        if level and (not element.tail or not element.tail.strip()):
            element.tail = f"\n{indent}"

def update_qrc_with_resources(qrc_file="resource/resource.qrc", qss_dir="resource/qss", svg_dir="resource/images/icons"):
    """自动将qss文件和svg文件添加到qrc资源文件中"""
    # 确保目录存在
    dirs_to_check = [
        (qss_dir, "QSS"),
        (svg_dir, "SVG")
    ]
    
    available_dirs = []
    for dir_path, dir_type in dirs_to_check:
        if os.path.exists(dir_path):
            available_dirs.append((dir_path, dir_type))
        else:
            print(f"{dir_type}目录 {dir_path} 不存在，跳过")
    
    if not available_dirs:
        print("没有找到可用的资源目录，跳过更新qrc文件")
        return
   
    # 解析现有的qrc文件或创建新的
    try:
        if os.path.exists(qrc_file):
            tree = ET.parse(qrc_file)
            root = tree.getroot()
        else:
            root = ET.Element("RCC")
            tree = ET.ElementTree(root)
            qresource = ET.SubElement(root, "qresource")
            qresource.set("prefix", "/")
    except ET.ParseError as e:
        print(f"解析qrc文件失败: {e}")
        return
   
    # 查找或创建qresource标签
    qresource = root.find("qresource")
    if qresource is None:
        qresource = ET.SubElement(root, "qresource")
        qresource.set("prefix", "/")
   
    # 收集所有现有的文件路径
    existing_files = {file_elem.text for file_elem in qresource.findall("file")}
   
    # 定义要处理的文件类型
    file_types = [
        (qss_dir, "**/*.qss", "QSS"),
        (svg_dir, "**/*.svg", "SVG")
    ]
    
    total_added_files = []
    
    # 遍历所有资源目录
    for resource_dir, pattern, file_type in file_types:
        if not os.path.exists(resource_dir):
            continue
            
        resource_dir_path = Path(resource_dir)
        added_files = []
        
        for resource_file in resource_dir_path.glob(pattern):
            # 转换为相对路径（相对于qrc文件所在目录）
            rel_path = os.path.relpath(resource_file, start=os.path.dirname(qrc_file))
           
            # 如果文件不在qrc中，则添加
            if rel_path.replace("\\", "/") not in existing_files:
                file_elem = ET.SubElement(qresource, "file")
                file_elem.text = rel_path.replace("\\", "/")
                added_files.append(rel_path)
        
        if added_files:
            total_added_files.extend(added_files)
            print(f"新增了 {len(added_files)} 个{file_type}文件")
   
    # 如果有新增文件，则写入qrc文件
    if total_added_files:
        # 使用自定义的格式化函数，避免空行问题
        format_xml_without_empty_lines(root)
        
        # 创建XML声明和格式化输出
        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_content = ET.tostring(root, encoding="unicode")
        
        # 确保qrc文件目录存在
        os.makedirs(os.path.dirname(qrc_file), exist_ok=True)
        
        # 写入文件
        with open(qrc_file, "w", encoding="utf-8") as f:
            f.write(xml_declaration + xml_content)
        print(f"已更新 {qrc_file}，总共新增了 {len(total_added_files)} 个资源文件")
    else:
        print(f"{qrc_file} 无需更新，没有新增的资源文件")

def clean_existing_qrc_file(qrc_file="resource/resource.qrc"):
    """清理现有qrc文件中的空行问题"""
    if not os.path.exists(qrc_file):
        print(f"文件 {qrc_file} 不存在")
        return
    
    try:
        # 解析现有文件
        tree = ET.parse(qrc_file)
        root = tree.getroot()
        
        # 重新格式化
        format_xml_without_empty_lines(root)
        
        # 写回文件
        xml_declaration = '<?xml version="1.0" encoding="UTF-8"?>\n'
        xml_content = ET.tostring(root, encoding="unicode")
        
        with open(qrc_file, "w", encoding="utf-8") as f:
            f.write(xml_declaration + xml_content)
            
        print(f"已清理 {qrc_file} 中的空行")
        
    except ET.ParseError as e:
        print(f"解析qrc文件失败: {e}")

def main():
    # 0. 首先清理现有qrc文件中的空行（可选）
    clean_existing_qrc_file()
    
    # 1. 然后更新qrc文件，包含所有qss文件和svg文件
    update_qrc_with_resources()
   
    # 2. 找到site-packages目录
    site_packages_path = site.getsitepackages()[-1]
   
    # 3. 找到pyside6的lrelease.exe的路径
    lr = 'lrelease.exe' if os.name == 'nt' else 'lrelease'
    lrelease_path = os.path.join(site_packages_path, 'PySide6', lr)
   
    # 4. 编译翻译文件
    os.system(f'{lrelease_path} -verbose resource/i18n/zh.ts -qm resource/i18n/zh.qm')
   
    # 5. 编译资源文件
    os.system("pyside6-rcc resource/resource.qrc -o resource_rc.py")
   
    # 6. 编译ui文件
    ui_files = os.listdir('ui_page')
    # ui_views = os.listdir('ui_view')
   
    # for ui_view in ui_views:
    #     if ui_view.endswith('.ui'):
    #         output = f"ui_view/ui_{ui_view.split('.')[0]}.py"
    #         os.system(f"pyside6-uic ui_view/{ui_view} -o {output}")
   
    for ui_file in ui_files:
        if ui_file.endswith('.ui'):
            output = f"ui_page/ui_{ui_file.split('.')[0]}.py"
            os.system(f"pyside6-uic ui_page/{ui_file} -o {output}")
            # if os.name != 'nt':
            #     remove_setfont_from_ui(output,output)

if __name__ == "__main__":
    main()