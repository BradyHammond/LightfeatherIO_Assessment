# ================================================== #
#                       ENCODE                       #
# ================================================== #
# Author: Brady Hammond                              #
# Created: 04/16/2020                                #
# Last Edited: 04/17/2020                            #
# ================================================== #
#                      IMPORTS                       #
# ================================================== #

import os
import uuid

# ================================================== #
#                      CLASSES                       #
# ================================================== #


class Encoder:
    # Encoder takes incoming shift and message
    def __init__(self, shift, message):
        self.shift = shift
        self.message = message
        self.encoded_message = None

    def encode(self):
        # Initialize char array
        encoded_characters = []

        # Loop through each character
        for i in range(len(self.message)):
            # If uppercase alpha ASCII char shift
            if self.message[i].isupper():
                encoded_characters.append(chr((ord(self.message[i]) + self.shift - 65) % 26 + 65))
            # If lowercase alpha ASCII char shift
            elif self.message[i].islower():
                encoded_characters.append(chr((ord(self.message[i]) + self.shift - 97) % 26 + 97))
            # If not alpha ASCII char keep old char
            else:
                encoded_characters.append(self.message[i])

        # Concatenate char array and return encoded message
        self.encoded_message = ''.join(encoded_characters)
        return self.encoded_message

    def save(self):
        # Generate unique file name
        file_name = str(uuid.uuid1()).replace('-', '') + '.txt'
        # Get save directory path
        save_directory = os.path.join(os.getcwd(), "saves")

        # Make sure save directory exists
        if not os.path.exists(save_directory):
            try:
                # Create new save directory if needed
                os.makedirs(save_directory)
            except OSError as ex:
                raise ex

        # Get full file path and save encoded message to disk
        full_path = os.path.join(save_directory, file_name)
        filer_writer = open(full_path, 'x')
        filer_writer.write(self.encoded_message)
        filer_writer.close()

# ================================================== #
#                        EOF                         #
# ================================================== #
