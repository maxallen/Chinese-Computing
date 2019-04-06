input_file = "Resources/Frequency_Dictionaries/hskvocab.txt"
output_file = "Resources/Frequency_Dictionaries/hskvocab_revised.txt"
DELINEATOR = "，"

# with open(output_file, 'w') as out_file:
#     with open(input_file, 'r') as in_file:
#         for line in in_file:
#             line_info = line.strip().split(DELINEATOR)
#             # Write correct info back into output file in proper format
#             if len(line_info) > 2:
#                 out_file.write("{} {}\n".format(line_info[2], line_info[1]))

with open(output_file, 'w') as out_file:
    with open(input_file, 'r') as in_file:
        for line in in_file:
            line_info = line.strip().split(DELINEATOR)
            for item in line_info:
                out_file.write("{}\n".format(item))
