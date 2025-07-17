#!/usr/bin/env python

import matplotlib.pyplot as plt     # https://matplotlib.org
from load_csv import load


def main() -> None:
    """
    Display life expectancy data for a specific country.
    """
    df = load("life_expectancy_years.csv")

    if df is None:
        print("Failed to load the dataset.")
        return

    country_name = "Germany"

    # Check if the country exists in the dataset
    if country_name not in df['country'].values:
        print(f"Country '{country_name}' not found in dataset.")
        return

    # Filter data for the specific country
    country_data = df[df['country'] == country_name]

    # axis=0 -> row, axis=1 -> column
    country_data = country_data.drop('country', axis=1)

    years = country_data.columns.astype(int)
    # converts multidimensional arrays into 1D
    values = country_data.values.flatten()

    # Create the plot
    plt.figure(figsize=(10, 5))
    plt.plot(years, values, color='blue')

    # Add title and labels
    plt.title(f"{country_name} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")

    # Customize the plot
    plt.xticks(range(1800, 2051, 40))

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
