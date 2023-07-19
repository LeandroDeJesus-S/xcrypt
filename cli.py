from argparse import ArgumentParser
from xcrypt import Encryper

from help_msgs import *

encrypter = Encryper()
arg = ArgumentParser(usage=PROGRAM_USAGE)

arg.add_argument('command')

# key gen
arg.add_argument('-o', nargs=1, type=str, dest='output_keyfile', default=False, 
                 help=OUTPUT_KEYFILE_MSG, metavar='<keyfile_path>')

arg.add_argument('-v', action='store_true', dest='view_key', help=VIEWKEY_MSG)

# encrypt and decrypt
arg.add_argument('-d', nargs=1, type=str, dest='directory', default=False, 
                 help=DIRECTORY_MSG, metavar='<dir_path>')

arg.add_argument('-f', nargs=1, type=str, dest='file', default=False,
                 help=FILE_MSG, metavar='<file_path>')

arg.add_argument('--ignore-suffix', nargs=1, type=str, dest='ignored_suffix', 
                 default=False, help=IGNORE_SUFFIX_MSG, metavar='<suffix>')

cmmd = arg.parse_args()

arg_value = lambda x: x if not x else x[0]

COMMAND = cmmd.command

o_command = cmmd.output_keyfile
OUTPUT_KEYFILE = arg_value(o_command)
VIEW_KEY = cmmd.view_key

DIRECTORY = arg_value(cmmd.directory)
FILE = arg_value(cmmd.file)
IGNORED_SUFFIX = arg_value(cmmd.ignored_suffix)


def key_gen_cmd():
    global OUTPUT_KEYFILE, VIEW_KEY, encrypter

    if not OUTPUT_KEYFILE:
        key = encrypter.generate_key()
    else:
        encrypter.key_file_path = OUTPUT_KEYFILE
        key = encrypter.generate_key()
        
    if VIEW_KEY:
        print(key)


def encrypt_cmd():
    global DIRECTORY, encrypter, IGNORED_SUFFIX
    
    key = input('Keypass: ')
    if DIRECTORY:
        encrypter.encrypt_directory(DIRECTORY, key, ignore_suffix=IGNORED_SUFFIX)
    
    elif FILE:
        encrypter.encrypt_file(FILE, key)


def decrypt_cmd():
    global DIRECTORY, FILE, encrypter
    
    key = input('Keypass: ')
    if DIRECTORY:
        encrypter.decrypt_directory(DIRECTORY, key)
    
    elif FILE:
        encrypter.decrypt_file(FILE, key)


if cmmd.command == 'key-gen':
    key_gen_cmd()
    
elif cmmd.command == 'encrypt':
    encrypt_cmd()

elif cmmd.command == 'decrypt':
    decrypt_cmd()
