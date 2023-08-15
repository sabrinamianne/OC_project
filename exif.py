import streamlit as st

from exif import Image as ExifImage
from PIL import Image as PillowImage
from PIL import ExifTags

PILLOW_TAGS = [
    271,    # Camera Make
    272,    # Camera Model
    36867,  # Date/Time Photo Taken
    34853,  # GPS Info
]
EXIF_TAGS = [
    "make",
    "model",
    "datetime_original",
    "gps_latitude",
    "gps_latitude_ref",
    "gps_longitude",
    "gps_longitude_ref",
    "gps_altitude",
]

pillow_img = PillowImage.open("p.jpeg")
img_exif = pillow_img.getexif()

for tag in PILLOW_TAGS:
    try:
        english_tag = ExifTags.TAGS[tag]
        value = img_exif[tag]
    except:
        continue
    st.write("{}: {}".format(english_tag, value))
    print("{}: {}".format(english_tag, value))

with open("p.jpeg", "rb") as input_file:
    img = ExifImage(input_file)

for tag in EXIF_TAGS:
    value = img.get(tag)
    st.write('{}: {}'.format(tag, value))
    print('{}: {}'.format(tag, value))




with open("p.jpeg", "rb") as input_file:
    exif_img = ExifImage(input_file)
    prenom = st.text_input('Quel est votre prénom ?')    
    exif_img.artist = prenom
 

with open(img, "wb") as ofile:
    ofile.write(exif_img.get_file())
