
# Olympic Athletes Analysis and Medal Table

## Overview

This project encompasses two main components: an analysis of Olympic athletes' demographic and performance data, and the fetching of current medal standings. The data is processed and presented in an HTML table, making it easily accessible for users. The project includes scripts for periodic and instant updates of the medal table, which can be viewed in `index.html`.

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
- [Medal Table Generation](#medal-table-generation)
  - [Athlete Data Gathering](#athlete-data-gathering)
  - [Medal Table Fetching](#medal-table-fetching)
  - [HTML Medal Table](#html-medal-table)
- [Running the Scripts](#running-the-scripts)
  - [Instant Execution](#instant-execution)
  - [Periodic Execution](#periodic-execution)
- [Helper Functions](#helper-functions)
- [Results and Insights](#results-and-insights)
- [Conclusion](#conclusion)
- [License](#license)

## Project Structure

- `olympic_basic_analysis.ipynb`: Jupyter Notebook containing analysis code for various aspects of Olympic athletes.
- `Fetching_Olmpics_Athletes.ipynb`: Jupyter Notebook that gathers information about Olympic athletes and fetches the medal table data.
- `helper.py`: Python script providing utility functions and resources for the analysis.
- `make_html.py`: Python script that generates an HTML file (`medal_table.html`) with the latest medal standings. This script can be run either instantly or periodically.
- `index.html`: The output HTML file that displays the latest medal standings in a user-friendly format.
- `csvs/`: Directory containing CSV files used in the analysis (e.g., athlete and NOC data).
- `images/medals/`: Directory containing images of medals used in visualizations.
- `configs/url_config.yaml`: Configuration file containing URLs for medal data.

## Data Sources

The analysis is based on the following datasets:
- **Athlete Data**: Contains information on Olympic athletes, including gender, date of birth, height, and nationality.
- **NOC Data**: Provides mappings between National Olympic Committee (NOC) codes and their respective country names.
- **Medal Standings**: The current medal table, which includes the number of gold, silver, and bronze medals won by each country.

## Setup and Installation

To run this project, follow these steps:

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

3. **Run the Jupyter Notebooks**:
   Open the notebooks to execute the data gathering and processing steps:
   ```
   jupyter notebook 
   ```

4. **Run the HTML generation script**:
   Execute the `make_html.py` script to generate the `index.html` file.

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

## Medal Table Generation

### Athlete Data Gathering

- **Objective**: To collect detailed information about Olympic athletes, including their biographical details and performance statistics.
- **Methodology**: The notebook fetches athlete data from various sources, processes it, and prepares it for further analysis or display.

### Medal Table Fetching

- **Objective**: To retrieve the latest medal standings from a reliable source.
- **Methodology**: The notebook or script fetches the medal table data, which is then processed and formatted for display in an HTML file.

### HTML Medal Table

- **Objective**: To present the medal standings in an easily accessible and readable format.
- **Output**: The `medal_table.html` file displays the latest medal standings, including the number of gold, silver, and bronze medals won by each country.

## Running the Scripts

### Instant Execution

The `make_html.py` script can be run manually to generate the medal table instantly. This is useful for getting the latest standings on demand.

- **Command**:
  ```bash
  python make_html.py instant
  ```

### Periodic Execution

The `make_html.py` script can also be scheduled to run periodically to ensure the medal table is always up to date. By default, the script will run every 30 mins (Since we are no longer in the Olympics Period, this is not needed)

- **Example**:
  To run the script every 20 minutes, simply run the script normally (It does not use cron, but python's library):
  `python make_html.py`

## Helper Functions

The `helper.py` script includes several utility functions that support the analysis:

- **`load_medal_images()`**: Loads and resizes images of medals for use in visualizations.
- **`fetch_json(api_url, return_json=True)`**: Fetches JSON data from an API and returns it for further processing.

These functions are integral to the smooth operation of the notebook, providing essential data and resources.

## Results and Insights

This project reveals several key insights into the demographics and performance of Olympic athletes:

- **Gender Representation**: The data shows any gender imbalances in Olympic participation.
- **Age and Performance**: Insights into how age impacts athletic success, particularly in relation to winning medals.
- **Country Dominance**: Identifies which countries excel in specific sports and overall medal tallies.

## Conclusion

The Olympic Athletes Analysis project provides a comprehensive look at various aspects of athlete demographics and performance. Through detailed visualizations and statistical analysis, we gain a deeper understanding of the factors that contribute to success in the Olympic Games. Additionally, the medal table generation component ensures that users have access to the most current standings in a convenient HTML format.