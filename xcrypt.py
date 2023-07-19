#!/usr/bin/env python
import os
from pathlib import Path
from cryptography.fernet  import Fernet


class Encryper:
    def __init__(self) -> None:
        self.key_file_path = Path(__file__).parent.absolute() / 'key.key'
        self.SUFFIX = '.encrypted'
    
    def generate_key(self) -> str:
        """Generate a keyfile with a passtoken
        
        Return:
            str: The generated key value
        """
        try:
            key = Fernet.generate_key()
            with open(self.key_file_path, 'wb') as f:
                f.write(key)
            
            return key
        
        except Exception as exc:
            print(exc)
            return ''

    def encrypt_file(self, filepath: str | Path, key: str | bytes) -> None:
        """Encrypt a file and delete
        
        Args:
            filepath (str | Path): the original file path
            key (str | bytes): the key to encrypt the file
        """
        try:
            mediator = Fernet(key)
            with open(filepath, 'rb') as f:
                original_content = f.read()
                token = mediator.encrypt(original_content)
            
            
            with open(str(filepath) + self.SUFFIX, 'wb') as f:
                f.write(token)
                
        except Exception as exc:
            print(exc)
        
        else:
            os.remove(filepath)
    
    def encrypt_directory(self, directory, key, *, ignore_suffix=None):
        for root, _, files in os.walk(directory):
            for file in files:
                ign_suffix = ignore_suffix and str(file).endswith(ignore_suffix)
                                
                if ign_suffix:
                    continue
                
                fullpath = os.path.join(root, file)
                self.encrypt_file(fullpath, key)
    
    def decrypt_file(self, filepath, key):
        if not str(filepath).endswith(self.SUFFIX):
            print('Sufixo inválido.')
            return
        
        try:
            with open(filepath, 'rb') as f:
                token = f.read()
                mediator = Fernet(key)
                decrypted_content = mediator.decrypt(token)
            
            original_filename = str(filepath).replace(self.SUFFIX, '')
            with open(original_filename, 'wb') as f:
                f.write(decrypted_content)
                
        except Exception as exc:
            print(exc)
        
        else:
            os.remove(filepath)

    def decrypt_directory(self, directory, key):
        for root, _, files in os.walk(directory):
            for file in files:
                invalid_suffix = not str(file).endswith(self.SUFFIX)
                if invalid_suffix:
                    continue
                               
                fullpath = os.path.join(root, file)
                self.decrypt_file(fullpath, key)


    
    