import pyodbc

class NwProducts:
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'

        self.new_northwind_db =  pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}' +
                                                ';SERVER=' + self.server +
                                                ';DATABASE='+self.database +
                                                ';UID='+self.username +
                                                ';PWD='+self.password)

        self.cursor = self.new_northwind_db.cursor()

    def __sql_query_no_transaction(self, sql_query): ##encapsulated to no allow users to change any data
        return self.cursor.execute(sql_query)

    def output_all_product_records(self):
        # create a query to select all
        # use the cursor and execute on the query

        query_records = self.__sql_query_no_transaction("SELECT * FROM Products")

        # Continuously iterate (while loop)
            # output each record (fetchone()
            # We will break when the record is none.
        while True:
            record = query_records.fetchone()
            if record is None:
                break
            print(record)

    def print_average_unit_price(self):
        # get the price of the products
        query_records = self.__sql_query_no_transaction("SELECT * FROM Products")
        # store them in a list
        total_unit_price = []
        while True:
            record = query_records.fetchone()
            if record is None:
                break   #when there are no more records, then break the loop
            total_unit_price.append(record.UnitPrice)
            # total sum of price / number of units
        print(sum(total_unit_price)/len(total_unit_price))
