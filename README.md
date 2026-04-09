# Assignment-8-Seaborn
# Purpose
This project demonstrates the use of Seaborn to create meaningful data visualizations using two datasets. The goal is to explore relationships between diet, exercise, and heart rate, and to practice different Seaborn plot types.
# Datasets Used
1. Exercise_Data.csv (heart rate data)

2. Seaborn built-in planets dataset
# Input File Requirements
Exercise_Data.csv

Must include columns:
- id
- 1 min
- 15 min
- 30 min
- diet
- kind

Planets Dataset

Loaded automatically using seaborn
# Class Design
1. ExerciseVisualizer

Attribute:
- data: stores the exercise dataset

Methods:
- create_heatmap(): shows pulse intensity over time
- create_categorical_plot(): compares pulse by diet and exercise type

PlanetsVisualizer

Attribute:
- data: stores planets dataset

Methods:
- relational_plots(): shows relationships between variables
- distribution_plots(): shows distributions of values
- categorical_plots(): compares categories
# Implementation
# Limitations
- Exercise dataset is small (30 samples), limiting generalization.
- Diet categories are simplified (only two types).
- Planets dataset contains missing values that may affect plots.
- Visualizations are basic and do not include advanced customization.
