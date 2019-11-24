# albumentations-demo

This service is created to demonstrate abilities of the [Albumentations](https://github.com/albumentations-team/albumentations) - a library for efficient image augmentations.

## Easy start
You can play with this service right now [https://albumentations-demo.herokuapp.com/](https://albumentations-demo.herokuapp.com/)
(It is deployed on free service with very limited computing power and can be quite unstable)

If you would like to run it locally follow the installation instruction.

## Installation
```
git clone https://github.com/IliaLarchenko/albumentations-demo
cd albumentations-demo
pip install -r requirements.txt
streamlit run src/app.py
```

If you want to work with you own images just replace the last line with:
```
streamlit run src/app.py -- --images_folder PATH_TO_YOUR_IMAGE_FOLDER
```

In your terminal you will see the link to the running local service similar to : 
```console
  You can now view your Streamlit app in your browser.

  Network URL: http://YOUR_LOCAL_IP:8501
  External URL: http://YOUR_GLOBAL_IP:8501
```
Just follow the local link to use the service.

## How to use

The interface is very simple and intuitive:
1. On the left you have a control sidebar. You can choose the image and the transformation.
2. After that you will see the control elements for the every parameter this transformation has.
3. Every time you change any parameter you will see the augmented version of the image on the right side of your screen.
4. Below the images you can find a code for calling of the augmentation with selected parameters.
5. You can also find there the original docstring for this transformation.
![screenshot](docs/screenshot.jpg?raw=true)


## Links
* Albumentations library: [github.com/albumentations-team/albumentations](https://github.com/albumentations-team/albumentations)
* Image Source: [pexels.com/royalty-free-images](https://pexels.com/royalty-free-images/)
* Streamlit - framework powering this app [github.com/streamlit/streamlit](https://github.com/streamlit/streamlit)  
