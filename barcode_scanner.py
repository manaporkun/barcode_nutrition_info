from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import cv2
from get_barcode_info import get_barcode_information
from ui import ui

old_barcode = ''
barcode_data = ''

def read_barcode(db):
    vs = VideoStream(src=0).start()
    text = ''
    global barcode_data 


    while True:

        frame = vs.read()
        frame = imutils.resize(frame, width=720)

        barcodes = pyzbar.decode(frame)
        
        for barcode in barcodes:

            (x, y, w, h) = barcode.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

            barcode_data = barcode.data.decode("utf-8")
            # barcode_type = barcode.type

            query = {'barcode': barcode_data}
            
            if db.get(query).collection.count_documents(query) == 0 and barcode_data != '':
                db.push(get_barcode_information(barcode_data))
                
            # product = db.get(query)[0]
            # my_ui.update_ui(product)
                
            text = barcode_data
            #text = "{}: {}".format(barcode_data)
            cv2.putText(frame, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            

        query = {'barcode':barcode_data}
        # cv2.putText(frame, text, (720//2, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 4)
        global old_barcode
        if barcode_data != '' and old_barcode != barcode_data:
            print(db.get(query)[0])
            old_barcode = barcode_data
            
        cv2.imshow("Barcode Scanner", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break


    cv2.destroyAllWindows()

def get_barcode_data():
    return barcode_data