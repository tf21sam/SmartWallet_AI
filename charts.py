import matplotlib.pyplot as plt
import seaborn as sns
import os

def generate_spending_chart(df):
    os.makedirs('static', exist_ok=True)
    category_totals = df.groupby('category')['amount'].sum()
    plt.figure(figsize=(8,5))
    sns.set_theme(style="whitegrid")
    sns.barplot(x=category_totals.index, y=category_totals.values, palette="mako")
    plt.title('Spending by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Spending')
    plt.xticks(rotation=30)
    chart_path = 'static/spending_chart.png'
    plt.tight_layout()
    plt.savefig(chart_path)
    plt.close()
    return chart_path
