# Introduction & Description

This program modifies the number of each track --mp3 file-- so that the number of digits
 in each track number is the same as others.

ex) ['music 1.mp3', 'music 2.mp3', 'music 10.mp3', 'music 100.mp3']
    >>> ['music 001.mp3', 'music 002.mp3', 'music 010.mp3', 'music 100.mp3']



This can be useful if your computer or mobile device sorts the tracks in a wrong order.
And by "in a wrong order," I mean this:

    music 01.mp3
    music 02.mp3
    music 03.mp3
          .
          .
          .
    music 09.mp3
    music 10.mp3
    music 100.mp3   <<< 100 coming after 10!?
    music 101.mp3   <<< NO! It should be 11!!!
          .
          .
          .



This problem can be solved if you keep the number of digits consistent!

    music 001.mp3
    music 002.mp3
    music 003.mp3
          .
          .
          .
    music 009.mp3
    music 010.mp3
    music 011.mp3
          .
          .
          .
    music 099.mp3
    music 100.mp3
    music 101.mp3
          .
          .
          .



# Requirements

- Any program that can execute python script files



# How To Use

1. Make sure the following conditions are met:
 - The script file is in the same directory as the mp3 files that need to be processed
 - All mp3 file names contain track numbers (like the ones in the examples above)
 - The track numbers are separated from alphabetical letters
     ex) These are okay: "01 - music.mp3", "music - 11.mp3", "artist - 05 music.mp3"
         These cause ERROR: "01music.mp3", "music11.mp3", "mu101sic.mp3"
 - The mp3 files are in the same album, soundtrack, or any of those sort
   (If not, the program won't crash or something, but it will consider all mp3 files
     in the directory as files from the same group. You don't want two different
     soundtracks to get messed up and have mixed track numbers...)

2. Execute the python script file "numbering_modifier.py"

3. Check the files in the list

4. If everything looks good, just press enter to continue

5. Check the modified file names in the list

6. All good? Press enter to exit the program

7. It should be good to go!
