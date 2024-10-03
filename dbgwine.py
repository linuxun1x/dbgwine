import os
import sys

hash_options = {}
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def where_ami():
    current = os.getcwd()
    with open('channels.txt',"r") as fh:
        output = fh.read()
    
    return output

def whats_avaiable(output):
    global hash_options
    count = 0
    str_brkup = output.split("\n")
    
    color = bcolors.OKGREEN
    print(f'{bcolors.HEADER}These are the channels avaiable for getting debug logs')
    for lines in str_brkup:
        hash_options[count]=lines
        print(f'{color}{count}){lines} ',end="\t")
        count += 1
        if count % 10 == 0:
            if color == bcolors.OKGREEN:
                color = bcolors.OKBLUE
            else:
                color = bcolors.OKGREEN
            if len(lines) > 10:
                print("\t\t")
            print("")

def get_input(wine_file):
    dbgstring = ""
    print(f'\n\n{bcolors.OKBLUE}Please enter values you would like to trace seperated by space. i.e. 1 13 22 64')
    the_input = input()
    the_input_array = the_input.split(" ")
    print(f'{bcolors.OKBLUE}{bcolors.UNDERLINE}Ok options ',end="")
    for each_space in the_input_array:
        print(f' {bcolors.UNDERLINE} {hash_options[int(each_space)]}', end="")
        dbgstring += "+" + hash_options[int(each_space)]+", "
    print(f' are enabled{bcolors.ENDC}')
    try:  
        wp = "WINEPREFIX="+os.environ["WINEPREFIX"]
    except: 
        wp = ""
        print(f'{bcolors.BOLD}I did not find a WINEPREFIX, going with default')
    final_str = wp + " WINEDEBUG="+dbgstring+" /usr/bin/wine "+wine_file
    print(f'final result{final_str}')
    #os.system('/usr/bin/wine')

def process_startup():
    num_of_args = len(sys.argv)
    if num_of_args == 1:
        print('I need a windows binary, i.e. dbl.py /home/win/notepad.exe')
    try:
        wine_file = sys.argv[num_of_args-1]
        if os.path.exists(wine_file):
            print(f"Hey! We got a winner! using {wine_file}")
            return wine_file
    except:
        print(f'just going to exit, I expected the last argument to be a windows binary, but the path is wrong. Sorry')
        sys.exit()
        
    
if __name__ == '__main__':
    wine_file = process_startup()
    whats_avaiable(where_ami())
    get_input(wine_file)

