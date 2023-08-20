def calculate_ticket_price(age):
    if age < 18:
        return 0
    elif 18 <= age < 25:
        return 990
    else:
        return 1390

def main():
    num_tickets = int(input("Введите количество билетов: "))
    total_price = 0

    for _ in range(num_tickets):
        age = int(input("Введите возраст посетителя: "))
        ticket_price = calculate_ticket_price(age)
        total_price += ticket_price

    if num_tickets > 3:
        total_price *= 0.9  # Применяем 10% скидку при заказе более 3 билетов

    print(f"Сумма к оплате: {total_price:.2f} руб.")

if __name__ == "__main__":
    main()
