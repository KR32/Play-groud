# Reading the command-line arguments
# Note:
# py read_CMD_line_args.py agr1 arg2...arg0=file_path
import sys
name=sys.argv[1]
print('sys.argv[0]='+sys.argv[0])
print('sys.argv[1] = '+name)
