
# Olympic Athletes Analysis

## Overview

This project analyzes Olympic athletes' demographic and performance data, focusing on gender, age, height, and medal distribution across different countries and disciplines. The analysis leverages data visualizations to uncover trends and insights, making it easier to understand the dynamics of Olympic competitions.

## Table of Contents

- [Project Structure](#project-structure)
- [Data Sources](#data-sources)
- [Setup and Installation](#setup-and-installation)
- [Analysis Overview](#analysis-overview)
  - [Gender Distribution](#gender-distribution)
  - [Birth Month Analysis](#birth-month-analysis)
  - [Senior and Junior Athletes](#senior-and-junior-athletes)
  - [Country-Specific Analysis](#country-specific-analysis)
  - [Medal Analysis](#medal-analysis)
  - [Age Distribution](#age-distribution)
  - [Height Analysis](#height-analysis)
- [Helper Functions](#helper-functions)
- [Results and Insights](#results-and-insights)
- [Conclusion](#conclusion)
- [Note](#note)

## Project Structure

- `olympic_basic_analysis.ipynb`: The main Jupyter Notebook containing the analysis code.
- `helper.py`: A Python script providing utility functions and resources for the analysis.
- `csvs/`: Directory containing CSV files used in the analysis (e.g., athlete and NOC data).
- `images/medals/`: Directory containing images of medals used in visualizations.
- `configs/url_config.yaml`: Configuration file containing URLs for medal data.

## Data Sources

The analysis is based on the following datasets:
- **Athlete Data**: Contains information on Olympic athletes, including gender, date of birth, height, and nationality.
- **NOC Data**: Provides mappings between National Olympic Committee (NOC) codes and their respective country names.
- **Medal Data**: Retrieved from external sources specified in the configuration file, detailing the distribution of medals across countries.

## Setup and Installation

To run this analysis, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/olympic-analysis.git
   cd olympic-analysis
   ```

2. **Install required packages**:
   Ensure you have Python 3.x installed, then install the required Python libraries using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Jupyter Notebook**:
   Start Jupyter Notebook and open `olympic_basic_analysis.ipynb` to execute the analysis.
   ```bash
   jupyter notebook
   ```

## Analysis Overview

### Gender Distribution

- **Objective**: To analyze the distribution of male and female athletes.
- **Methodology**: The gender distribution is visualized using a pie chart to provide a quick overview of gender representation among athletes.
- **Results**: This section reveals the proportion of male to female athletes, highlighting any significant gender disparities.

### Birth Month Analysis

- **Objective**: To determine if there's any trend in the birth months of athletes.
- **Methodology**: The number of athletes born in each month is plotted using a bar chart.
- **Results**: The analysis shows the distribution of athletes' birth months, potentially indicating whether certain months are more common among top athletes.

### Senior and Junior Athletes

- **Objective**: To identify the oldest and youngest athletes in the dataset.
- **Methodology**: The analysis finds the athletes with the earliest and latest dates of birth, providing insights into the age range of Olympic competitors.
- **Results**: The section lists the oldest and youngest athletes, offering a look at the age diversity within the games.

### Country-Specific Analysis

- **Objective**: To focus on athletes from specific countries, with a spotlight on Thai athletes.
- **Methodology**: Custom functions are used to filter athletes by country and discipline, displaying relevant data for detailed exploration.
- **Results**: The analysis offers insights into the performance and demographics of athletes from selected countries.

### Medal Analysis

- **Objective**: To analyze the distribution of medals across different countries and investigate any correlations between age and medal wins.
- **Methodology**: Data is pulled from external sources to count medals by country. Age and medal correlations are also explored.
- **Results**: This section reveals which countries dominate in medal wins and whether younger or older athletes are more likely to win medals.

### Age Distribution

- **Objective**: To examine the age distribution of athletes across the dataset and within specific disciplines.
- **Methodology**: Histograms and box plots are used to visualize the age distribution, highlighting the range and average ages.
- **Results**: The analysis provides a detailed look at how athletes' ages vary across different sports and the Olympic Games overall.

### Height Analysis

- **Objective**: To investigate the distribution of athletes' heights.
- **Methodology**: The data is filtered to exclude missing or zero values, and then visualized to show the height distribution among athletes.
- **Results**: This section explores the typical height ranges in the athlete population, possibly offering insights into physical trends in different sports.

## Helper Functions

The `helper.py` script includes several utility functions that support the analysis, namely:

- **`load_medal_images()`**: Loads and resizes images of medals for use in visualizations.
- **`fetch_json(api_url, return_json=True)`**: Fetches JSON data from an API and returns it for further processing.

These functions are integral to the smooth operation of the notebook, providing essential data and resources.

## Results and Insights

This project reveals several key insights into the demographics and performance of Olympic athletes:

- **Gender Representation**: The data shows any gender imbalances in Olympic participation.
- **Age and Performance**: Insights into how age impacts athletic success, particularly in relation to winning medals.
- **Country Dominance**: Identifies which countries excel in specific sports and overall medal tallies.

## Conclusion

The Olympic Athletes Analysis project provides a comprehensive look at various aspects of athlete demographics and performance. Through detailed visualizations and statistical analysis, we gain a deeper understanding of the factors that contribute to success in the Olympic Games.

## Note 

The notebook will run to completion only if the API URLS are specified in `configs/url_config.yaml`. Please contact me if you want to see how the calls are made. 