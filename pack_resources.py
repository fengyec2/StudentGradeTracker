# -*- coding: utf-8 -*-
# 用于运行前编译pyside的资源文件和ui文件，并自动更新qrc文件中的qss资源
import os
import site
import xml.etree.ElementTree as ET
from pathlib import Path

def update_qrc_with_qss(qrc_file="resource/resource.qrc", qss_dir="resource/qss"):
    """自动将qss文件添加到qrc资源文件中"""
    # 确保qss目录存在
    if not os.path.exists(qss_dir):
        print(f"QSS目录 {qss_dir} 不存在，跳过更新qrc文件")
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
    
    # 遍历qss目录
    qss_dir_path = Path(qss_dir)
    added_files = []
    for qss_file in qss_dir_path.glob("**/*.qss"):
        # 转换为相对路径（相对于qrc文件所在目录）
        rel_path = os.path.relpath(qss_file, start=os.path.dirname(qrc_file))
        
        # 如果文件不在qrc中，则添加
        if rel_path.replace("\\", "/") not in existing_files:
            file_elem = ET.SubElement(qresource, "file")
            file_elem.text = rel_path.replace("\\", "/")
            added_files.append(rel_path)
    
    # 如果有新增文件，则写入qrc文件
    if added_files:
        # 美化XML输出
        from xml.dom import minidom
        xml_str = ET.tostring(root, encoding="utf-8")
        pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="    ")
        
        # 写入文件
        with open(qrc_file, "w", encoding="utf-8") as f:
            f.write(pretty_xml)
        print(f"已更新 {qrc_file}，新增了 {len(added_files)} 个qss文件")
    else:
        print(f"{qrc_file} 无需更新，没有新增的qss文件")

def main():
    # 1. 首先更新qrc文件，包含所有qss文件
    update_qrc_with_qss()
    
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
    ui_views = os.listdir('ui_view')
    
    for ui_view in ui_views:
        if ui_view.endswith('.ui'):
            output = f"ui_view/ui_{ui_view.split('.')[0]}.py"
            os.system(f"pyside6-uic ui_view/{ui_view} -o {output}")
    
    for ui_file in ui_files:
        if ui_file.endswith('.ui'):
            output = f"ui_page/ui_{ui_file.split('.')[0]}.py"
            os.system(f"pyside6-uic ui_page/{ui_file} -o {output}")
            # if os.name != 'nt':
            #     remove_setfont_from_ui(output,output)

if __name__ == "__main__":
    main()