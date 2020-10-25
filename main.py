
from json_flatten import flatten
import json

# Print json object as flattened one
unflat_json = {'user' :
			{'Rachel':
				{'UserID':1717171717,
				'Email': 'rachel1999@gmail.com',
				'friends': ['John', 'Jeremy', 'Emily']
				}
			}
			}
flat_json = flatten(unflat_json)
print(flat_json)

#Read a json file and print as flattened one
with open('mydata.json') as f:
  data = json.load(f)
  myflatdata = flatten(data)
  print(myflatdata);

  # write to a file
  with open("flatten_file.json", "w") as write_file:
	  json.dump(myflatdata, write_file)

  #print each property separate with = intead of : and quotoes and as a property
  for x in myflatdata:
	  print("%s=%s" % (x, myflatdata[x]))


  # Write json as properties to a file
  file1 = open("myfile.txt", "w")  # write mode
  for x in myflatdata:
	  file1.writelines("%s=%s" % (x, myflatdata[x]))
	  file1.writelines("\n")
  file1.close()

