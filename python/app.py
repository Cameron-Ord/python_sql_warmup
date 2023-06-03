import input_handler
import dbcreds
import mariadb

def input():

    while(True):

        choice = input_handler.option()
        
        if(choice == "1"):

            conn = mariadb.connect(**dbcreds.conn_params)
            cursor = conn.cursor()
            name = input_handler.sales()
            print(name)
            cursor.execute('CALL insert_sales_person(?)', [name])
            cursor.close()
            conn.close()
            return

        elif(choice == "2"):

            conn = mariadb.connect(**dbcreds.conn_params)
            cursor = conn.cursor()
            name = input_handler.item()
            price = input_handler.item_price()
            cursor.execute('CALL insert_item(?, ?)', [name, price])
            cursor.close()
            conn.close()
            return


        elif(choice == "3"):

            conn = mariadb.connect(**dbcreds.conn_params)
            cursor = conn.cursor()
            sales_per_id = input_handler.per_id()
            item_id = input_handler.item_id()
            cursor.execute('CALL insert_sale(?, ?)', [sales_per_id, item_id])
            cursor.close()
            conn.close()
            return
        
        else:
            break

input()


