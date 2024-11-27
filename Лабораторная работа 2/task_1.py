money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

months = 0
current_money = money_capital
current_spend = spend
while True:
    current_money += salary

    if current_money < current_spend:
        break

    current_money -= current_spend
    months += 1

    current_spend += current_spend * increase

print("Количество месяцев, которое можно протянуть без долгов:", months)