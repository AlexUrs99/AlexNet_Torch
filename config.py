# Copyright 2022 Dakewe Biotech Corporation. All Rights Reserved.
# Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import random

import numpy as np
import torch
from torch.backends import cudnn

# Random seed to maintain reproducible results
random.seed(0)
torch.manual_seed(0)
np.random.seed(0)
# Use GPU for training by default
device = torch.device("cuda", 0)
# Turning on when the image size does not change during training can speed up training
cudnn.benchmark = True
# Model arch name
model_arch_name = "alexnet"
# Model number class
model_num_classes = 1000
# Current configuration parameter method
mode = "train"
# Experiment name, easy to save weights and log files
exp_name = f"{model_arch_name.upper()}-ImageNet_1K"

if mode == "train": ## If we are currently training the model
    # Dataset address
    train_image_dir = "./data/ImageNet_1K/ILSVRC2012_img_train" ## Directory which contains images used for training
    valid_image_dir = "./data/ImageNet_1K/ILSVRC2012_img_val" ## Directory which contains images used for testing

    image_size = 224 ## Size of the images which will be fed to the model
    batch_size = 128 ## Number of images processed simultaneously during training 
    num_workers = 4 ## Number of processes used for loading the images into memory

    # The address to load the pretrained model
    pretrained_model_weights_path = "./results/pretrained_models/AlexNet-ImageNet_1K-9df8cd0f.pth.tar"

    # Incremental training and migration training
    resume = ""

    # Total num epochs
    epochs = 600 ## Number of iterations the dataset will pass through the NN
 
    # Loss parameters
    loss_label_smoothing = 0.1 ## undefined

    # Optimizer parameter
    model_lr = 0.5
    model_momentum = 0.9
    model_weight_decay = 2e-05
    model_ema_decay = 0.99998

    # Learning rate scheduler parameter
    lr_scheduler_T_0 = epochs // 4 ## undefined
    lr_scheduler_T_mult = 1 ## undefined
    lr_scheduler_eta_min = 5e-5 ## undefined

    # How many iterations to print the training/validate result
    train_print_frequency = 200 ## How often should metrics be printed (in epochs)
    valid_print_frequency = 20 ## How often should metrics be printed (in epochs)

if mode == "test":
    # Test data address
    test_image_dir = "./data/ImageNet_1K/ILSVRC2012_img_val"

    # Test dataloader parameters
    image_size = 224 ## Size of the images which will be fed to the model
    batch_size = 256 ## Number of images processed simultaneously during testing 
    num_workers = 4 ## Number of processes used for loading the images into memory

    # How many iterations to print the testing result
    test_print_frequency = 20 ## How often should metrics be printed (in epochs)

    model_weights_path = "./results/pretrained_models/AlexNet-ImageNet_1K-9df8cd0f.pth.tar"
