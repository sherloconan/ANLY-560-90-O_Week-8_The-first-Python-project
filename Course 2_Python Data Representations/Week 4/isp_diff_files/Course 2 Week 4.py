"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    length1 = len(line1)
    length2 = len(line2)
    
    if line1 == line2:
        #first check if two line strings are the same
        return IDENTICAL
    
    elif length1 <= length2:
        if line1 == line2[0:length1]:
            #line1 is the sub string of line2
            return length1
        else:
            for line_index in range(0,length1):
                if line1[line_index] != line2[line_index]:
                    return line_index
                
    else:
        if line2 == line1[0:length2]:
            #line2 is the sub string of line1
            return length2
        else:
            for line_index in range(0,length2):
                if line2[line_index] != line1[line_index]:
                    return line_index


def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index of first difference between the lines
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    length1 = len(line1)
    length2 = len(line2)
    
    #check idx is valid
    #this function assumes idx is correct
    if not isinstance(idx, int):
        return ""
    if line1 == "" or line2 == "":
        return line1 + "\n^\n" + line2 + "\n"
    if (idx not in range(0, length1 + 1)) or (idx not in range(0, length2 + 1)):
        return ""
    
    #check input lines are valid
    if ("\n" in line1) or ("\n" in line2):
        return ""
    if ("\r" in line1) or ("\r" in line2):
        return ""
    
    formatted_line = line1.rstrip() + "\n" + "="*idx + "^\n" + line2.rstrip() + "\n"
    return formatted_line


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    length1 = len(lines1)
    length2 = len(lines2)
    if lines1 == lines2:
        #check two lists are the same
        return (IDENTICAL, IDENTICAL)
    
    elif length1 <= length2:
        #check lines1 is the sub list of lines2
        if lines1 == lines2[0:length1]:
            return (length1, 0)
        else:
            list_index = 0
            for list_index in range(0, length1):
                line_index = singleline_diff(lines1[list_index], lines2[list_index])
                if line_index != IDENTICAL:
                    break
            return (list_index, line_index)
        
    else:
        #check lines2 is the sub list of lines1
        if lines2 == lines1[0:length2]:
            return (length2, 0)
        else:
            list_index = 0
            for list_index in range(0, length2):
                line_index = singleline_diff(lines1[list_index], lines2[list_index])
                if line_index != IDENTICAL:
                    break
            return (list_index, line_index)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list_of_lines = []
    openfile = open(filename, "rt")
    for line in openfile:
        #remove all the trailling whitespaces
        formatted_line = line.rstrip()
        list_of_lines.append(formatted_line)
        
    openfile.close()
    return list_of_lines


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    list1 = get_file_lines(filename1)
    list2 = get_file_lines(filename2)
    compared_result = multiline_diff(list1, list2)
    list_index = compared_result[0]
    line_index = compared_result[1]
    
    if compared_result == (IDENTICAL, IDENTICAL):
        return "No differences\n"
    elif list1 == []:
        #check filename1 is empty
        result = singleline_diff_format(" ", list2[list_index], line_index)
        return "Line 0:\n" + result
    elif list2 == []:
        #check filename2 is empty
        result = singleline_diff_format(list1[list_index], " ", line_index)
        return "Line 0:\n" + result
    else:
        result = singleline_diff_format(list1[list_index], list2[list_index], line_index)
        return "Line " + str(list_index) + ":\n" + result


#print(file_diff_format("file8.txt","file9.txt"))