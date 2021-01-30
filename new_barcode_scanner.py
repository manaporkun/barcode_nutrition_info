from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import cv2
from get_barcode_info import get_barcode_information


class BarcodeScanner:
    def __init__(self, db):
        self.old_barcode = ''
        self.barcode_data = ''
        self.query = ''
        self.product_count = 1
        self.db = db
        self.isBarcode = False

    def read_barcode(self):
        vs = VideoStream(src=0).start()

        while True:

            frame = vs.read()
            frame = imutils.resize(frame, width=720)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # calculate x & y gradient
            gradX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1)
            gradY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=-1)

            # subtract the y-gradient from the x-gradient
            gradient = cv2.subtract(gradX, gradY)
            gradient = cv2.convertScaleAbs(gradient)

            # blur the image
            blurred = cv2.blur(gradient, (3, 3))

            # threshold the image
            (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
            thresh = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            barcodes = pyzbar.decode(frame)

            for barcode in barcodes:

                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

                self.barcode_data = barcode.data.decode("utf-8")
                # barcode_type = barcode.type

                self.query = {'barcode': self.barcode_data}

                self.isBarcode = self.barcode_data[0] == '8'

                if self.isBarcode and self.barcode_data != '' and self.old_barcode != self.barcode_data:
                    self.product_count = self.db.get(self.query).collection.count_documents(self.query)

                if self.isBarcode and self.product_count == 0 and self.barcode_data != '':
                    product = get_barcode_information(self.barcode_data)
                    if product['name'] == '' or product['name'] is None:
                        print('\nName not found\n')
                    else:
                        self.db.push(product)
                        print('\npushed\n:', product['name'], self.barcode_data, self.product_count)

                text = self.barcode_data
                cv2.putText(frame, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            if self.isBarcode and self.product_count != 0 and self.barcode_data != '' and self.old_barcode != self.barcode_data:
                product = self.db.get(self.query)[0]
                print('\n')
                for info in product:
                    print(info, ' : ', product[info])
                print('\n------------------------------------------------')
                self.old_barcode = self.barcode_data
                continue

            cv2.imshow("Barcode Scanner", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break

        cv2.destroyAllWindows()
