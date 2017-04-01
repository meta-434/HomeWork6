# <Reads a file, and lists all doubled words and the lines
# they appear on.>
#
#  @author <Alex Hapgood> (ach1)
#  @date   <03/30/2017>
#
# Virginia Tech Honor Code Pledge
#  On my honor:
#
#  -I have not discussed the Python language code in my program with
#    anyone other than my instructor or the teaching assistants
#    assigned to this course.
#  -I have not used Python language code obtained from another student,
#   or any other unauthorized source, either modified or unmodified.
# -If any Python language code or documentation used in my program
#    was obtained from another source, such as a text book or course
#   notes, that has been clearly noted with a proper citation in
#    the comments of my program.
#  -I have not designed this program in such a way as to defeat or
#    interfere with the normal operation of the Web-Cat Server.
#
# <Alex Hapgood>
# -----------------------------------------------------------------------
file_name = input('Enter file name: ')
file_obj = open(file_name, 'r')
split_line = []
line_counter = 0
lastWord = ''

for line in file_obj:
    split_line = line.split()
    line_counter += 1
    #since index = length -1, and we're already looking +1.
    #I had to make sure I didn't try to access a list item that
    #didn't exist.
    if lastWord == split_line[0]:
        print('Found word: %r on line %r.' % (lastWord, line_counter))
    for x in range(0, len(split_line) - 1):
        if split_line[x] == split_line[x + 1]:
            print('Found word: %r on line %r.' % (split_line[x], line_counter))
    lastWord = split_line[-1]
