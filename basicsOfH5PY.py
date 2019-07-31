import numpy as np
import h5py as hpy

# h5py -- mainly 3 things -- file / groups / datasets

# 1. file

m1=np.random.random(size=(1000,100))
m2=np.random.random(size=(100,10000))

with hpy.File('data_h5py.h5','w') as hdf:
    hdf.create_dataset('data_1',data=m1)   # h5py crates a dict with key = name of dataset & value = dataset
    hdf.create_dataset('data_2',data=m2)
# file will be autoclose when we move out of the above block

with hpy.File('data_h5py.h5','r') as hdf:
    ls=list(hdf.keys()) # list of all datasets
    print('list of data sets',ls)
    data=hdf.get('data_1')
    data=np.array(data)
    print(data)
    print(data.shape)

# another method -- but here we've to manually close the file
f=hpy.File('data_h5py.h5','r')
print(list(f.keys()))
f.close()


# 2. groups - groups of datasets
m3=np.random.random(size=(1000,100))
m4=np.random.random(size=(1000,100))

with hpy.File('data2_h5py.py','w') as hdf:
    g1=hdf.create_group('group1')
    g1.create_dataset('data1',data=m1)
    g1.create_dataset('data4',data=m4)

    g2=hdf.create_group('group2/subgroup1')
    g2.create_dataset('data2',data=m2)
    g2.create_dataset('data3',data=m3)

    g2=hdf.create_group('group2/subgroup2')
    g2.create_dataset('data1',data=m1)
    g2.create_dataset('data3',data=m3)

with hpy.File('data2_h5py.py','r') as hdf:
    ls=list(hdf.items())  # list of all groups 
    print(ls)
    g1=hdf.get('group1') # to access datasets of g1 -- g1.get('dataset_name')
    print(list(g1.items())) # list of all datasets in group
    g2=hdf.get('group2') 
    print(list(g2.items())) # to access subgroups -- g2.get('subgroup_name')


# to compress the data -- hdf.create_dataset('data1',data=m2, compression='gzip', compression_opts=9)


# set the attributes -- think of them as dict -- a dict -- in which we can add our own attributes -- initially the dict would be empty
# to add attributes -- dataset.attrs['key'] = value
# we've to add these with creation of dataset -- we can't do it later

with hpy.File('data_h5py.py','w') as hdf:
    d3=hdf.create_dataset('data_3',data=m3)
    d3.attrs['class']='Data of Dogs'
    d3.attrs['version']=1.3

with hpy.File('data_h5py.py','r') as hdf:
    d3=hdf.get('data_3')
    print(list(d3.attrs.items()))
