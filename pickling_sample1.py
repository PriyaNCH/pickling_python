import pickle

data1 = {'a':  [1, 2.0, 3, 4+6j],
         'b': [('string', u'Unicode String')],
         'c': None }

print(pickle.HIGHEST_PROTOCOL)
selfref_list = [1,2,3]
selfref_list.append(selfref_list)

output = open('data.pk2','wb')

pickle.dump(data1, output)

pickle.dump(selfref_list, output, 2)

output.close()

