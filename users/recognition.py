from deepface import DeepFace
import os

def verify_face(img_path):
    base = "media/faces"

    for person in os.listdir(base):
        person_path = os.path.join(base, person)

        for img in os.listdir(person_path):
            try:
                result = DeepFace.verify(img_path, os.path.join(person_path, img), enforce_detection=False)

                if result["verified"]:
                    return person
            except:
                pass

    return None