import numpy as np
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import cv2
import json

import albumentations as A
import streamlit as st


def load_image(image_name, path_to_folder = '../images'):
    path_to_image = os.path.join(path_to_folder, image_name)
    image = cv2.imread(path_to_image)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image


def show_int_interval(name, limits, defaults, **kwargs):
    min_max_interval = st.sidebar.slider(name, limits[0], limits[1], defaults)
    return min_max_interval



# dict from param name to function showing this param
param2func = {
    'int_interval': show_int_interval
}



st.title('Demo of Albumentations transforms')


# selecting the image
path_to_images = 'images'
image_names_list = [x for x in os.listdir(path_to_images) if x[-3:] in ['jpg', 'peg', 'png']]
image_name = st.sidebar.selectbox('Select an image:', image_names_list)
image = load_image(image_name, path_to_images)


# selecting the transformation
path_to_config = 'configs/augmentations.json'
with open(path_to_config, 'r') as config_file:
    augmentations = json.load(config_file)
transform_name = st.sidebar.selectbox('Select a transformation:', list(augmentations.keys()))
transform_params = augmentations[transform_name]


# show the transform options
if len(transform_params) == 0:
    st.sidebar.text(transform_name + ' transform has no parameters')
else:
    for param in transform_params:
        param['value'] = param2func[param['type']](**param)
        
        
params_string = ','.join([param['name'] + '=' + str(param['value']) for param in transform_params] + ['p=1.0'])
params_string = '(' + params_string + ')'

st.text('Press R to update')
exec('transform = A.' + transform_name + params_string)
st.image([image, transform(image = image)['image']], 
         caption = ['Original image', 'Transformed image'],
         width = 320)
st.text(str(transform.__doc__))