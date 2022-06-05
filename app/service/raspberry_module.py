import json
import cv2
import argparse
import numpy as np
import base64
from app import ins_db
from app.model import Vehicle


def image_frame_to_seat_map(request):
    try:
        dct_request = request.json
        str_vehicle_id = dct_request.get("str_vehicle_id")
        if dct_request.get("str_img_frame")[1] == "b":
            str_image_frame_base64 = dct_request.get("str_img_frame")[2:-1]
        else:
            str_image_frame_base64 = dct_request.get("str_img_frame")

        # Convert base64 to image    
        strImageFilename = "./app/data/"+str_vehicle_id+"_raw.jpg"
        encImgFile = open(strImageFilename, 'wb')
        encImgFile.write(base64.b64decode((str_image_frame_base64)))
        encImgFile.close()

        # objects detection from raw image            
        image = cv2.imread(strImageFilename)

        Width = image.shape[1]
        Height = image.shape[0]
        scale = 0.00392

        classes = None
        with open('./app/yolo/yolov3.txt', 'r') as f:
            classes = [line.strip() for line in f.readlines()]

        COLORS = np.random.uniform(0, 255, size=(len(classes), 3))

        net = cv2.dnn.readNet('./app/yolo/yolov3.weights', './app/yolo/yolov3.cfg')

        blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

        net.setInput(blob)

        outs = net.forward(get_output_layers(net))

        class_ids = []
        confidences = []
        boxes = []
        conf_threshold = 0.5
        nms_threshold = 0.4

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5 and class_id == 0:
                    center_x = int(detection[0] * Width)
                    center_y = int(detection[1] * Height)
                    w = int(detection[2] * Width)
                    h = int(detection[3] * Height)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h,detection[2],detection[1]])

        # indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)
        # (34, 2317, 1542, 3261, 1)

        seats = [(51, 2317, 1601, 3220, "L1" ,2),(757, 939, 1297, 1011,"L9",3),(308, 1812, 1458, 2317 , "L2",2),(440, 1540, 1326, 1812, "L3",2),(500, 1363, 1262, 1540, "L4",2),(564, 1242, 1199, 1363, "L5",2),(652, 1144, 1202, 1242, "L6",2),(1486, 1363, 2270, 1589, "R3",2)]
        objSeatMap = {"Left":{},"Right":{}}
        arrAlreadyDetected = []
        for seatContour in seats:
            x1,y1,w1,h1,seatId,seatCount = seatContour
            arrSeat = []
            arrSeat = [False]*seatCount            
            for box in boxes:
                # i = i[0]
                if box not in arrAlreadyDetected:
                    # box = boxes[i]
                    x = box[0]
                    y = box[1]
                    w = box[2]
                    h = box[3]

                    if h>2*w:
                        h = h * 0.65
                    cen_x,cen_y = round(x+(w/2)),round(y+(h/2))
                    # check for seats
                    if cen_x > x1 and cen_x < w1 and cen_y > y1 and cen_y < h1:                    
                        if seatCount == 2:
                            # two seater
                            left_dist = cen_x - x1
                            right_dist = w1 - cen_x

                            if left_dist < right_dist:
                                arrSeat[0] = True
                            else:
                                arrSeat[1] = True
                            arrAlreadyDetected.append(box) 
                        elif seatCount > 2:
                            # three seater
                            pass
                    
                    # cv2.putText(image, "Person :"+str(i), (round(x)-20,round(y)-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[i], 2)
                    # draw_prediction(image, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+(h)))

            if "L" in seatId:
                objSeatMap["Left"][int(seatId[1:])] = arrSeat
            elif "R" in seatId:
                objSeatMap["Right"][int(seatId[1:])] = arrSeat

        cv2.waitKey()
        # cv2.imwrite("object-detection.jpg", image)
        # imShow('object-detection.jpg')
        cv2.destroyAllWindows()

        # update seat map to DB
        vehicle = Vehicle.query.filter_by(pk_bint_vehicle_id=str_vehicle_id).first()
        if vehicle:
            vehicle.json_seat_map = objSeatMap
            save_changes(vehicle)

            return json.dumps({"status":"success"})
        else:
            return json.dumps({"status":"fail","message":"No vehicle with this ID is found"})

    except Exception as e:
        print(e)
        return json.dumps({"status":"fail","message":str(e)})

def get_output_layers(net):    
    layer_names = net.getLayerNames()    
    # python >3.7
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    # if python <=3.7 uncomment this 
    # output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    return output_layers

def save_vehicle_location(request):
    dct_request = request.json

    try:
        str_vehicle_id = dct_request.get("str_vehicle_id")
        str_longitude = dct_request.get("str_longitude")
        str_latitude = dct_request.get("str_latitude")

        vehicle = Vehicle.query.filter_by(pk_vchr_vehicle_id=str_vehicle_id).first()

        if vehicle:
            vehicle.json_location = {"longitude":str_longitude,"str_latitude":str_latitude}
            save_changes(vehicle)
            return json.dumps({"status":"success"})
        else:
            return json.dumps({"status":"fail","message":"No vehicle with this ID is found"})

    except Exception as e:
        print(e)
        return json.dumps({"status":"fail","message":str(e)})

def save_changes(data):
    ins_db.session.add(data)
    ins_db.session.commit()
