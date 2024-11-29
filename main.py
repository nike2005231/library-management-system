import psycopg2 as pg2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from config.cfg import host, user, password, db_name
from ui.py.books import Ui_Book
from ui.py.extradition import Ui_Extradition
from ui.py.reader import Ui_Reader
from ui.py.statistic_window import Ui_Statisctic
from ui.py.record_book import Ui_RecordBook
from ui.py.record_reader import Ui_RecordReader
from ui.py.record_extradition import Ui_RecordExtradition
from ui.py.menu import Ui_Menu
from ui.py.window_log import Ui_window_logs
from ui.py.form_book import Ui_Form
from ui.py.history_window import Ui_History
from ui.py.form_history import Ui_FormHistory
from datetime import datetime

class FormHistory(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.history_form = Ui_FormHistory()
        self.history_form.setupUi(self)

    def text_label(self, text_form):
        self.history_form.label.setText(text_form)
    
    def set_text_color_red(self):
        self.history_form.label.setStyleSheet("color: red;")

#Класс формы для встраивания в скролл книги
class FormBook(QtWidgets.QWidget):
    def __init__(self, books_window):
        super().__init__()
        self.window_form = Ui_Form()
        self.window_form.setupUi(self)
        self.window_form.delete_button.clicked.connect(self.handle_button_delete)
        self.data_base = DataBase()
        self.books_window = books_window

    def handle_button_delete(self):
        book_id = self.window_form.label.text().split(",")[0]
        param = (book_id, )
        query_delete_history = f"DELETE FROM history WHERE fk_book = %s"
        self.data_base.execute_query_add(query=query_delete_history, params=param)
        query = f"delete from books where id_book = %s"
        self.data_base.execute_query_add(query=query, params=param)
        self.books_window.update_record_book()

    def text_label(self, text_form):
        self.window_form.label.setText(text_form)

#Класс формы для встраивания в скролл читателя
class FormReader(QtWidgets.QWidget):
    def __init__(self, reader_window):
        super().__init__()
        self.window_form = Ui_Form()
        self.window_form.setupUi(self)
        self.window_form.delete_button.clicked.connect(self.handle_button_delete)
        self.data_base = DataBase()
        self.reader_window = reader_window

    def handle_button_delete(self):
        reader_id = self.window_form.label.text().split(",")[0]
        param = (reader_id, )
        query_delete_history = f"DELETE FROM history WHERE fk_reader = %s"
        self.data_base.execute_query_add(query=query_delete_history, params=param)
        query = f"delete from readers where id_reader = %s"
        self.data_base.execute_query_add(query=query, params=param)
        self.reader_window.update_record()

    def text_label(self, text_form):
        self.window_form.label.setText(text_form)

#Класс формы для встраивания в скролл выдачи
class FormExtradition(QtWidgets.QWidget):
    def __init__(self, extradition_window):
        super().__init__()
        self.window_form = Ui_Form()
        self.window_form.setupUi(self)
        self.window_form.delete_button.clicked.connect(self.handle_button_delete)
        self.data_base = DataBase()
        self.extradition_window = extradition_window
        self.window_form.delete_button.setText("Провести")

    def handle_button_delete(self):
        query = f"delete from extradition where id_extradition = {self.window_form.label.text().split(" ")[0]}"
        data = self.window_form.label.text().split(" ")
        fk_reader = data[1][1:].strip('[]')
        fk_book = data[2].strip('[]')
        date_of_receipt = data[-3]
        return_date = data[-1]
        current_datetime = datetime.now()
        current_date = current_datetime.strftime("%Y-%m-%d")
        return_date_obj = datetime.strptime(return_date, "%Y-%m-%d") 
        current_date_obj = datetime.strptime(current_date, "%Y-%m-%d")
        flag_check = None
        if return_date_obj < current_date_obj:
            flag_check = False
        else:
            flag_check = True
        query_insert_history = f"""
            INSERT INTO history (fk_reader, fk_book, date_of_receipt, return_date, passed)
            VALUES (%s, %s, %s, %s, %s);
        """
        params = (fk_reader, fk_book, date_of_receipt, return_date, flag_check) 
        self.data_base.execute_query_add(query=query_insert_history, params=params)
        self.data_base.execute_query_add(query=query)
        self.extradition_window.update_extradition()

    def text_label(self, text_form):
        self.window_form.label.setText(text_form)

#Окно для обработки ошибок и получения логов
class WindowLog(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.window_log = Ui_window_logs()
        self.window_log.setupUi(self)

#Класс базы данных
class DataBase():
    def __init__(self):
        self.logs = WindowLog()

    #выполнение запроса
    def execute_query_add(self, query, params=None):
        connection = None
        cursor = None
        try:
            self.connection = pg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host
            )
            self.cursor = self.connection.cursor()
            self.cursor.execute(query, params)
            self.connection.commit()
            self.logs.window_log.text_log.clear()

        except Exception as ex:
            self.logs.window_log.text_log.clear()
            self.logs.window_log.text_log.append(f"{ex}")
            self.logs.show()
            print(ex)

        finally:
            if self.cursor is not None:
                self.cursor.close()
            elif self.connection is not None:
                self.connection.close()

    #выполнение запроса и возвращение результата
    def execute_query_read(self, query, params=None):
        connection = None
        cursor = None
        try:
            self.connection = pg2.connect(
                dbname=db_name,
                user=user,
                password=password,
                host=host
            )
            self.cursor = self.connection.cursor()
            self.cursor.execute(query, params)
            self.connection.commit()
            result = self.cursor.fetchall()

        except Exception as ex:
            self.logs.window_log.text_log.clear()
            self.logs.window_log.text_log.append(f"{ex}")
            self.logs.show()
            result = None
            print(ex)

        finally:
            if self.cursor is not None:
                self.cursor.close()
            elif self.connection is not None:
                self.connection.close()

        return result

#Первое начальное окно для перехода в другие
class MenuWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_menu = Ui_Menu() 
        self.ui_menu.setupUi(self)
        self.handler_button()
        self.books_window = BooksWindow()
        self.extradition_window = ExtraditionWindow()
        self.statistic_window = StatisticWindow()
        self.reader_window = ReaderWindow()
        self.histoty_window = History()

    def handler_button(self):
        self.ui_menu.book.clicked.connect(self.open_window_book)
        self.ui_menu.readers.clicked.connect(self.open_window_readers)
        self.ui_menu.extradition.clicked.connect(self.open_window_extradition)
        self.ui_menu.statistics.clicked.connect(self.open_window_statistics)
        self.ui_menu.history.clicked.connect(self.open_hostory_window)
    
    def open_window_book(self):
        self.books_window.show()
        self.books_window.update_record_book()

    def open_window_readers(self):
        self.reader_window.show() 
        self.reader_window.update_record()
    
    def open_window_extradition(self):
        self.extradition_window.show() 
        self.extradition_window.update_extradition()
    
    def open_window_statistics(self):
        self.statistic_window.show() 
        self.statistic_window.completion()

    def open_hostory_window(self):
        self.histoty_window.show()
        self.histoty_window.open_window()
            
#Окно записи в бд и форму в окно книг
class RecordBookWindow(QtWidgets.QMainWindow):
    def __init__(self, books_window):
        super().__init__()
        self.ui_record_book = Ui_RecordBook()
        self.ui_record_book.setupUi(self)
        self.ui_record_book.record_button.clicked.connect(self.heandler_record_button)
        self.database_obj = DataBase()
        self.log = WindowLog()
        self.books_window = books_window

    def heandler_record_button(self):
        authot_parm = self.ui_record_book.author.toPlainText()
        name_book_parm = self.ui_record_book.name_book.toPlainText()

        if not authot_parm or not name_book_parm:
            self.log.window_log.text_log.setText("Поле автор, или название книги, не может быть пустым.")
            self.log.show()
        else:
            query = f"""
            insert into books (author, reading_book) 
            values (%s, %s);
            """
            params = (authot_parm, name_book_parm)
            self.database_obj.execute_query_add(query, params=params)
            self.books_window.update_record_book()

#Окно со списком имеющихся книг
class BooksWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_books = Ui_Book()
        self.ui_books.setupUi(self)
        self.handler_button()
        self.database_obj = DataBase()
        self.record_book = RecordBookWindow(self)
        self.container_widget = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QVBoxLayout(self.container_widget)
        self.ui_books.scrollArea.setWidget(self.container_widget)

    def handler_button(self): 
        self.ui_books.pushButton.clicked.connect(self.open_record_book)
        self.ui_books.pushButton_2.clicked.connect(self.update_record_book)
        
    def open_record_book(self):
        self.record_book.show()

    def update_record_book(self):
        while self.container_layout.count():
            child = self.container_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        query = "SELECT * FROM books where id_book not in (select fk_book from extradition);"
        text_form = self.database_obj.execute_query_read(query)
        if text_form:
            for record in text_form:
                form_book = FormBook(self)
                id_book = str(record[0])
                name_book = str(record[1])
                author = str(record[2])
                record = f"{id_book}, {name_book}, {author}"
                form_book.text_label(str(record)) 
                self.container_layout.addWidget(form_book) 

#Окно записи в бд и форму в окно читателей
class RecordReader(QtWidgets.QMainWindow):
    def __init__(self, reader_window):
        super().__init__()
        self.ui_record_reader = Ui_RecordReader()
        self.ui_record_reader.setupUi(self)
        self.ui_record_reader.record_button.clicked.connect(self.heandler_record_button)
        self.database_obj = DataBase()
        self.log = WindowLog()
        self.reader_window = reader_window

    def heandler_record_button(self):
        fio = self.ui_record_reader.fio.toPlainText()
        phone = self.ui_record_reader.phone.toPlainText()
        adress = self.ui_record_reader.adress.toPlainText()
        if not fio or not phone or not adress:
            self.log.window_log.text_log.setText("Какое-то из полей не заполнено")
            self.log.show()
        else:
            query = f"""
                insert into readers (fio, phone, adress)
                values (%s, %s, %s)
            """
            params = (fio, phone, adress)
            self.database_obj.execute_query_add(query=query, params=params)
            self.reader_window.update_record()

#Окно со списком имеющихся учетных записей пользователей
class ReaderWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_reader = Ui_Reader()
        self.ui_reader.setupUi(self)   
        self.heandlear_button()
        self.database_obj = DataBase()
        self.record_reader_window = RecordReader(self)
        self.container_widget = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QVBoxLayout(self.container_widget)
        self.ui_reader.scrollArea.setWidget(self.container_widget)

    def heandlear_button(self):
        self.ui_reader.pushButton.clicked.connect(self.open_record_window)
        self.ui_reader.pushButton_2.clicked.connect(self.update_record)
    
    def open_record_window(self):
        self.record_reader_window.show()

    def update_record(self):
        while self.container_layout.count():
            child = self.container_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        query = "SELECT * FROM readers;"
        text_form = self.database_obj.execute_query_read(query)
        if text_form:
            for record in text_form:
                form_book = FormReader(self)
                id_reader = str(record[0])
                fio = str(record[1])
                phone = str(record[2])
                adress = str(record[3])
                record = f"{id_reader}, {fio}, {phone}, {adress}"
                form_book.text_label(str(record)) 
                self.container_layout.addWidget(form_book) 

#Окно записи в бд и форму в окно выдачи
class RecordExtradition(QtWidgets.QMainWindow):
    def __init__(self, extradition_window):
        super().__init__()
        self.ui_record_extradition = Ui_RecordExtradition()
        self.ui_record_extradition.setupUi(self)
        self.database = DataBase()
        self.log = WindowLog()
        self.ui_record_extradition.record_button.clicked.connect(self.heandler_record)
        self.ui_record_extradition.date_extradition.setDate(QDate(2024, 1, 1))
        self.ui_record_extradition.date_return.setDate(QDate(2024, 1, 1))
        self.extradition_window = extradition_window

    def filling_lists(self):
        self.ui_record_extradition.listWidget.clear()
        self.ui_record_extradition.listWidget_2.clear()
        query_books = "select * from books where id_book not in (select fk_book from extradition);"
        books = self.database.execute_query_read(query=query_books)
        for elem_books in books:
            elem_resent = f"{elem_books[0]}, {elem_books[1]}"
            self.ui_record_extradition.listWidget.addItem(elem_resent)
        query_readers = "select * from readers"
        readers = self.database.execute_query_read(query=query_readers)
        for elem_readers in readers:
            elem_resent = f"{elem_readers[0]}, {elem_readers[1]}"
            self.ui_record_extradition.listWidget_2.addItem(elem_resent)
    
    def heandler_record(self):
        book_item = self.ui_record_extradition.listWidget.currentItem()
        reader_item = self.ui_record_extradition.listWidget_2.currentItem()
        if book_item and reader_item:
            book_item = book_item.text().split(',')[0]
            reader_item = reader_item.text().split(',')[0]
            date_extradition = self.ui_record_extradition.date_extradition.date().toString("yyyy-MM-dd")
            date_return = self.ui_record_extradition.date_return.date().toString("yyyy-MM-dd")
            query = f"""
                insert into extradition (fk_reader, fk_book, date_of_receipt, return_date)
                values (%s, %s, %s, %s)
            """
            params = (reader_item, book_item, date_extradition, date_return)
            self.database.execute_query_add(query=query, params=params)
            self.filling_lists()
            self.extradition_window.update_extradition()
        else:
            self.log.window_log.text_log.setText("Выберите элементы из таблиц")
            self.log.show()

#Окно со списком даты взятия и возврата книг с подробной инф.          
class ExtraditionWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_extradition = Ui_Extradition()
        self.ui_extradition.setupUi(self)   
        self.headler_button()
        self.record_extradition = RecordExtradition(self)
        self.database_obj = DataBase()
        self.container_widget = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QVBoxLayout(self.container_widget)
        self.ui_extradition.scrollArea.setWidget(self.container_widget)

    def headler_button(self):
        self.ui_extradition.pushButton.clicked.connect(self.open_record_extradition_window)
        self.ui_extradition.pushButton_2.clicked.connect(self.update_extradition)

    def open_record_extradition_window(self):
        self.record_extradition.filling_lists()
        self.record_extradition.show()

    def update_extradition(self):
        while self.container_layout.count():
            child = self.container_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        query_date_and_id_fk = "SELECT * FROM extradition;"
        data_extradition = self.database_obj.execute_query_read(query_date_and_id_fk)
        if data_extradition:
            for enemes in data_extradition:
                id_reader = f"{enemes[1]}"
                query_name_reader = f"select fio from readers where id_reader = %s"
                param_id_reader = (id_reader,)
                reader_name = self.database_obj.execute_query_read(query_name_reader, params=param_id_reader)
                id_book = f"{enemes[2]}"
                query_name_book = f"select reading_book, author from books where id_book = %s"
                param_id_book = (id_book,)
                book_name = self.database_obj.execute_query_read(query_name_book, params=param_id_book)
                text_form = f"{enemes[0]} [{enemes[1]} {enemes[2]}] - {book_name[0][0]} [{book_name[0][1]}], {reader_name[0][0]} : {enemes[3]} / {enemes[4]}"
                form_book = FormExtradition(self)
                form_book.text_label(str(text_form))
                self.container_layout.addWidget(form_book)

#История всех выданных книг
class History(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_history = Ui_History()
        self.ui_history.setupUi(self)  
        self.container_widget = QtWidgets.QWidget()
        self.container_layout = QtWidgets.QVBoxLayout(self.container_widget)
        self.ui_history.scrollArea.setWidget(self.container_widget)
        self.database_obj = DataBase()

    def open_window(self):
        while self.container_layout.count():
            child = self.container_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        query_data = "SELECT * FROM history;"
        data = self.database_obj.execute_query_read(query_data)
        if data:
            for elem in data:
                flag_except = elem[5]
                date_extradition = elem[3]
                date_return = elem[4]
                id_reader = elem[1]
                id_book = elem[2]
                query_data_reader = "select fio, phone, adress from readers where id_reader = %s;"
                param_data_reader = (id_reader, )
                data_reader = self.database_obj.execute_query_read(query_data_reader, params=param_data_reader)
                query_data_book = "select reading_book, author from books where id_book = %s;"
                param_data_book = (id_book, )
                data_book = self.database_obj.execute_query_read(query_data_book, params=param_data_book)
                book_title, book_author = data_book[0]
                reader_name, reader_phone, reader_adress = data_reader[0]
                text_form = f"{book_title}, {book_author} | {reader_name}, {reader_phone}, {reader_adress} | {date_extradition}/{date_return}"
                form_book = FormHistory()
                form_book.text_label(str(text_form))
                if not flag_except:
                    form_book.set_text_color_red()
                    form_book.text_label(f"{str(text_form)} - Просрочено")
                else:
                    form_book.text_label(str(text_form))
                self.container_layout.addWidget(form_book)

class StatisticWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui_statistic = Ui_Statisctic()
        self.ui_statistic.setupUi(self)  
        self.database_obj = DataBase()
        self.all_books = self.ui_statistic.sum_book
        self.all_readers = self.ui_statistic.sum_readers
        self.all_extraditions = self.ui_statistic.sum_extradition
        self.all_book_to_extradition = self.ui_statistic.sum_book_to_extradition
        self.list_readers = self.ui_statistic.list_top_readers
        self.list_books = self.ui_statistic.list_top_book

    def completion(self):
        # Запросы для подсчета общей информации
        query_all_books = "SELECT COUNT(*) FROM books"
        self.all_books.setText(str(self.database_obj.execute_query_read(query=query_all_books)[0][0]))
        query_all_readers = "SELECT COUNT(*) FROM readers"
        self.all_readers.setText(str(self.database_obj.execute_query_read(query=query_all_readers)[0][0]))
        query_all_extradition = "SELECT COUNT(*) FROM extradition"
        self.all_extraditions.setText(str(self.database_obj.execute_query_read(query=query_all_extradition)[0][0]))
        # Получаем количество доступных для выдачи книг
        self.all_book_to_extradition.setText(str(int(self.database_obj.execute_query_read(query=query_all_books)[0][0]) - int(self.database_obj.execute_query_read(query=query_all_extradition)[0][0])))
        # Получаем топ-3 самых популярных книг
        query_top_books = """
            SELECT b.reading_book, b.author, COUNT(h.fk_book) AS count
            FROM history h
            JOIN books b ON h.fk_book = b.id_book
            GROUP BY b.id_book
            ORDER BY count DESC
            LIMIT 3;
        """
        top_books = self.database_obj.execute_query_read(query=query_top_books)
        self.list_books.clear()  # Очищаем предыдущие записи
        for book in top_books:
            book_title, book_author, count = book
            self.list_books.addItem(f"{book_title} by {book_author} - {count} раз(a)")
        # Получаем топ-3 самых активных пользователей
        query_top_readers = """
            SELECT r.fio, COUNT(h.fk_reader) AS count
            FROM history h
            JOIN readers r ON h.fk_reader = r.id_reader
            GROUP BY r.id_reader
            ORDER BY count DESC
            LIMIT 3;
        """
        top_readers = self.database_obj.execute_query_read(query=query_top_readers)
        self.list_readers.clear()  # Очищаем предыдущие записи
        for reader in top_readers:
            reader_name, count = reader
            self.list_readers.addItem(f"{reader_name} - {count} раз(a)")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MenuWindow()
    window.show()
    sys.exit(app.exec_())