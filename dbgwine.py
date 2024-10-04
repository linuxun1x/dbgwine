import os
import sys
import tty
import termios
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
        dbgstring += ",+" + hash_options[int(each_space)]
    print(f' are enabled{bcolors.ENDC}')
    try:  
        wp = "WINEPREFIX="+os.environ["WINEPREFIX"]
    except: 
        wp = "WINEPREFIX=~/.wine"
        #print(f'{bcolors.BOLD}I did not find a WINEPREFIX, going with default')
    final_str = wp + " WINEDEBUG="+dbgstring+" /usr/bin/wine "+wine_file 
    
    
    return final_str


    
def summarize(launch):
    running = True
    print(f'{launch}')
    print(f'\nPress l to launch, b to quit, c to send to clipboard, t for toggle outputing log file to /tmp/out.log')


def process_startup():
    num_of_args = len(sys.argv)
    if num_of_args == 1:
        print('I need a windows binary, i.e. dbl.py /home/win/notepad.exe')
    try:
        wine_file = sys.argv[num_of_args-1]
        if os.path.exists(wine_file):
            print(f"Hey! We got a winner! using {wine_file}")
            print("just need to make it unix friendly...")
            wine_file = wine_file.replace(" ","\ ")
            wine_file = wine_file.replace("(","\(")
            wine_file = wine_file.replace(")","\)")
            print(f"{wine_file}")
            return wine_file
    except:
        print(f'just going to exit, I expected the last argument to be a windows binary, but the path is wrong. Sorry')
        sys.exit()
        
    
if __name__ == '__main__':
    wine_file = process_startup()
    whats_avaiable(where_ami())
    launch = get_input(wine_file)

    default = launch
    t = 1
    summarize(launch)
    orig_settings = termios.tcgetattr(sys.stdin)
    
    tty.setcbreak(sys.stdin)
    x = 0
    while x != chr(27): # ESC
        x=sys.stdin.read(1)[0]
        
        if x == 't':
            
            t += 1
            if t % 2 == 0:
                launch += ">> /tmp/output.log"
                print(f'Enabled Log to file')
            else:
                launch = default
            summarize(launch)
        if x == 'l':
            os.system(launch)
        if x == 'b' or x == 'q':
            break
        if x == 'c':
            str = "echo " +launch +" | xclip -sel clip "
            os.system(str)
            print("Coppied to clipboard")
    

