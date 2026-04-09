#Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Class for Exercise Data Visualization
class ExerciseVisualizer:

    def __init__(self, file_path):
        #Load dataset
        self.data = pd.read_csv(file_path)

    def create_heatmap(self):
        #Prepare data for heatmap (only pulse columns)
        pulse_data = self.data[['1 min', '15 min', '30 min']]

        #Create heatmap
        sns.heatmap(pulse_data, cmap='coolwarm')
        plt.title('Heatmap of Pulse Rates Over Time')
        plt.xlabel('Time Intervals')
        plt.ylabel('Participants')
        plt.show()

    def create_categorical_plot(self):
        #Convert data to long format
        melted = pd.melt(self.data,
                         id_vars=['diet', 'kind'],
                         value_vars=['1 min', '15 min', '30 min'],
                         var_name='Time',
                         value_name='Pulse')

        #Create categorical plot
        sns.catplot(x='kind', y='Pulse', hue='diet', col='Time',
                    data=melted, kind='bar')
        plt.show()

#Class for Planets Dataset Visualization
class PlanetsVisualizer:

    def __init__(self):
        #Load seaborn dataset
        self.data = sns.load_dataset('planets')

        #Handle missing values
        #Drop rows where important columns are missing
        self.data = self.data.dropna(subset=['distance', 'orbital_period', 'mass', 'year', 'method'])

        #Reset index after dropping rows
        self.data = self.data.reset_index(drop=True)

    #Relational plots
    def relational_plots(self):
        sns.scatterplot(x='distance', y='orbital_period', data=self.data)
        plt.title('Distance vs Orbital Period')
        plt.show()

        sns.lineplot(x='year', y='distance', data=self.data)
        plt.title('Distance Over Years')
        plt.show()

    #Distribution plots
    def distribution_plots(self):
        sns.histplot(self.data['orbital_period'], bins=20)
        plt.title('Distribution of Orbital Period')
        plt.show()

        sns.kdeplot(self.data['mass'], fill=True)
        plt.title('Density of Planet Mass')
        plt.show()

    #Categorical plots
    def categorical_plots(self):
        sns.boxplot(x='method', y='distance', data=self.data)
        plt.xticks(rotation=45)
        plt.title('Distance by Discovery Method')
        plt.show()

        sns.violinplot(x='method', y='orbital_period', data=self.data)
        plt.xticks(rotation=45)
        plt.title('Orbital Period by Method')
        plt.show()

#Main execution
if __name__ == '__main__':
    exercise = ExerciseVisualizer('Exercise_Data.csv')
    exercise.create_heatmap()
    exercise.create_categorical_plot()

    planets = PlanetsVisualizer()
    planets.relational_plots()
    planets.distribution_plots()
    planets.categorical_plots()

#Conclusions from the data:
#From the exercise data, we can observe that heart rate increases as exercise intensity increases (rest < walking < running). 
#Resting has the lowest heart rate, walking is higher, and running makes the heart beat the fastest, especially after 15 and 30 minutes.
#While diet (low fat vs no fat) shows some small differences, the type of exercise has a much bigger impact on heart rate.
#This shows that how active an individual is matters more than diet when it comes to how fast the heart beats during activity.

#Best visualizations:
#Among all the visualizations, the line plot and KDE plot best demonstrate notable patterns in the data. 
#The line plot effectively shows trends in how planetary distances or discoveries change over time, 
#making it easier to observe patterns or shifts across years. 
#The KDE plot provides a smooth representation of the distribution of planet masses, 
#clearly illustrating where values are most concentrated and revealing the overall shape of the data.