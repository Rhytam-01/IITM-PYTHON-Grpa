'''You are given certain details of the trains that stop at a station. Your task is to store these details in a nested dictionary.

The first line of input is n, the number of trains that stop at the station.n blocks of input follow. The first line in each block corresponds to the train name. 
The second line in each block corresponds to m, the number of compartments in the train. m lines of input follow. Each of these m lines has two values separated by 
a comma: name of the compartment and number of passengers in it.

Your task is to create a nested dictionary named station_dict. The keys of the dictionary are train names, the value corresponding to a key is another dictionary. The 
keys of the inner dictionary are the compartment names in this train, the values are the number of passengers in each compartment. For example:

{
    'Mumbai Express': {
        'S1': 10,
        'S2': 20,
        'S3': 30
    },
    'Chennai Express': {
        'S1': 10,
        'S2': 20,
        'S3': 30
    }
  }

(1) The values of the compartments should be represented as integers and not as strings.
(2) You do not have to print the output to the console. Do not try to print the output that you observe in the "Expected Output". You just have to process the input 
andcreate the dictionary station_dict'''
