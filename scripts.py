import pandas as pd
from datetime import datetime, timedelta

# ====== Задача 1: Анализ данных о заказах ======
def analyze_orders(n_years):
    # Загрузка данных
    orders = pd.read_csv('data/orders.csv')
    customers = pd.read_csv('data/customers.csv')

    # Фильтрация заказов за последние n лет
    current_date = datetime.now()
    n_years_ago = current_date - timedelta(days=n_years * 365)
    orders['Order Date'] = pd.to_datetime(orders['Order Date'])
    recent_orders = orders[orders['Order Date'] >= n_years_ago]

    # 1. Количество заказов, отправленных первым классом
    first_class_orders = recent_orders[recent_orders['Ship Mode'] == 'First Class']
    print(f"Количество заказов, отправленных первым классом за последние {n_years} лет: {first_class_orders.shape[0]}")

    # 2. Количество клиентов из Калифорнии
    california_customers = customers[customers['State'] == 'California']
    print(f"Количество клиентов из Калифорнии: {california_customers.shape[0]}")

    # 3. Количество заказов клиентов из Калифорнии
    california_customer_ids = california_customers['Customer ID']
    california_orders = recent_orders[recent_orders['Customer ID'].isin(california_customer_ids)]
    print(f"Количество заказов клиентов из Калифорнии за последние {n_years} лет: {california_orders.shape[0]}")

    # 4. Сводная таблица средних чеков по штатам
    average_sales_by_state = recent_orders.groupby('State')['Sales'].mean().reset_index()
    print("Сводная таблица средних чеков по штатам:")
    print(average_sales_by_state)

# ====== Основной блок выполнения ======
if __name__ == '__main__':
    n_years = 11  # Количество лет для анализа
    print("=== Анализ данных заказов и клиентов ===")
    analyze_orders(n_years)
