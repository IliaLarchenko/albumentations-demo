import numpy as np
import os
import cv2
import json

import albumentations as A
import streamlit as st

from control import *


def load_image(image_name, path_to_folder="../images"):
    path_to_image = os.path.join(path_to_folder, image_name)
    image = cv2.imread(path_to_image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


st.title("Demo of Albumentations transforms")


# selecting the image
path_to_images = "images"
image_names_list = [
    x for x in os.listdir(path_to_images) if x[-3:] in ["jpg", "peg", "png"]
]
image_name = st.sidebar.selectbox("Select an image:", image_names_list)
image = load_image(image_name, path_to_images)


# selecting the transformation
path_to_config = "configs/augmentations.json"
with open(path_to_config, "r") as config_file:
    augmentations = json.load(config_file)
transform_name = st.sidebar.selectbox(
    "Select a transformation:", sorted(list(augmentations.keys()))
)
transform_params = augmentations[transform_name]


# show the transform options
if len(transform_params) == 0:
    st.sidebar.text(transform_name + " transform has no parameters")
else:
    for param in transform_params:
        param["value"] = param2func[param["type"]](**param)


params_string = ", ".join(
    [param["param_name"] + "=" + str(param["value"]) for param in transform_params]
    + ["p=1.0"]
)
params_string = "(" + params_string + ")"

st.text(transform_name + params_string)
st.text("Press R to update")
exec("transform = A." + transform_name + params_string)
st.image(
    [image, transform(image=image)["image"]],
    caption=["Original image", "Transformed image"],
    width=320,
)

st.subheader("Docstring:")
st.text(str(transform.__doc__))


st.text("")
st.text("")
st.subheader("Credentials:")
st.text("Source: https://github.com/IliaLarchenko/albumentations-demo")
st.text("Albumentations library: https://github.com/albumentations-team/albumentations")
st.text("Image Source: https://www.pexels.com/royalty-free-images/")
