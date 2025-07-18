#!/usr/bin/env python

import matplotlib.pyplot as plt     # https://matplotlib.org
import pandas as pd                 # https://pandas.pydata.org/
from load_csv import load


def main():
    """
    Main function to create a scatter plot showing the relationship between
    life expectancy and GDP per capita for the year 1900.
    """
    # Load the datasets
    gdp_df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_df = load("life_expectancy_years.csv")

    # Check if both datasets were loaded successfully
    if gdp_df is None or life_df is None:
        print("Error: Could not load one or both datasets.")
        return

    # Extract data for the year 1900
    year = "1900"

    # Check if the year column exists in both datasets
    if year not in gdp_df.columns or year not in life_df.columns:
        print(f"Error: Year {year} not found in one or both datasets.")
        return

    # Create a merged dataset for 1900
    # Merge on country name
    merged_df = pd.merge(
        gdp_df[["country", year]].rename(columns={year: "gdp_per_capita"}),
        life_df[["country", year]].rename(columns={year: "life_expectancy"}),
        on="country",
        how="inner"
    )

    # Remove rows with missing data
    merged_df = merged_df.dropna()

    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.scatter(merged_df["gdp_per_capita"], merged_df["life_expectancy"],
                color='blue', edgecolors='black')

    # Add title and labels
    plt.title(f"{year}")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    # Show plot
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
