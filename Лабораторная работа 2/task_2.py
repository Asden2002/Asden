salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.03  # Ежемесячный рост цен
months = 10  # Количество месяцев, которое нужно протянуть

needed_money = 0  # Необходимая подушка безопасности
current_spend = spend  # Текущие траты

for month in range(months):
    shortage = current_spend - salary

    if shortage > 0:
        needed_money += shortage

    current_spend += current_spend * increase

money_capital = round(needed_money)

print("Подушка безопасности, чтобы протянуть", months, "месяцев:", money_capital)