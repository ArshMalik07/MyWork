import matplotlib.pyplot as plt

def create_line_graph(sales_data):
    years = list(sales_data.keys())
    cars_sold = list(sales_data.values())

    
    line_colors = ['green' if cars_sold[i] > cars_sold[i - 1] else 'red' for i in range(1, len(cars_sold))]

    plt.plot(years[1:], cars_sold[1:], marker='o', color='blue', linestyle='solid', linewidth=5)
    for x, y, color in zip(years[1:], cars_sold[1:], line_colors):
        plt.axhline(y, xmin=(x - 1) / (max(years) - min(years)), xmax=x / (max(years) - min(years)), color=color, linestyle='--')

    plt.xlabel('Year')
    plt.ylabel('Number of Cars Sold')
    plt.title('TATA Car Sales by Year')
    plt.xticks(years)
    plt.grid(axis='y', linestyle='solid', alpha=1.0)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    
    tata_car_sales = {
        2018: 3000,
        2019: 4500,
        2020: 4000,
        2021: 7000,
        2022: 9000,
        2023: 10500
    }

    create_line_graph(tata_car_sales)





