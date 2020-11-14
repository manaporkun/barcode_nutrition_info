from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import cv2
from get_barcode_info import get_barcode_information


old_barcode = ''
barcode_data = ''
query = ''
product_count = 0


def read_barcode(db):
    vs = VideoStream(src=0).start()
    text = ''

    global barcode_data
    global old_barcode
    global query
    global product_count

    while True:

        frame = vs.read()
        frame = imutils.resize(frame, width=960)

        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:

            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            barcode_data = barcode.data.decode("utf-8")
            # barcode_type = barcode.type

            query = {'barcode': barcode_data}

            product_count = db.get(query).collection.count_documents(query)
            print(product_count)
            if product_count == 0 and barcode_data != '':
                product = get_barcode_information(barcode_data)
                if product['name'] == '' or product['name'] == None:
                    print('\nName not found\n')
                else:
                    db.push(product)
                    print('\npushed\n:', product['name'])

            text = barcode_data
            cv2.putText(frame, text, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        """
        if product_count != 0 and barcode_data != '' and old_barcode != barcode_data:
            print(db.get(query)[0])
            old_barcode = barcode_data
        """
        cv2.imshow("Barcode Scanner", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    # cv2.destroyAllWindows()


def get_barcode_data():
    return barcode_data
