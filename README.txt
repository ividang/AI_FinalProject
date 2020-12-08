BabySitterAI team: Dang Vi, Do Phuong, Tran Phuc

SUBMITTING FILE             AUTHOR              DESCRIPTION
----------------------------------------------------------------------------------------
Revised schedule	   Vi Dang	   Summary of what we've achieved/learned
					   and troubles we've facing.
					   Revised schedule for checkpoint2 & completion
----------------------------------------------------------------------------------------

BabysistterAI.ipynb
  - Block 1:              Phuong Do,        Find and add required library
                          Vi Dang,            and set up the environment
                          Phuc Tran

  - Block 2:              Phuong Do,       Preprocessing images and load
                                              from train to validation folder.

  - Block 3-6:            Phuc Tran        Load data, reprocessing for the labels,
                                            denormalize then and convert them to numpy.

  - Block 6-13            Phuc Tran        Building AlexNet model construction.


  - Block 14              Vi Dang          Predicting testing images

Note: 
The code is authored by Uysim a developer who contributed his work on Kaggle [4]. In the
source code he used CNN model. However, we will use his code as reference and will update
his model using AlexNet. At this moment, the code is still in developing, therefore, there
are a lot of errors that need to fix.

Requirement to run the code:
You can use GoogleColab to run the code.
If you want to run the BabysistterAI.ipynb, you will need to install the following library:
1. Keras
2. Numpy
3. Pandas
4. Matplotlib
5. Pillow

And you also need Jupyter Notebook to run the program.

----------------------------------------------------------------------------------------
Dataset:
  - Training images
    Unsafe-Data           Vi Dang          This training set is for unsafe position
    + Climbing                               of different children
    + Face down
    + Standing

    Safe-Data             Phuong Do         This training set is for safe position
    + Sitting up                             of different children
    + Face up

  - Testing images        Vi Dang            This is a combination of un-labeled
                          Phuong Do             images of children for testing purpose

--------------------------------------------------------------------------------
Citation: Our team has looked up and study from different sources on Internet. Below
          are the websites that we are currently focused on.

    [1] https://nbviewer.jupyter.org/github/KushajveerSingh/Deep-Learning-Notebooks/blob/master/Blog%20Posts%20Notebooks/Training%20AlexNet%20with%20tips%20and%20checks%20on%20how%20to%20train%20CNNs/%281%29.ipynb
    [2] https://medium.com/@kushajreal/training-alexnet-with-tips-and-checks-on-how-to-train-cnns-practical-cnns-in-pytorch-1-61daa679c74a
    [3] https://towardsdatascience.com/how-to-train-an-image-classifier-in-pytorch-and-use-it-to-perform-basic-inference-on-single-images-99465a1e9bf5
    [4] https://www.kaggle.com/uysimty/keras-cnn-dog-or-cat-classification
