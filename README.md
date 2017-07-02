# motion-identifier

## Data
   https://www.kaggle.com/c/state-farm-distracted-driver-detection/data

## Objective
   Given driver pictures, identified the action of the driver.

## Methodology
   * There are 10 labels associated with these pictures.
   * c0: safe driving
   * c1: texting - right
   * c2: talking on the phone - right
   * c3: texting - left
   * c4: talking on the phone - left
   * c5: operating the radio
   * c6: drinking
   * c7: reaching behind
   * c8: hair and makeup
   * c9: talking to passenger
   * The goal is to identify a given picture with one of this label. This is a classical image classification
   problem. CNN will be a good choice for this problem. The idea is to train the CNN so when given a new
   picture, the model can correctly classify the action the drive is doing(aka label).

## Result
   I have used the K-Nearest Neighbor as my base case model. I randomly choose 800 pictures
   and fitted the model. I predicted another 200 pictures with the model and see an accuracy
   of around 65%. This is actually surprisingly good given a very simple model. This dataset
   has 22000+ pictures, I use the ResNet50 as a feature extraction model. At the end of the
   ResNet I added a Dense layer to collapse the result to 10 classes. I froze all the ResNet
   layers and only train the newly added Dense layer. After two epochs, the validation accuracy
   is already up to 99%. So there is no need to continue training. This competition also gives
   a huge number of pictures without labels as the testing set. I have build an interactive
   tool to test this pictures. 
