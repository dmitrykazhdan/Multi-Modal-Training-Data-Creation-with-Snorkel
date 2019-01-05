import os

'''
Combined code for running all of the models one after the other.
See https://github.com/husseinmouzannar/multimodal-deep-learning-for-disaster-response for more info 
'''



#------------------------------------------------Data Pre-Processing--------------------------------------------------

build_img_data_path = ''
train_dir = ''
val_dir = ''
labels_file = ''
output_dir = ''

os.system('python3 ' + build_img_data_path +
          ' --train_directory=' + train_dir +
          ' --validation_directory=' + val_dir +
          ' --labels_file=' + labels_file +
          ' --output_directory=' + output_dir)

print('Dataset converted to TFRecords')


#---------------------------------------------Unimodal Image Model Training---------------------------------------------

max_number_of_steps = 200
train_image_classifier_path = ''
train_dir = ''
dataset_dir=''
dataset_name=''
dataset_split_name=''
model_name=''
checkpoint_path=''


# Delete previous model checkpoint
os.system('python3 ' + train_image_classifier_path +
          ' --max_number_of_steps=' + str(max_number_of_steps) +
          ' --train_dir=' + train_dir +
          ' --dataset_dir=' + dataset_dir +
          ' --dataset_name=' + dataset_name +
          ' --dataset_split_name=' + dataset_split_name +
          ' --model_name=' + model_name +
          ' --checkpoint_path=' + checkpoint_path +
          ' --checkpoint_exclude_scopes=InceptionV3/Logits,InceptionV3/AuxLogits '
          ' --trainable_scopes=InceptionV3/Logits,InceptionV3/AuxLogits')

print('Image classifier trained')


inf_graph_path = ''
output_file = ''

os.system('python3 ' + inf_graph_path +
          ' --alsologtostderr '
          ' --model_name=inception_v3 '
          ' --output_file=' + output_file)


print('Inference graph exported')


freeze_graph_path = ''
input_graph=''
input_checkpoint=''
output_graph=''

os.system('python3 ' + freeze_graph_path +
         ' --input_graph=' + input_graph +
         ' --input_checkpoint=' + input_checkpoint +
         ' --input_binary=true '
         ' --output_graph=' + output_graph +
         ' --output_node_names=InceptionV3/Predictions/Reshape_1')


print('Image inference graph frozen successfully...')



#---------------------------------------------Unimodal Text Model Training----------------------------------------------

train_path=''

# Configure the 'config.yml' file first
os.system('python3 ' + train_path)
print('Training the text model...')




#---------------------------------------Text and Image Representation Extraction----------------------------------------

load_data_text_path = ''
load_data_image_path = ''

# Set parameters in the 'loadDataText' file
# Set checkpoint value
os.system('python3 ' + load_data_text_path)
print('Text representations retrieved...')


# Set parameters in the 'loadDataImage' file
os.system('python3 ' + load_data_image_path)
print('Image representations retrieved...')



#-----------------------------------------MultiModal Model Training + Testing-------------------------------------------

ann_features_path = ''

# Set parameters in the 'annFeatures' file
os.system('python3 ' + ann_features_path)
print('Training, Validating and Testing the MultiModal model...')

