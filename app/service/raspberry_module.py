import json

def image_frame_to_seat_map(request):
    try:
        dct_request = request.json()
        str_vehicle_id = dct_request.get("str_vehicle_id")
        str_image_frame_base64 = dct_request.get("str_img_frame")
    except Exception as e:
        return json.dumps({"status":"fail","message":str(e)})