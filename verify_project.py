#!/usr/bin/env python3
"""
房价预测项目的快速验证脚本
用于检查数据文件是否存在以及基本功能是否正常
"""

import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path

def check_project_structure():
    """检查项目结构是否完整"""
    print("🔍 检查项目结构...")
    
    required_dirs = [
        'data',
        'notebooks', 
        'models',
        'results',
        'images',
        'docs'
    ]
    
    required_files = [
        'README.md',
        'requirements.txt',
        '.gitignore',
        'LICENSE'
    ]
    
    missing_dirs = []
    missing_files = []
    
    # 检查目录
    for dir_name in required_dirs:
        if not os.path.exists(dir_name):
            missing_dirs.append(dir_name)
    
    # 检查文件
    for file_name in required_files:
        if not os.path.exists(file_name):
            missing_files.append(file_name)
    
    if missing_dirs:
        print(f"❌ 缺少目录: {', '.join(missing_dirs)}")
    if missing_files:
        print(f"❌ 缺少文件: {', '.join(missing_files)}")
    
    if not missing_dirs and not missing_files:
        print("✅ 项目结构完整")
        return True
    return False

def check_data_files():
    """检查数据文件是否存在"""
    print("\n📊 检查数据文件...")
    
    train_file = 'data/train.csv'
    test_file = 'data/test.csv'
    
    if os.path.exists(train_file) and os.path.exists(test_file):
        print("✅ 数据文件存在")
        
        # 简单验证数据
        try:
            train_df = pd.read_csv(train_file)
            test_df = pd.read_csv(test_file)
            
            print(f"📈 训练集: {train_df.shape[0]} 样本, {train_df.shape[1]} 特征")
            print(f"📉 测试集: {test_df.shape[0]} 样本, {test_df.shape[1]} 特征")
            
            if 'SalePrice' in train_df.columns:
                print(f"💰 房价范围: ${train_df['SalePrice'].min():,.0f} - ${train_df['SalePrice'].max():,.0f}")
            
            return True
            
        except Exception as e:
            print(f"❌ 数据文件读取错误: {e}")
            return False
    else:
        print("⚠️  数据文件不存在，请添加 train.csv 和 test.csv 到 data/ 目录")
        return False

def check_notebooks():
    """检查笔记本文件"""
    print("\n📓 检查笔记本文件...")
    
    notebooks = [
        'notebooks/01_descriptive_analysis.ipynb',
        'notebooks/02_feature_engineering_tsne.ipynb',
        'notebooks/03_gbdt_modeling.ipynb',
        'notebooks/04_visualization_analysis.ipynb'
    ]
    
    all_exist = True
    for notebook in notebooks:
        if os.path.exists(notebook):
            print(f"✅ {notebook}")
        else:
            print(f"❌ {notebook}")
            all_exist = False
    
    return all_exist

def check_dependencies():
    """检查依赖包是否可以导入"""
    print("\n📦 检查依赖包...")
    
    packages = [
        'pandas',
        'numpy', 
        'matplotlib',
        'seaborn',
        'sklearn',
        'xgboost'
    ]
    
    missing_packages = []
    
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n安装缺少的包: pip install {' '.join(missing_packages)}")
        return False
    return True

def main():
    """主函数"""
    print("🏠 房价预测项目验证脚本")
    print("=" * 40)
    
    # 更改到项目根目录
    script_dir = Path(__file__).parent
    os.chdir(script_dir)
    
    all_good = True
    
    # 运行所有检查
    all_good &= check_project_structure()
    all_good &= check_dependencies()  
    all_good &= check_notebooks()
    all_good &= check_data_files()
    
    print("\n" + "=" * 40)
    if all_good:
        print("🎉 项目验证通过！可以开始分析了。")
        print("\n快速开始:")
        print("1. jupyter notebook")
        print("2. 按顺序运行以下笔记本：")
        print("   - 01_descriptive_analysis.ipynb")
        print("   - 02_feature_engineering_tsne.ipynb")
        print("   - 03_gbdt_modeling.ipynb")
        print("   - 04_visualization_analysis.ipynb")
    else:
        print("⚠️  项目验证发现问题，请根据上述提示修复。")
        sys.exit(1)

if __name__ == "__main__":
    main()
