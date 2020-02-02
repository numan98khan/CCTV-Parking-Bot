import pickle

obj = []

# Getting back the objects:
# file = open(filename, encoding="utf8")

with open('objs.pkl', 'rb') as f:  # Python 3: open(..., 'rb')
    obj = pickle.load(f)

print(obj)