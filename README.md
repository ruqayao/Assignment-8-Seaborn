# Assignment-8-Seaborn
# Purpose
This project demonstrates the use of Seaborn to create meaningful data visualizations using two datasets. The goal is to explore relationships between diet, exercise, and heart rate, and to practice different Seaborn plot types.
# Datasets Used
Exercise_Data.csv

This dataset contains heart rate measurements collected during different types of exercise.

Columns:

- id: Unique identifier for each participant
- 1 min: Heart rate after 1 minute of activity
- 15 min: Heart rate after 15 minutes of activity
- 30 min: Heart rate after 30 minutes of activity
- diet: Type of diet (low fat or no fat)
- kind: Type of activity (rest, walking, running)

Seaborn Planets Dataset

This is a built-in dataset provided by Seaborn that contains information about discovered exoplanets.

Key columns used:

- distance: Distance of the planet from Earth
- orbital_period: Time taken for one orbit around its star
- mass: Mass of the planet
- year: Year of discovery
- method: Method used to discover the planet
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

2. PlanetsVisualizer

Attribute:
- data: stores planets dataset

Methods:
- relational_plots(): shows relationships between variables
- distribution_plots(): shows distributions of values
- categorical_plots(): compares categories
# Implementation
The assignment is implemented using two main Python classes:

ExerciseVisualizer

- Loads the Exercise_Data.csv file using pandas.
- Cleans and reshapes the data for visualization.

Generates:
- A heatmap of heart rate values over time
- A categorical bar plot comparing pulse by exercise type and diet

PlanetsVisualizer
- Loads the built-in seaborn planets dataset.
- Handles missing values by dropping incomplete rows in key columns.

Generates three types of visualizations:
- Relational plots (scatter and line plots)
- Distribution plots (histogram and KDE)
- Categorical plots (boxplot and violin plot)
# Limitations
- Exercise dataset is small (30 samples), limiting generalization.
- Diet categories are simplified (only two types).
- Planets dataset contains missing values that may affect plots.
- Visualizations are basic and do not include advanced customization.
