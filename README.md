# motion-identifier

## Data
   https://www.kaggle.com/c/state-farm-distracted-driver-detection/data

## Objective
   Given driver pictures, identified the action of the driver.

## Methodology
   There are 10 labels associated with these pictures.
   c0: safe driving
   c1: texting - right
   c2: talking on the phone - right
   c3: texting - left
   c4: talking on the phone - left
   c5: operating the radio
   c6: drinking
   c7: reaching behind
   c8: hair and makeup
   c9: talking to passenger
   The goal is to identify a given picture with one of this label. This is a classical image classification
   problem. CNN will be a good choice for this problem. The idea is to train the CNN so when given a new
   picture, the model can correctly classify the action the drive is doing(aka label).
