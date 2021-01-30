# Barcode Nutrition Info

Information:

This project reads the barcode of the product with the webcam. And with the barcode data, it uses http://barkodoku.com/ website to search for the barcode. With this information (name, date, country, price), it searches for the product on the website https://www.fatsecret.com.tr. After that, it displays the product information such as calorie, fat, protein, carbohydrate etc. on the terminal.

Requirements:

requests
bs4
imutils
pyzbar
opencv-python
pymongo
dnspython

How to use it:

Firstly, you need to create a MongoDB Cloud Server. After that, you have to install the requirements. Finaly, you need to enter database name, table name, user name and password information as arguments. 

For example you can run the code like this:

python main.py db_name table_name user_name password
