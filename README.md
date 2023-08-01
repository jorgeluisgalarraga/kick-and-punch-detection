# Kick and Punch detection Notebook
This came as a group idea, we started as a class project. However, we couldn't get a good accuracy.

We used a dataset that we created from scratch, after watching MMA's videos on youtube, and looking for different fight images on the internet. This data set contains 4 classes, **kick**, **kicknt**, **punch**, and **punchnt**. The ***nt*** means not touch.

The dataset can be downloaded from [Roboflow](https://universe.roboflow.com/georgebrown/punch-and-kick-detection-group). This tool allowed us to do the image classification, and the split of the dataset, which is very interisting and easy to go.

So far, we have tried different  [Keras](https://keras.io/api/applications/) applications such as vgg16, ResNet50V2, and InceptionResNetV2.

With these three models and 4 classes we got the following results:

- VGG16 with 100.356 trainable params and 14.815.044 total params, no dropout but with data augmentation ![VGG16 4 classes](/images/image-3.png)
- ResNet50V2 with 401.412 trainable parameters and 23.966.212 total params, no dropout but with data augmentation ![ResNet50V2 4 classes](/images/image-4.png)
- InceptionResNetV2 with 3.985.412 trainable parameters and 55.125.732 total params, with dropout of 0.5, Average Pooling and a fully connect layer ![InceptionResNetV2 with 4 classes](/images/image-5.png)

It is important to notice that some of the models doesn't have dropout since we realized that by adding dropout the performance was worst in each case.

## Removing classes

After running number of experiments, we decided to remove 2 classes, which were **kicknt**, and **punchnt**. These 2 classes were so similar to our **kick**, **punch**, so the training of the models could be confused by the similutedes of the 4 classes. The dataset can be found in [Roboflow Universe](https://universe.roboflow.com/georgebrown/punch-and-kick-image-classification)

In order to run the experiments with the same models, we decided to train the models with similar condtions; however, for these experiments we included a dropout of 0.5. So, with these three models and 2 classes we got the following results:

- VGG16 with 50.178 trainable parameters and 14.764.866 total parameters, ![VGG16](/images/image.png)
- ResNet50V2 with 200.706 trainable parameters and 23.756.506 total params ![ResNet50V2](/images/image-1.png)
- InceptionResNetV2 with 3.074 trainable parameters and 54.339.810 total params ![InceptionResNetV2](/images/image-2.png)

We can notice that the overal performance increase a 30% in average for the 3 models. Meaning that our assumptions about the 4 classes was right.

## Yolo V8

After noticing that we increased our models accuracy, we decided to have some experiments with [YoloV8n classify model](https://docs.ultralytics.com/tasks/classify/).

To have some fair experiments we tried with the 4 classes and 2 classes datasets.

Let's compare the results:

| YoloV8n 4 classes | YoloV8n 2 classes |
|---| --- |
| ![4 Classes](/yolo_results/4_classes_results.png) | ![4 Classes](/yolo_results/2_classes_results.png) |

In conclusion, we can say that we got better accuracy when using 2 classes and YoloV8 in the overal.
