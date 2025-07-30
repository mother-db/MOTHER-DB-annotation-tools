import datetime
import os

### JPS updated March 7, 2025

### NOTE: This parameters file is for a multiclass classifier, all the small follicles (Primordial -> Multilayer) 
###       have the SAME window_size

# Add all the follicle types
# Add window size, max offset (decimal fraction of the window)
# User to decide which follicle type to use
# Create a folder with the code and the timestamp. (Now the folder name is comapatable with Windows)

### Reference set of data
'''
types = {"Primordial":              {'coordinates':[], 'window_size': 100,  'offset':150*0.10}, 
         "Transitional Primordial": {'coordinates':[], 'window_size': 150,  'offset':150*0.10}, 
         "Primary":                 {'coordinates':[], 'window_size': 150,  'offset':150*0.10}, 
         "Transitional Primary":    {'coordinates':[], 'window_size': 150,  'offset':150*0.10}, 
         "Secondary":               {'coordinates':[], 'window_size': 150,  'offset':150*0.10}, 
         "Multilayer":              {'coordinates':[], 'window_size': 150,  'offset':150*0.10},
         "Atretic Antral":          {'coordinates':[], 'window_size': 1800, 'offset':1800*0.10}, 
         "Antral":                  {'coordinates':[], 'window_size': 1800, 'offset':1800*0.10}}
'''

# List of MOTHER follicle types and window sizes

types = {"Primordial":              {'coordinates':[], 'window_size': 200,  'offset':200 * 0.10}, 
         "Transitional Primordial": {'coordinates':[], 'window_size': 200,  'offset':200 * 0.10}, 
         "Primary":                 {'coordinates':[], 'window_size': 200,  'offset':200 * 0.10}, 
         "Transitional Primary":    {'coordinates':[], 'window_size': 200,  'offset':200 * 0.10}, 
         "Secondary":               {'coordinates':[], 'window_size': 200,  'offset':200 * 0.10}, 
         "Multilayer":              {'coordinates':[], 'window_size': 200,  'offset':200 * 0.10}}


'''
types = {"Atretic Antral": {"coordinates": [], "window_size": 1800, "offset": 1800 * 0.10},
         "Antral":         {"coordinates": [], "window_size": 1800, "offset": 1800 * 0.10}}
'''

# Create list of files to be processed
# March 2025: there are a total of 18 annotated data sets
### JPS, added the "../" to the paths for my local runs

###file_base = "../../../Data/Original/" #Relative or absolute path to the folder containing the image files
file_base = "./TrainingData_20250409/" #Relative or absolute path to the folder containing the image files

print(os.getcwd())
print("file_base:\n",file_base)

# original file list is further down in this file, this shortened list is for testing
'''
file_list = [
             {'Image path':      file_base + '30381_RT_200c.ome.tif',
              'Annotation path': file_base + '30381_RT_200c.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '21930_LT_060a.ome.tif',
              'Annotation path': file_base + '21930_LT_060a_annotationsTable.txt',
              'Resolution': 0.69},
            ]

'''
file_list = [{'Image path':      file_base + '14736_UN_050a.ome.tif',
              'Annotation path': file_base + '14736_UN_050a.annotations.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '16418_UN_140b.ome.tif',
              'Annotation path': file_base + '16418_UN_140b.annotations.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '19006_UN_020a.ome.tif',
              'Annotation path': file_base + '19006_UN_020a.annotations.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '25058_LT_005a.ome.tif',
              'Annotation path': file_base + '25058_LT_005a.annotations.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '25065_LT_010a.ome.tif',
              'Annotation path': file_base + '25065_LT_010a.annotations.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '25081_LT_010a.ome.tif',
              'Annotation path': file_base + '25081_LT_010a.annotations.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '27570_UN_110a.ome.tif',
              'Annotation path': file_base + '27570_UN_110a.annotations.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '30381_RT_070b.ome.tif',
              'Annotation path': file_base + '30381_RT_070b.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '30381_RT_140b.ome.tif',
              'Annotation path': file_base + '30381_RT_140b.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '30381_RT_200c.ome.tif',
              'Annotation path': file_base + '30381_RT_200c.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '32002_RT_050a.ome.tif',
              'Annotation path': file_base + '32002_RT_050a.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '32002_RT_110b.ome.tif',
              'Annotation path': file_base + '32002_RT_110b.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '32002_RT_160c.ome.tif',
              'Annotation path': file_base + '32002_RT_160c.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '33564_RT_060a.ome.tif',
              'Annotation path': file_base + '33564_RT_060a.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '33564_RT_120b.ome.tif',
              'Annotation path': file_base + '33564_RT_120b.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '33564_RT_180b.ome.tif',
              'Annotation path': file_base + '33564_RT_180b.ome.annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '21930_LT_060a.ome.tif',
              'Annotation path': file_base + '21930_LT_060a_annotationsTable.txt',
              'Resolution': 0.69},
             {'Image path':      file_base + '21930_LT_120b.ome.tif',
              'Annotation path': file_base + '21930_LT_120b_annotationsTable.txt',
              'Resolution': 0.69},
            ]


# List of angles to rotate subimages, for data augmentation (zero is done by default)
angles = [90,180,270]


# Function to ask user for follicle type to process. For "hotdog-not-a-hotdog" single class classifiers
def prediction_follicle():
    print('Choose a follicle type from:\n   ',types.keys(),'\nor "Multiple"')
    flag = True
    default_type = 'Primordial'
    default_type = 'Multiple'
    while flag:
        follicle_type = input(f"Enter the type of follicle for the model[default="+default_type+"]:") or default_type
        if follicle_type in types.keys() or follicle_type == "Multiple":
            flag = False
        else:
            print("Input incorrect, try again")
    print('\nprediction_follicle type = ',follicle_type)
    return follicle_type

# Create a folder using the follicle type being processed and a time stamp
# can also create other time stamped folders by passing in some other string instead of a follicle_type
def create_folder(follicle_type):
    #now = datetime.datetime.now().strftime("%H:%M:%S %m-%d-%y")  # jps, not compatable with Windows file names
    #now = datetime.datetime.now().strftime("%H_%M_%S %m-%d-%y")  
    now = datetime.datetime.now().strftime("%y-%m-%d__%H_%M_%S" )  # jps, put date first so it sorts properly
    file_name = follicle_type + '_' + now
    os.mkdir(file_name)

    return file_name