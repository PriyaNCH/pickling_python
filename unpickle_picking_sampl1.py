import pickle, pprint

pkl_file = open('data.pk1','rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()

with open('data.pk2','rb') as f:
    unpickled_data = pickle.load(f)
    print(unpickled_data)
    
with open('data.pk2','rb') as f:
    data = pickle.load(f)
    print(data)