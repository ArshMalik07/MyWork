import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def create_line_graph(sales_data):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(list(sales_data.items()), columns=['Year', 'Cars_Sold'])

    # Convert 'Year' to NumPy array for plotting
    years = df['Year'].to_numpy()
    cars_sold = df['Cars_Sold'].to_numpy()

    # Compute line colors based on sales increase or decrease
    line_colors = np.where(np.diff(cars_sold) > 0, 'green', 'red')

    # Plot the sales data
    plt.plot(years, cars_sold, marker='o', color='blue', linestyle='solid', linewidth=2)
    
    # Add colored horizontal lines to indicate increase/decrease
    for x, y, color in zip(years[1:], cars_sold[1:], line_colors):
        plt.axhline(y, xmin=(x - 1) / (years[-1] - years[0]), xmax=x / (years[-1] - years[0]), color=color, linestyle='--')

    # Set labels and title
    plt.xlabel('Year')
    plt.ylabel('Number of Cars Sold')
    plt.title('TATA Car Sales by Year')
    plt.xticks(years)
    plt.grid(axis='y', linestyle='solid', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Define sales data
    tata_car_sales = {
        2018: 3000,
        2019: 4500,
        2020: 4000,
        2021: 7000,
        2022: 9000,
        2023: 10500
    }

    create_line_graph(tata_car_sales)
