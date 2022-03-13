import sys


class Category:

    def __init__(self, category_name):
        self.category_name = category_name
        self.products_list = []


class Product:

    def __init__(self, product_name, product_price):
        self.product_name = product_name
        self.product_price = product_price


class Order:

    def __init__(self):
        self.orders_list = []


class User:

    def __init__(self, name):
        self.user_name = name
        self.order = Order()

    def count_bill(self):
        user_sum = 0
        if len(self.order.orders_list) != 0:
            for product in self.order.orders_list:
                user_sum += product.product_price
            return user_sum
        else:
            return user_sum

    def make_order(self, categories_list):
        i = 1
        print('Выберите категорию :')
        for category in categories_list:
            print(str(i) + ').' + str(category.category_name))
            i += 1
        choice = int(input('Ваш выбор: '))
        i = 1
        print('Выберите товар :')
        for product in categories_list[choice - 1].products_list:
            print(str(i) + ').' + str(product.product_name) + ', цена:' + str(product.product_price))
            i += 1
        choice_2 = int(input('Ваш выбор: '))
        self.order.orders_list.append(categories_list[choice - 1].products_list[choice_2 - 1])

    def remove_order(self):
        print('Что Вы хотите удалить?')
        i = 1
        for order_1 in self.order.orders_list:
            print(str(i) + ').' + str(order_1.product_name) + ', цена:' + str(order_1.product_price))
            i += 1
        choice = int(input('Ваш выбор: '))
        del self.order.orders_list[choice - 1]


class Admin(User):

    def __init__(self, name):
        super().__init__(name)
        self.categories_list = []

    @staticmethod
    def add_category(categories_list):
        category_name = str(input("Введите наименование новой категории: "))
        category = Category(category_name)
        categories_list.append(category)

    @staticmethod
    def add_product(categories_list):
        i = 1
        print('\nВыберите категорию, в которую требуется добавить товар: ')
        for category in categories_list:
            print(str(i) + ').' + str(category.category_name))
            i += 1
        choice = int(input('Ваш выбор: '))
        product_name = str(input('Введите наименование товара: '))
        product_price = int(input('Введите цену товара: '))
        product = Product(product_name, product_price)
        categories_list[choice - 1].products_list.append(product)

    @staticmethod
    def remove_product(categories_list, users_list):
        i = 1
        print('\nВыберите категорию, из которой требуется удалить товар: ')
        for category in categories_list:
            print(str(i) + ').' + str(category.category_name))
            i += 1
        choice = int(input('Ваш выбор: '))
        print('Какой товар В хотите удалить?')
        i = 1
        for product in categories_list[choice - 1].products_list:
            print(str(i) + ').' + str(product.product_name) + ', цена:' + str(product.product_price))
        choice_2 = int(input('Ваш выбор: '))
        for user in users_list:
            if len(user.order.orders_list) != 0:
                user.order.orders_list = [product for product in user.order.orders_list if
                                          product.product_name != categories_list[choice - 1].products_list[
                                              choice - 2].product_name]
        del categories_list[choice - 1].products_list[choice - 2]


class Interface:

    def __init__(self):
        self.users_list = []
        self.admins_list = []
        self.categories_list = []
        self.current_user = ''
        self.user_flag = 0

    def create_user(self):
        print('Какая роль?')
        print('1). Администратор.')
        print('2). Пользователь.')
        choice = int(input('Ваш выбор: '))
        if choice == 1:
            self.user_flag = 1
            name = input('\nВведите имя администратора: ')
            print()
            admin = Admin('Администратор ' + name)
            self.current_user = admin
            self.admins_list.append(admin)
        elif choice == 2:
            self.user_flag = 2
            name = input('\nВведите имя пользователя: ')
            print()
            user = User('Пользователь ' + name)
            self.current_user = user
            self.users_list.append(user)

    def choose_user(self):
        print('Какая роль?')
        print('1). Администратор.')
        print('2). Пользователь.')
        choice = int(input('Ваш выбор: '))
        if choice == 1:
            self.user_flag = 1
            i = 1
            print('\nВыберите администратора: ')
            for admin in self.admins_list:
                print(str(i) + ').' + str(admin.user_name))
                i += 1
            choice = int(input('Ваш выбор: '))
            self.current_user = self.admins_list[choice - 1]
        elif choice == 2:
            self.user_flag = 2
            i = 1
            print('\nВыберите пользователя: ')
            for user in self.users_list:
                print(str(i) + ').' + str(user.user_name))
                i += 1
            choice = int(input('Ваш выбор: '))
            self.current_user = self.users_list[choice - 1]

    def show_menu(self):
        flag = True
        while flag:
            if self.user_flag == 1:
                i = 1
                print('Добро пожаловать, ' + str(self.current_user.user_name) + '\nЧто Вы хотите сделать?\n')
                print(str(i) + '). Создать категорию.')
                i += 1
                print(str(i) + '). Добавить товар.')
                i += 1
                print(str(i) + '). Удалить товар.')
                i += 1
                print(str(i) + '). Сменить пользователя.')
                i += 1
                print(str(i) + '). Добавить пользователя.')
                i += 1
                print(str(i) + '). Выход.\n')
                choice = input('Ваш выбор: ')
                if int(choice) == 1:
                    self.current_user.add_category(self.categories_list)
                elif int(choice) == 2:
                    self.current_user.add_product(self.categories_list)
                elif int(choice) == 3:
                    self.current_user.remove_product(self.categories_list, self.users_list)
                elif int(choice) == 4:
                    self.choose_user()
                elif int(choice) == 5:
                    self.create_user()
                elif int(choice) == 6:
                    flag = False
                    sys.exit()
            elif self.user_flag == 2:
                user_sum = self.current_user.count_bill()
                print('Добро пожаловать, ' + str(self.current_user.user_name))
                print('Стоимость Ваших покупок: ' + str(user_sum))
                if len(self.current_user.order.orders_list) != 0:
                    print('Ваши товары: ')
                    i = 1
                    for order in self.current_user.order.orders_list:
                        print(str(i) + ').' + str(order.product_name) + ', цена:' + str(order.product_price))
                        i += 1
                print('Что Вы хотите сделать?\n')
                i = 1
                print(str(i) + '). Добавить товар в корзину.')
                i += 1
                print(str(i) + '). Удалить товар из корзины.')
                i += 1
                print(str(i) + '). Сменить пользователя.')
                i += 1
                print(str(i) + '). Добавить пользователя.')
                i += 1
                print(str(i) + '). Выход.\n')
                choice = input('Ваш выбор: ')
                if int(choice) == 1:
                    self.current_user.make_order(self.categories_list)
                elif int(choice) == 2:
                    self.current_user.remove_order()
                elif int(choice) == 3:
                    self.choose_user()
                elif int(choice) == 4:
                    self.create_user()
                elif int(choice) == 5:
                    flag = False
                    sys.exit()

    def start_menu(self):
        print('Добавьте пользователей.')
        self.create_user()
        self.show_menu()


interface = Interface()
interface.start_menu()
