# 房价预测数据分析项目

## 项目概述

本项目是一个基于Python的房价预测数据分析项目，使用机器学习方法对房屋销售价格进行预测。项目包含完整的数据科学工作流程，从探索性数据分析到模型构建和评估。

## 项目特点

- 📊 **全面的探索性数据分析**：深入分析房屋特征与价格的关系
- 🔧 **完善的特征工程**：处理缺失值、特征选择和特征变换
- 🤖 **多种机器学习模型**：比较不同算法的性能表现
- 📈 **可视化分析**：丰富的图表展示数据洞察
- 📝 **详细的文档**：完整的分析报告和代码说明

## 数据集信息

- **训练集**：1460个样本，81个特征
- **测试集**：1459个样本，80个特征
- **目标变量**：SalePrice（房屋销售价格）
- **特征类型**：数值型和类别型特征的混合

## 项目结构

```
├── README.md                    # 项目说明文件
├── requirements.txt            # Python依赖包列表
├── verify_project.py           # 项目验证脚本
├── LICENSE                     # MIT许可证
├── .gitignore                  # Git忽略文件配置
├── notebooks/                  # Jupyter分析笔记本
│   ├── 01_descriptive_analysis.ipynb      # 描述性数据分析
│   ├── 02_feature_engineering_tsne.ipynb  # 特征工程与t-SNE降维
│   ├── 03_gbdt_modeling.ipynb             # 机器学习建模（GBDT、XGBoost、Stacking）
│   └── 04_visualization_analysis.ipynb    # 模型评估与可视化分析
├── data/                       # 数据文件目录
│   ├── train.csv              # 训练数据集
│   ├── test.csv               # 测试数据集
│   └── processed_data.pkl     # 预处理后的数据（自动生成）
├── models/                     # 模型文件目录
│   ├── best_gbdt_model.pkl    # 最佳GBDT模型
│   └── model_objects.pkl      # 所有模型对象（自动生成）
├── results/                    # 结果输出目录
│   └── submission.csv         # 预测结果文件
├── images/                     # 可视化图表目录
│   ├── *.png                  # 各种分析图表（自动生成）
├── docs/                       # 项目文档目录
│   ├── project_report.md      # 完整分析报告
│   └── *.docx, *.pdf          # 其他项目文档
└── .github/workflows/          # GitHub Actions配置
    └── ci.yml                 # 持续集成配置

## 环境要求

- Python 3.7+
- Jupyter Notebook
- 主要依赖包：
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - xgboost
  - plotly

## 快速开始

1. **克隆项目**
   ```bash
   git clone <your-repository-url>
   cd house-price-prediction
   ```

2. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

3. **验证项目**
   ```bash
   python verify_project.py
   ```

4. **运行分析**
   ```bash
   jupyter notebook
   ```
   
   **按以下顺序依次运行笔记本：**
   
   1. **`01_descriptive_analysis.ipynb`** - 数据探索与描述性分析
      - 数据质量检查
      - 缺失值分析
      - 特征分布可视化
      - 相关性分析
   
   2. **`02_feature_engineering_tsne.ipynb`** - 特征工程与降维
      - 数据预处理（对数变换、独热编码、标准化）
      - t-SNE降维分析
      - 生成 `processed_data.pkl`
   
   3. **`03_gbdt_modeling.ipynb`** - 机器学习建模
      - GBDT超参数优化
      - RFE特征选择
      - XGBoost模型训练
      - Stacking集成学习
      - 生成 `best_gbdt_model.pkl` 和 `model_objects.pkl`
   
   4. **`04_visualization_analysis.ipynb`** - 模型评估与可视化
      - 模型性能对比
      - 特征重要性分析
      - 预测结果可视化
      - 生成所有分析图表

   **注意：** 每个notebook都会为下一个notebook生成必要的数据文件，请按顺序执行。

## 主要分析内容

### 1. 数据探索与描述性分析 (`01_descriptive_analysis.ipynb`)
- 数据质量评估与缺失值分析
- 数值特征与类别特征分布可视化
- 特征间相关性分析
- 目标变量与关键特征的关系探索

### 2. 特征工程与降维分析 (`02_feature_engineering_tsne.ipynb`)
- 目标变量对数变换，改善分布偏态
- 高偏度数值特征对数变换
- 类别特征独热编码处理
- 特征标准化与缺失值填充
- t-SNE降维可视化分析

### 3. 机器学习建模 (`03_gbdt_modeling.ipynb`)
- GBDT超参数随机搜索优化
- RFE递归特征消除与特征选择
- XGBoost梯度提升模型训练
- Stacking集成学习模型构建
- 多模型性能对比与评估

### 4. 模型评估与可视化分析 (`04_visualization_analysis.ipynb`)
- 真实值与预测值对比散点图
- 各模型MSE性能对比柱状图
- 特征重要性排序与累计贡献曲线
- 超参数分布与最优参数雷达图
- 交叉验证结果可视化分析

## 主要发现

- **核心特征**：整体质量评级(OverallQual)、地上居住面积(GrLivArea)、车库容量(GarageCars)等对房价影响最大
- **模型性能**：Stacking集成模型表现最佳，结合了GBDT和XGBoost的优势
- **特征工程**：对数变换显著改善了目标变量和高偏度特征的分布
- **降维分析**：t-SNE揭示了数据的内在聚类结构，不同建筑类型和价格区间呈现明显分离

## 技术亮点

- **模块化设计**：将复杂分析拆分为4个独立notebook，便于理解和维护
- **数据流衔接**：通过pkl文件实现notebook间的数据传递，确保分析连贯性
- **多模型比较**：实现了GBDT、XGBoost、RFE-GBDT、Stacking等多种模型的训练与对比
- **丰富可视化**：包含20+种专业图表，全面展示数据特征和模型性能

## 可视化展示

项目包含丰富的数据可视化，包括：
- 📊 特征分布图
- 🔗 相关性热力图
- 📈 模型性能对比图
- 🎯 特征重要性排序
- 📉 残差分析图

## 贡献指南

欢迎提交问题和改进建议！请通过以下方式参与：

1. Fork 本项目
2. 创建特性分支 
3. 提交更改
4. 推送到分支
5. 打开 Pull Request

## 许可证

本项目仅用于学习和研究目的。

## 联系方式

如有问题，请通过以下方式联系：
- 📧 Email: [3450886609@qq.com]
- 🐙 GitHub: [https://github.com/Mickey0Lmq]

---

⭐ 如果这个项目对您有帮助，请给它一个星标！
