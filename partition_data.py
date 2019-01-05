import os
from random import shuffle
import shutil


def overwrite_dir(dir_path):
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.makedirs(dir_path)


def copy_files(src_path, dst_path, files, extension="jpg"):
    for f_name in files:
        ext_name = f_name[:-3] + extension
        src = src_path + ext_name
        dst = dst_path + ext_name

        if os.path.exists(src):
            shutil.copy(src, dst)



def get_common_files(base_path):
    # Get all class files
    path = base_path
    imgs_path = base_path + "images/"
    texts_path = base_path + "text/"

    img_files = [f[:-3] for f in os.listdir(imgs_path)]
    text_files = [f[:-3] for f in os.listdir(texts_path)]

    return list(set(img_files) & set(text_files))





data_path = ""
classes = ["damaged_infrastructure", "damaged_nature", "fires", "flood", "human_damage", "non_damage"]

imgs_path = ""
texts_path = ""
combined_path = ""

# Re-create the parent directories
overwrite_dir(imgs_path)
overwrite_dir(texts_path)
overwrite_dir(combined_path)

# Create image sub-directores
os.makedirs(imgs_path+"/train")
os.makedirs(imgs_path+"/val")
os.makedirs(imgs_path+"/output")

# Create text sub-directories
os.makedirs(texts_path+"/train")
os.makedirs(texts_path+"/val")

# Create image sub-directores
os.makedirs(combined_path+"/train")
os.makedirs(combined_path+"/val")
os.makedirs(combined_path+"/test")
os.makedirs(combined_path+"/models")


print("Parent folders setup successfully...")


test_percentage = 0.2
train_percentage = 0.85
val_percentage = 0.15


for label_class in classes:

    print("Processing class: ", label_class)

    # Make a more balanced dataset
    if label_class == "non_damage":
        n_files = 1200
    elif label_class == "human_damage":
        n_files = 240
    else:
        n_files = 300


    # Get files appearing in both directories
    path = data_path + "/" + label_class + "/"
    files = [f + 'jpg' for f in get_common_files(path)]
    shuffle(files)
    files = files[:n_files]

    # Create output image directories
    os.makedirs(imgs_path + "/train/" + label_class)
    os.makedirs(imgs_path + "/val/" + label_class)
    os.makedirs(texts_path + "/train/" + label_class)
    os.makedirs(texts_path + "/val/" + label_class)
    os.makedirs(combined_path + "/train/" + label_class)
    os.makedirs(combined_path + "/val/" + label_class)
    os.makedirs(combined_path + "/test/" + label_class)
    os.makedirs(combined_path + "/train/" + label_class + "/images")
    os.makedirs(combined_path + "/val/" + label_class + "/images")
    os.makedirs(combined_path + "/test/" + label_class + "/images")
    os.makedirs(combined_path + "/train/" + label_class + "/text")
    os.makedirs(combined_path + "/val/" + label_class + "/text")
    os.makedirs(combined_path + "/test/" + label_class + "/text")

    # Compute sizes of training, testing and validation sets
    n_files = len(files)
    n_tests = int(n_files * test_percentage)
    n_train = int((n_files - n_tests) * train_percentage)
    n_val = n_files - n_tests - n_train

    # Randomly shuffle the files
    shuffle(files)

    # Copy over image files
    test_files = files[0:n_tests]
    train_files = files[n_tests:n_tests+n_train]
    val_files = files[n_tests+n_train:]

    src_path = data_path + "/" + label_class + "/images/"

    dst_path = imgs_path + "/train/" + label_class + "/"
    copy_files(src_path, dst_path, train_files)

    dst_path = imgs_path + "/val/" + label_class + "/"
    copy_files(src_path, dst_path, val_files)


    dst_path = combined_path + "/val/" + label_class + "/images/"
    copy_files(src_path, dst_path, val_files)

    dst_path = combined_path + "/train/" + label_class + "/images/"
    copy_files(src_path, dst_path, train_files)

    dst_path = combined_path + "/test/" + label_class + "/images/"
    copy_files(src_path, dst_path, test_files)



    # Copy over text files
    # Validation is done by the code itself, so merge the training and validation files
    src_path = data_path + "/" + label_class + "/text/"

    dst_path = texts_path + "/train/" + label_class + "/"
    copy_files(src_path, dst_path, train_files, "txt")

    dst_path = texts_path + "/val/" + label_class + "/"
    copy_files(src_path, dst_path, val_files, "txt")

    dst_path = combined_path + "/val/" + label_class + "/text/"
    copy_files(src_path, dst_path, val_files, "txt")

    dst_path = combined_path + "/train/" + label_class + "/text/"
    copy_files(src_path, dst_path, train_files, "txt")

    dst_path = combined_path + "/test/" + label_class + "/text/"
    copy_files(src_path, dst_path, test_files, "txt")






