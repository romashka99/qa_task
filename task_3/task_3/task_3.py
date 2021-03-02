import hashlib

from sys import argv

def get_hash(filename, hash_mode):
    with open(filename, 'rb') as file:
        mode = None
        if hash_mode == 'md5':
            mode = hashlib.md5()
        if hash_mode == 'sha1':
            mode = hashlib.sha1()
        if hash_mode == 'sha256':
            mode = hashlib.sha256()
        if mode:
            while True:
                data = file.read(8192)
                if not data:
                    break
                mode.update(data)
            return mode.hexdigest()
        else:
            return None

file_name = argv[1]
path = argv[2]

file_data = open(file_name, 'r')

for file in file_data:
    data = file.split(' ')
    if len(data) == 3:
        try:
            if get_hash(path + data[0], data[1]) == data[2]:
                print('{0} OK'.format(data[0]))
            else:
                print('{0} FAIL'.format(data[0]))
        except IOError:
            print('{0} NOT FOUND'.format(data[0]))
    else:
        print('{0} FAIL'.format(data[0]))