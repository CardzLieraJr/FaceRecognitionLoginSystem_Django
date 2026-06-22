from django.http import JsonResponse
from django.conf import settings
from .face_utils import capture_face
from .recognition import verify_face
import cv2
import os
import shutil


def register(request):
    name = request.GET.get("name")

    if not name:
        return JsonResponse({"status": "error", "message": "Name required"})

    capture_face(name)

    return JsonResponse({"status": "registered", "user": name})


def login(request):
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        return JsonResponse({"status": "error", "message": "Camera not available"})

    ret, frame = cam.read()

    if not ret or frame is None:
        cam.release()
        return JsonResponse({"status": "error", "message": "Failed to capture image"})

    temp_path = os.path.join(settings.MEDIA_ROOT, "temp.jpg")

    cv2.imwrite(temp_path, frame)

    cam.release()

    user = verify_face(temp_path)

    if user:
        return JsonResponse({"status": "success", "user": user})
    else:
        return JsonResponse({"status": "failed"})


def delete_user(request):
    name = request.GET.get("name")

    if not name:
        return JsonResponse({"status": "error", "message": "name is required"})

    path = f"media/faces/{name}"

    if os.path.exists(path):
        shutil.rmtree(path)
        return JsonResponse({"status": "deleted", "user": name})

    return JsonResponse({"status": "not found"})
