from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"copying from {from_file} to {to_file}")

# we could do these two on one line, how?

print(f"""
The input file is {len(open(from_file).read())} bytes long")
Does the output file exist? {exists(to_file)}
Ready, hit RETURN to continue, CTRL-C to abort
""")
input()

out_file = open(to_file,'w').write(open(from_file).read())

print("Alright, all done.")

#out_file.close()
#in_file.close()
