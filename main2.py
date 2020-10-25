import json


def flatten_json(y):
    out = {}

    def flatten(x, name=''):

        # If the Nested key-value
        # pair is of dict type
        if type(x) is dict:

            for a in x:
                flatten(x[a], name + a + '_')

            # If the Nested key-value
        # pair is of list type
        elif type(x) is list:

            i = 0

            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

# Read json file and print
with open('mydata.json') as f:
  data = json.load(f)
  myflatdata = flatten_json(data)
  #print(myflatdata)
  for x in myflatdata:
      print("%s=%s" % (x, myflatdata[x]))


