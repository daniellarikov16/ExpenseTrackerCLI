import argparse
from expenses import *
def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    add_parser = subparsers.add_parser('add',
                                       help='Добавить новые расходы')
    add_parser.add_argument('--description',
                            type=str, default='Пусто',
                            help='Введите описание расхода')
    add_parser.add_argument('--amount',
                            type=int, default=0,
                            help='Введите сумму расхода (default: 0)')

    update_parser = subparsers.add_parser('update',
                                          help='Обновить данные о расходах')
    update_parser.add_argument('--id',
                               type=int,
                               required=True,
                               help='Введите id записи')
    update_parser.add_argument('--field',
                               type=str, required=True,
                               help='Поле для изменения (description/amount)')
    update_parser.add_argument('--new_value',
                               required=True,
                               help='Введите значение для изменения')
    delete_paser = subparsers.add_parser('delete',
                                         help = 'Удалить расход')
    delete_paser.add_argument('id_delete',
                              type = int,
                              help = 'id записи')
    all_parser = subparsers.add_parser('show_info',
                                       help = 'Просмотр всех записей')
    amount_parser = subparsers.add_parser('all_amount',
                                          help = 'Просмотр суммы все трат')
    month_parser = subparsers.add_parser('month_expense',
                                         help = 'Вывод информации о тратах в месяце')
    month_parser.add_argument('month',
                              type = int,
                              help = 'Номер месяца (Например: Январь - 1, Февраль - 2...')
    args = parser.parse_args()
    if args.command == 'add':
        add_expense(args.description, args.amount)
    if args.command == 'update':
        update_expense(args.id,args.field,args.new_value)
    if args.command == 'delete':
        delete_expense(args.id_delete)
    if args.command == 'show_info':
        show_info()
    if args.command == 'all_amount':
        all_amount()
    if args.command == 'month_expense':
        month_expense(args.month)
    else:
        print('Введена неверная команда')
        parser.print_help()