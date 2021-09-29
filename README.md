# MPhil_Project
# Abstract
Incidents that occur with the ATMs have become a significant problem whose rampant growth
has deeply affected the global delivery of financial institutions. In addition to financial losses
incurred, clients who patronize ATMs for financial transactions suffer a downtime experience
because service providers cannot detect incidents at the onset. ATM incidents are committed
through users of ATMs and its operations. The need to develop a Self-Reporting System for
ATM Incident Detection (SRSAID) for accurate, automated incidents detection processing to
offset downtime experience faced by the Banks and users of the ATMs cannot be overstated.
This paper utilized the ATM tampering images and the 2018 ATM system defects incidents
dataset obtained from the internet and NCR in Ghana, respectively, for detecting incidents. RCNN and support vector machines (SVM) which were fine-tuned by regression model and
optuna respectively, which are algorithms that provide the automatic detection of incidents and
periodic updates on the dashboard is used through the implementation of Python 3 on raspberry
pi along with hardware modules such as GPS and GSM modules. With the security aspect of
this study, the experimental results have proven that the R-CNN possessed better security
incident detection and classification performance when applied. Two (2) CNN architectures
were evaluated for the security aspect of the incidents and their performance compared.
Experimental results for security incident detection show ATM security incidents detection
classification accuracy via the CNN architectures, the two CNN architectures (ALEXNET
(80%) and ssdlite_mobilenet_V2 (96%). With the defect detection aspect of this study, the
experimental results have proven that the SVM possessed better detection and classification
performance when applied using SVM kernel classifiers. Initially, three SVM classifiers were
evaluated as linear (70.6%), polynomial (72.56%), and radial basis function (RBF) kernelv
(81.21%). Based on the results obtained, there was a need to improve the accuracy of the SVM
classifiers. An efficient hyperparameter optimization technique was adopted to optimize the
SVM model, and their results were compared for the defects aspect of incident detection.
Experimental results show a significant reduction in computational time on ATM system defect
incidents detection processing while increasing classification accuracy via the various SVM
classifiers (linear (76%), polynomial (77%), and radial basis function (RBF) kernel (86%).
Extensive testing of machine learning algorithms and their performance metrics yielded
promising results. A Graphical User Interface (GUI) to enable an analysis of incidents was
incorporated to allow decision-making to overcome downtime experience.

This repository contains all the source codes for Ivy Nkrumah Payne MPhil Project on the topic Self-reporting System for ATM Incidents Detection.

