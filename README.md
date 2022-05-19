# Defeating-AIMS-Captcha
Captchas are annoying. So, to save those 5 seconds spent filling captcha on [AIMS](https://aims.iith.ac.in/aims/). We will build a Deep learning model to almost accurately solve the captcha for us. Although, by making this model I would be spending collectively more time solving a problem which requires comparitively smaller time.

Follow this tutorial to learn how to build a captcha Defeator.

We can divide the task into subsections

## Data Collection
This task may seem particularly boring at first, but trust me it is interesting. Think of how would you collect the dataset manually?

I can think of two ways
1. Search for the original captcha image dataset which AIMS portal uses. This is indeed a boring method, you can search for different captcha image datasets or try reverse searching some image. I don't prefer this method, it's likely it won't even work.
2. The more interesting approach is go the the AIMS portal and download the captcha image by right clicking on image. But do you really have to visit the website yourself however many images you want? The answer is simple, write a code that does it for you. Look at `get-images.py`. I've written comments in that file to help you with understanding the code there. **The only reason this approach works is because AIMS portal has a flaw, it has exposed label for the Captcha image on the first**

## Preprocessing
So, this is certaining a boring task. You have the dataset of captcha images, each with 5 characters but unfortunately it's not quite the type data you need. You need individual characters. That's where our saviour OpenCV kicks in. Although, I found the BGR ordering quite annoying, OpenCV is a great tool. We will first remove all the unecessary things from the image and also make it grayscale. Begin with converting the image to grayscale. Our next quest is removing the unecessary things from the image. We would like to have somthing like the beautiful MNIST dataset gives us. We use a threshold (220), any pixel with intensity below that is set to 0, and anything more is set to 255. Just that simply we were able to bring the image with a lot going on (there's gray background, there's some circles etc) to just the character blobs sitting in the image screaming to be extracted. The question is how do you identify where those blobs are in the image? OpenCV saves the day again with `find_contours` method. Now, I'd like you to go read the `break-image.py` code, it has enough comments to walk you through the code and then come back here.... Alright, So the dataset that we created can be found on [kaggle]([www.kaggle.com/cmaspi/character](https://www.kaggle.com/datasets/cmaspi/character)), I won't include it in this repository for size constraints. You can always download the data using kaggle API
```bash
kaggle datasets download -d cmaspi/character
```

## SHOWDOWN
Now, we are down to just writing a CNN model to fit our data. 
