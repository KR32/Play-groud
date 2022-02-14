import os
import re
import sys
import glob


# filename = "D:\\App_Folders\\vscode\\Python\\vumaasha-s-py\\week 3\\1990.html"


def extract_names(filename,printable=True):
    names = []
    file = open(filename, "r+")
    text = file.read()

    year_match = re.search(r"Popularity\sin\s(\d\d\d\d)", text)
    if not year_match:
        sys.stderr.write("year not found")
        sys.exit(1)
    year = year_match.group(1)
    names.append(year)
    # get the ranking of names.
    tuples = re.findall(r"<td>(\d+)</td><td>(\w+)</td>\<td>(\w+)</td>", text)
    if printable == False:
        print(names)
        print(year)
        print(tuples)
    names_rank = {}
    for ranked in tuples:
        (rank, boyname, girlname) = ranked
        if boyname not in names_rank:
            names_rank[boyname] = rank
        if girlname not in names_rank:
            names_rank[girlname] = rank
    ranked_names = sorted(names_rank.keys())

    if printable == False:
        for name in ranked_names:
            names.append(name + "" + names_rank[name])

        return names
    else:
        file = open(str(year)+'.txt','w+')
        file.write("name" + "   |   " +'rank'+'\n')
        file.write("_____" + "______" +'_____'+'\n')

        for name in ranked_names:
            file.write(name + "     " + names_rank[name]+'\n')

        return file




def main():
    print('''Choose one of The Options Below:
  1) summary ---> print large amount of data (not recommended) 
  2) file ---> tO get  .txt files accordingly
  Type 1 or 2 :
              ''')
    option = input()
    if int(option) == 1:
        # iterate over files in directory to get a file path 
        for filename in glob.iglob(r'D:\\App_Folders\\vscode\\Python\\vumaasha-s-py\\week 3\\data\\*.html'):
            extract_names(filename,printable=False)
        # sys.exit(1)
    elif int(option) == 2:
        for filename in glob.iglob(r'D:\\App_Folders\\vscode\\Python\\vumaasha-s-py\\week 3\\data\\*.html'):
            extract_names(filename,printable=True)
        # sys.exit(1)
    else:
        print('unknown option: ' + option)
        sys.exit(1)

if __name__ == '__main__':
  main()

    
    
