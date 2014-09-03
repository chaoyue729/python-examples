""" https://docs.python.org/2/library/pickle.html
    Pickle module implements an algorithm for serializing and deserializing
    a Python object structure.  'Pickling' is the process where a Python
    object hierarchy is converted into a byte stream and 'unpickling' is the
    reverse.  Also known as 'serialization', 'marshalling', or 'flattening'

    Note: if you need fast pickling, use the C version (cPickle), slightly
    different, but
    Marshal is similar (more primitive), but should always prefer Pickle instead
"""

import pickle

def pickle_dump_example(data_to_pickle, filename):
    print "Pickling an object: ", data_to_pickle
    fileObject = open(filename, 'wb')  # Open the file for writing
    pickle.dump(a, fileObject) # Pickle the fileobject
    fileObject.close()  # Close the fileObject

    print "Loading a pickled object:"
    fileObject = open(filename, 'r')  # Open the file for reading
    b = pickle.load(fileObject)  # Load the pickled object
    print b

if __name__ == '__main__':

    a = ['test value', 'test value 2', 'test value 3']  # Data that you want to pickle
    pickle_dump_example(a, 'testfile')