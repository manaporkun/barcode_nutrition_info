from database_operations import MongoDB
import new_barcode_scanner
import sys

db_name = sys.argv[1]
table_name = sys.argv[2]
user_name = sys.argv[3]
password = sys.argv[4]

db = MongoDB(db_name, table_name, user_name, password)

b_scanner = new_barcode_scanner.BarcodeScanner(db)

b_scanner.read_barcode()
