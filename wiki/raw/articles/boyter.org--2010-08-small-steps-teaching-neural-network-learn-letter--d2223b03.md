---
title: "Small Steps 1 - Teaching a Neural Network to Learn the Letter A from B"
url: "https://boyter.org/2010/08/small-steps-teaching-neural-network-learn-letter/"
fetched_at: 2026-05-05T07:02:07.654640+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Small Steps 1 - Teaching a Neural Network to Learn the Letter A from B

Source: https://boyter.org/2010/08/small-steps-teaching-neural-network-learn-letter/

I’m going to make the assumption that if you are reading this you already know what a NN is, and you are trying to do some sort of image recognition. I’m also going to assume you are somewhat familiar with programming preferably in Python since that’s what all the examples will be using.
Get the source to everything below in
Step1.zip
To get started we are going to need the following,
A neural network implementation
A imaging library to read images
Sample images to train and test on.
The images we are going to use are the following,
The Letter A - image lost to time
The Letter B - image lost to time
Our goal is to teach a neural network to tell the difference between the above. There are two ways we can look at feeding data into our network. The first is to just convert each of the pixels in the image into an input. So for a 10×10 image you would need 100 input neurons. The second is to try and describe what the letter looks like. This can mean describing the thickness of lines at various cut points etc…
The first is the easiest to code so I am going to go with that. The first thing we need is a way to open the image and convert it to a list of data. I am going to just iterate over each row and for each pixel that’s black add a 1 to a list otherwise a 0. I also added some methods to save and load the network to disk.
The next step is to write some code which takes the above pixel data and feeds it into the Neural Network.
import bpnn
import Loader

if **name** == '**main**':
  cla = Loader.Loader()
  hiddennodes = 2

  adata = cla.loadimagedata("./letters/A.gif",xsize=20,ysize=20)
  bdata = cla.loadimagedata("./letters/B.gif",xsize=20,ysize=20)
  apat = [
    [adata,[1,0]],
    [bdata,[0,1]],
  ]

  an = bpnn.NN(len(adata),hiddennodes,len(apat[0][1]))
  an.train(apat)
  cla.savenn(an,filename='abnn.n')
You can see that in the above we create a loader object which allows us to read images and networks. We then load our data, put it into the correct pattern for our Neural Network to train on, then train it and save the network.
The important thing to look at here is the number of hiddennodes. This is something you will have to play with in order to make your network efficient. I have set it to 2 for the moment.
Now running the above code we get the following,
$python Step1.py
error 4.42059
error 0.71834
error 0.71834
error 0.71834
error 0.71834
error 0.71834
error 0.71834
error 0.71834
error 0.71834
error 0.71834
What the above shows is the network learning. The important thing is that the error continues to decrease. In this case it lowers a bit, then stops. The reason for this can could be one of the following,
Not enough hidden nodes – So not enough memory to “learn” the difference
Not enough training time – Unlikely since the error isn’t decreasing
Not enough inputs – Unlikely since we have 400 inputs but is possible
To remedy this I have increased the number of hidden nodes to 3 to increase the learning power of the network and then run it again.
$python Step1.py
error 2.93246
error 0.00048
error 0.00023
error 0.00015
error 0.00012
error 0.00010
error 0.00008
error 0.00007
error 0.00006
error 0.00006
This is much better! The error continues to decrease and almost reaches 0. This means that our network has learnt the difference between our sample letter A and B.
We can test this pretty easily with the following test script which uses unit tests to ensure we don’t break the network in the future
import unittest
import Loader

class TestStep1(unittest.TestCase):
  def setUp(self):
    self.c = Loader.Loader()

  def testLearnA(self):
    n = self.c.loadnn(filename='abnn.n')
    guess = n.guess(self.c.loadimagedata("./letters/A.gif",20,20))
    self.assertTrue(guess[0] > 0.95)
    self.assertTrue(guess[1] &lt; 0.05)

  def testLearnB(self):
    n = self.c.loadnn(filename='abnn.n')
    guess = n.guess(self.c.loadimagedata("./letters/B.gif",20,20))
    self.assertTrue(guess[1] > 0.95)
    self.assertTrue(guess[0] &lt; 0.05)

if **name** == '**main**':
  unittest.main()
Running this gives,
$python TestStep1.py

----------------------------------------------------------------------

Ran 2 tests in 0.031s

OK
Looks like all is well. The next step and what will be in the next blog post is training our network so that it can identify from characters it has never seen before.
