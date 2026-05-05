---
title: "Small Steps 2 - Teaching a Neural Network to Learn the Letter A from B-Z"
url: "https://boyter.org/2010/09/small-steps-2-%E2%80%93-teaching-neural-network-learn-letter-b-z/"
fetched_at: 2026-05-05T07:02:07.574430+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Small Steps 2 - Teaching a Neural Network to Learn the Letter A from B-Z

Source: https://boyter.org/2010/09/small-steps-2-%E2%80%93-teaching-neural-network-learn-letter-b-z/

So in the previous article we managed to get our
neural network to learn the difference between A and B
. I mentioned at the end I was going to next test and teach it on various versions of A and B to see how effective it is, but rather then that I figured teaching a network to learn A from every other letter would be more interesting.
Get the source to everything below in
Step2
Now the code below is rather un-pythonic but it does show us loading each of the letters and then training the network to learn that an A is an A and that every other letter is not an A. I had initially tried to teach it how to recognise each letter however I found this resulted in a huge neural network which was slow to train. For the moment teaching the network what an A is should be fine for now.
import Loader

if **name** == '**main**':
  cla = Loader.Loader()

  hiddennodes = 3
  x = 5
  y = 5

  adata = cla.loadimagedata("./letters/A.gif",x,y)
  bdata = cla.loadimagedata("./letters/B.gif",x,y)
  cdata = cla.loadimagedata("./letters/C.gif",x,y)
  ddata = cla.loadimagedata("./letters/D.gif",x,y)
  edata = cla.loadimagedata("./letters/E.gif",x,y)
  fdata = cla.loadimagedata("./letters/F.gif",x,y)
  gdata = cla.loadimagedata("./letters/G.gif",x,y)
  hdata = cla.loadimagedata("./letters/H.gif",x,y)
  idata = cla.loadimagedata("./letters/I.gif",x,y)
  jdata = cla.loadimagedata("./letters/J.gif",x,y)
  kdata = cla.loadimagedata("./letters/K.gif",x,y)
  ldata = cla.loadimagedata("./letters/L.gif",x,y)
  mdata = cla.loadimagedata("./letters/M.gif",x,y)
  ndata = cla.loadimagedata("./letters/N.gif",x,y)
  odata = cla.loadimagedata("./letters/O.gif",x,y)
  pdata = cla.loadimagedata("./letters/P.gif",x,y)
  qdata = cla.loadimagedata("./letters/Q.gif",x,y)
  rdata = cla.loadimagedata("./letters/R.gif",x,y)
  sdata = cla.loadimagedata("./letters/S.gif",x,y)
  tdata = cla.loadimagedata("./letters/T.gif",x,y)
  udata = cla.loadimagedata("./letters/U.gif",x,y)
  vdata = cla.loadimagedata("./letters/V.gif",x,y)
  wdata = cla.loadimagedata("./letters/W.gif",x,y)
  xdata = cla.loadimagedata("./letters/X.gif",x,y)
  ydata = cla.loadimagedata("./letters/Y.gif",x,y)
  zdata = cla.loadimagedata("./letters/Z.gif",x,y)

  apat = [
    [adata,[1]],
    [bdata,[0]],
    [cdata,[0]],
    [ddata,[0]],
    [edata,[0]],
    [fdata,[0]],
    [gdata,[0]],
    [hdata,[0]],
    [idata,[0]],
    [jdata,[0]],
    [kdata,[0]],
    [ldata,[0]],
    [mdata,[0]],
    [ndata,[0]],
    [odata,[0]],
    [pdata,[0]],
    [qdata,[0]],
    [rdata,[0]],
    [sdata,[0]],
    [tdata,[0]],
    [udata,[0]],
    [vdata,[0]],
    [wdata,[0]],
    [xdata,[0]],
    [ydata,[0]],
    [zdata,[0]],
  ]

  an = bpnn.NN(len(adata),hiddennodes,1)
  an.train(apat)

  cla.savenn(an,filename='aznn.n')
Again like before what the above does is open up each of our sample images and then trains the network on them. I ended up playing around with the number of nodes and managed to get a low error rate with 25 inputs and 3 hidden nodes. This is interesting as the last network used 400 inputs and 3 hidden nodes, and at first I was skeptical if the network had learnt this pattern correctly.
Of course we need something to test the effectiveness of our network and so I created the below test script which should take care of this and should let us see if the network does work correctly.
import unittest
import Loader

class TestClassifyAfromB(unittest.TestCase):
  def setUp(self):
    self.c = Loader.Loader()
    self.x = 10
    self.y = 10

  def testLearnA(self):
    n = self.c.loadnn(filename='aznn.n')
    guess = n.guess(self.c.loadimagedata("./letters/A.gif",self.x,self.y))
    self.assertTrue(guess[0] &gt; 0.95)

  def testLearnB(self):
    n = self.c.loadnn(filename='aznn.n')
    guess = n.guess(self.c.loadimagedata("./letters/B.gif",self.x,self.y))
    self.assertTrue(guess[0] &lt; 0.05)

  def testLearnC(self):
    n = self.c.loadnn(filename='aznn.n')
    for let in 'B2 B3 C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(' '):
      guess = n.guess(self.c.loadimagedata("./letters/%s.gif"%(let),self.x,self.y))
      self.assertTrue(guess[0] &lt; 0.05)

if **name** == '**main**':
  unittest.main()
The above is just a quick and dirty test and the results of which are,
$python TestStep2.py
...
----------------------------------------------------------------------

Ran 3 tests in 0.015s

OK
All good! The next goal is to build a large sample of different letters in different fonts and get the network to pick out the letter A from many examples. This will indicate that it has learnt the pattern of what an A looks like rather then the letter A as given in the above examples.
