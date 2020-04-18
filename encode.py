# ================================================== #
#                       ENCODE                       #
# ================================================== #
# Author: Brady Hammond                              #
# Created: 04/16/2020                                #
# Last Edited: N/A                                   #
# ================================================== #
#                      IMPORTS                       #
# ================================================== #

import os
import uuid

# ================================================== #
#                      CLASSES                       #
# ================================================== #


class Encoder:
    def __init__(self, shift, message):
        self.shift = shift
        self.message = message
        self.encoded_message = None

    def encode(self):
        encoded_characters = []
        for i in range(len(self.message)):
            if self.message[i].isupper():
                encoded_characters.append(chr((ord(self.message[i]) + self.shift - 65) % 26 + 65))
            elif self.message[i].islower():
                encoded_characters.append(chr((ord(self.message[i]) + self.shift - 97) % 26 + 97))
            else:
                encoded_characters.append(self.message[i])
        self.encoded_message = ''.join(encoded_characters)
        return self.encoded_message

    def save(self):
        file_name = str(uuid.uuid1()).replace('-', '') + '.txt'
        save_directory = os.path.join(os.getcwd(), "saves")

        if not os.path.exists(save_directory):
            try:
                os.makedirs(save_directory)
            except OSError as ex:
                raise ex

        full_path = os.path.join(save_directory, file_name)
        filer_writer = open(full_path, 'x')
        filer_writer.write(self.encoded_message)
        filer_writer.close()

# ================================================== #
#                        EOF                         #
# ================================================== #
