"""
This program searches for mp3 files in the same directory as this script file,
then modifies the numberings of each music in a manner that makes each number of digits
the same.

Note :: This program assumes that the names all have numbers separate from names
        ex) "01 musician - name.mp3", "artist - 100 name.mp3"
"""

import os
import re

if __name__ == '__main__':
    music_original_names = [file_name for file_name in os.listdir() if file_name.endswith('.mp3')]

    print("Files to be modified :\n")
    for mp3_file_name in music_original_names:
        print(mp3_file_name)

    # Check if no mp3 files were found and if so, stop the program
    if music_original_names == []:
        input("\nNo mp3 files are found."
              "\nPlease, check if this script file and the mp3 files"
              "\n are in the same directory."
              "\n<Press ENTER to exit the program>")
        exit()

    # Checking before the user procedes
    input("\nIf the files in the list above is correct,\n"
          "Press ENTER to continue.")

    try:
        max_number = max(int(re.search(r"\b\d+\b", name).group()) for name in music_original_names)
    except AttributeError:
        input("\n\nFile Name Error! : The name of one or more files might not have numberings\n"
              "                    or the numbering might be right next to letters\n"
              "                   without any whitespaces separating it.\n\n"
              "Please, check the names of the files and come back.\n"
              "<Press ENTER to exit the program>")
        exit()

    num_of_digits_for_numbering = len(str(max_number))

    def renumber(string, max_len):
        """
        Function that takes a string that contains digits
        and a int that indicates the number of digits required.

        Then, it modifies the number part of the string and returns the result.

        ex) >>>renumber('toby fox - UNDERTALE Soundtrack - 1 Once Upon a Time.mp3', 3)
            # returns 'toby fox - UNDERTALE Soundtrack - 001 Once Upon a Time.mp3'
        """
        pattern = r"\b\d+\b"
        matched_numstring = re.search(pattern, string).group()
        modified_numstring = '0' * (max_len - len(matched_numstring)) + matched_numstring
        result = re.sub(pattern, modified_numstring, string)
        return result

    modified_mp3_names = list(map(lambda string: renumber(string, num_of_digits_for_numbering),
                                  music_original_names))

    for original_name, modified_name in zip(music_original_names, modified_mp3_names):
        os.rename(original_name, modified_name)

    print("\n\nModified names :\n")
    for modified_mp3_name in modified_mp3_names:
        print(modified_mp3_name)

    input("\nFile names are successfully modified.\n"
          "Press ENTER to exit the program.")
