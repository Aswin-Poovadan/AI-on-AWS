import cv2
#opencv-photo capture
cap = cv2.VideoCapture(0)
myphoto="aswinai.jpg"
ret , photo = cap.read()
cv2.imwrite( myphoto ,photo)
cap.release()
#boto3:s3 upload
import boto3
s3=boto3.resource('s3')
bucket="aionaws-aswin"
s3.Bucket(bucket).upload_file(myphoto,"aiimage.jpg")
#connect rek
region="ap-south-1"
rek=boto3.client('rekognition',region)
#object_detect
upimage="aiimage.jpg"
response=rek.detect_labels(
    Image= {
        "S3Object": {
            "Bucket": bucket,
            "Name": upimage,
        }
    },
    MaxLabels=10,
    MinConfidence=80
)
print(response)
#face_detect
resfaces=rek.detect_faces(
    Image= {
        "S3Object": {
            "Bucket": bucket,
            "Name": upimage,
        }
    },
    Attributes=['ALL']
)
print(resfaces)
