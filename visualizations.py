import matplotlib.pyplot as plt

def plot_sales_trends(df):
    """Plots sales trends over time."""
    df_grouped = df.groupby("Date")["Sales"].sum()

    plt.figure(figsize=(10, 5))
    plt.plot(df_grouped.index, df_grouped.values, marker="o", linestyle="-", color="b")
    plt.xlabel("Date")
    plt.ylabel("Total Sales")
    plt.title("Sales Trends Over Time")
    plt.grid(True)
    
    return plt

def plot_category_distribution(df):
    """Plots category-wise distribution of sales."""
    plt.figure(figsize=(8, 6))
    df.groupby("Category")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%", cmap="Set3")
    plt.title("Sales Distribution by Category")
    return plt

def plot_top_performers(df):
    """Plots top 5 performing products based on sales."""
    top_products = df.groupby("Product")["Sales"].sum().nlargest(5)

    plt.figure(figsize=(8, 6))
    top_products.plot(kind="bar", color="green")
    plt.xlabel("Product")
    plt.ylabel("Total Sales")
    plt.title("Top 5 Best-Selling Products")
    
    return plt
