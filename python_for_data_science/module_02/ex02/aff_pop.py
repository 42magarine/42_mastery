#!/usr/bin/env python

import matplotlib.pyplot as plt     # https://matplotlib.org
import pandas as pd                 # https://pandas.pydata.org
from matplotlib.ticker import FuncFormatter
from typing import Optional, Tuple, List
from load_csv import load


def parse_population_value(value: str) -> float:
    """
    Convert population string to a numeric float value.

    Args:
        value (str): Population value as string.

    Returns:
        float: Parsed numeric value.
    """
    value = value.strip()

    if value.endswith('M'):
        return float(value[:-1]) * 1_000_000
    elif value.endswith('k'):
        return float(value[:-1]) * 1_000
    else:
        return float(value)


def get_country_data(
    df: pd.DataFrame,
    country_name: str,
) -> Tuple[Optional[List[int]], Optional[List[float]]]:
    """
    Extract population data for a specific country between 1800 and 2050.

    Args:
        df (pd.DataFrame): DataFrame containing the population data.
        country_name: Name of the country to extract data for

    Returns:
        Tuple containing:
            - List[int]: Years from 1800 to 2050.
            - List[float]: Corresponding population values.
    """
    # Validate country exists in dataset
    if country_name not in df['country'].values:
        print(f"Country '{country_name}' not found in dataset.")
        return None, None

    # Select only year columns between 1800 and 2050
    year_columns = [col for col in df.columns
                    if col.isdigit() and 1800 <= int(col) <= 2050]

    # Single-step filtering: get specific country row and year columns
    country_data = df.loc[df['country'] == country_name, year_columns]

    if country_data.empty:
        print(f"No data found for country '{country_name}'")
        return None, None

    # Convert year columns to integers for x-axis
    years = [int(year) for year in year_columns]

    # Convert population strings to numeric values
    # country_data.iloc[0] gets the first (and only) row for this country
    country_row = country_data.iloc[0]
    values = [parse_population_value(country_row[val]) for val in year_columns]

    return years, values


def format_population_axis(ax: plt.Axes) -> None:
    """
    Format the y-axis to display population values in human-readable format.

    Args:
        ax: Matplotlib axes object to format
    """
    def format_population_ticks(value, pos):
        """Format population values for axis labels."""
        if value >= 1_000_000:
            return f'{value/1_000_000:.1f}M'
        elif value >= 1_000:
            return f'{value/1_000:.0f}k'
        else:
            return f'{value:.0f}'

    from matplotlib.ticker import FuncFormatter
    ax.yaxis.set_major_formatter(FuncFormatter(format_population_ticks))


def main() -> None:
    """
    Display population data for Germany and France (1800-2050).
    """
    df = load("population_total.csv")

    if df is None:
        print("Error: Could not load population data.")
        return

    germany_years, germany_values = get_country_data(df, "Germany")
    france_years, france_values = get_country_data(df, "France")

    if germany_years is None or france_years is None:
        print("Error: Could not extract data for one or both countries.")
        return

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot data
    ax.plot(germany_years, germany_values, color='blue', label='Germany')
    ax.plot(france_years, france_values, color='red', label='France')

    # Set labels and title
    ax.set_title("Population Projections")
    ax.set_xlabel("Year")
    ax.set_ylabel("Population")

    # Set axis ticks
    ax.set_xticks(range(1800, 2051, 40))
    ax.set_yticks(range(20_000_000, 80_000_001, 20_000_000))

    # Format Y-axis ticks
    ax.yaxis.set_major_formatter(
        FuncFormatter(lambda x, _: f'{x / 1_000_000:.0f}M')
    )

    # Add legend
    ax.legend()

    # Show plot
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
