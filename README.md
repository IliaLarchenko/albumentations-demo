# albumentations-demo

This service is created to demonstrate abilities of the [Albumentations](https://github.com/albumentations-team/albumentations) - a library for efficient image augmentations.
[Link to my article about augmentations selection and why this service can be useful](https://towardsdatascience.com/explore-image-augmentations-using-a-convenient-tool-a199b4ac8214)

## Easy start
I don't actively support this tool anymore but you can run it locally or use one of the deployed instances. 

If you would like to run the service locally follow the installation instruction.

You can find the online version of this tool here: [https://albumentations-demo.herokuapp.com/](https://albumentations-demo.herokuapp.com/) (it will be stopped soon).

It is also deployed as a Hugging Face space: [https://huggingface.co/spaces/ilarchenko/albumentations-demo](https://huggingface.co/spaces/ilarchenko/albumentations-demo)

As alternative you can use the fork supported and deployed by the Albumentations team [https://demo.albumentations.ai/](https://demo.albumentations.ai/)

## Installation and run
```
git clone https://github.com/IliaLarchenko/albumentations-demo
cd albumentations-demo
pip install -r requirements.txt
streamlit run src/app.py
```

If you want to work with you own images just replace the last line with:
```
streamlit run src/app.py -- --image_folder PATH_TO_YOUR_IMAGE_FOLDER
```

If your images have some unusual proportions you can use `image_width` parameter to set the width in pixels of the original image to show. The width of the transformed image and heights of both images will be computed automatically. Default value of width is `400`.
```
streamlit run src/app.py -- --image_width INT_VALUE_OF_WIDTH
```


In your terminal you will see the link to the running local service similar to : 
```console
  You can now view your Streamlit app in your browser.

  Network URL: http://YOUR_LOCAL_IP:8501
  External URL: http://YOUR_GLOBAL_IP:8501
```
Just follow the local link to use the service.

## Run in docker
You can run the service in docker:
```
docker-compose up
```
It will be available at http://DOCKER_HOST_IP:8501

## How to use

The interface is very simple and intuitive:
1. On the left you have a control sidebar. Select the "Simple" mode. You can choose the image and the transformation.
2. After that you will see the control elements for the every parameter this transformation has.
3. Every time you change any parameter you will see the augmented version of the image on the right side of your screen.
4. Below the images you can find a code for calling of the augmentation with selected parameters.
5. You can also find there the original docstring for this transformation.
![screenshot](docs/screenshot.jpg?raw=true)


## Professional mode
In the professional mode you can:
1. Upload your own image
2. Combine multiple transformations
3. See the random parameters used to get the result

Be aware that in Professional mode some combination of parameters of different transformations can be invalid. You should control it.

## Links
* Albumentations library: [github.com/albumentations-team/albumentations](https://github.com/albumentations-team/albumentations)
* Image Source: [pexels.com/royalty-free-images](https://pexels.com/royalty-free-images/)
* Streamlit - framework powering this app [github.com/streamlit/streamlit](https://github.com/streamlit/streamlit)  
