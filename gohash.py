import requests
import json
from sys import stderr
import time



Bl='\033[30m' # VARIABLE COLOR 
Re='\033[1;31m'
Gr='\033[1;32m'
Ye='\033[1;33m'
Blu='\033[1;34m'
Mage='\033[1;35m'
Cy='\033[1;36m'
Wh='\033[1;37m'

def banner():
    stderr.writelines(f"""{Gr}

     ██████╗  ██████╗       ██╗  ██╗ █████╗ ███████╗██╗  ██╗
    ██╔════╝ ██╔═══██╗      ██║  ██║██╔══██╗██╔════╝██║  ██║
    ██║  ███╗██║   ██║█████╗███████║███████║███████╗███████║
    ██║   ██║██║   ██║╚════╝██╔══██║██╔══██║╚════██║██╔══██║
    ╚██████╔╝╚██████╔╝      ██║  ██║██║  ██║███████║██║  ██║
     ╚═════╝  ╚═════╝       ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
            {Wh}<<------ {Gr}C O D E   B Y   H U N X {Wh}------>>
                       {Wh}< Hash identified >
""")
banner() #FUNCTION BANNER

try:
    def function(): #FUNCTION HASH
        api_url = 'https://hashes.com/en/api/identifier' #API HASHES
        hash_input = input(f"\n  {Wh}[{Gr}+{Wh}] {Gr}Enter Your Hash : {Wh}") #ENTER HASH
        Query = {'hash': hash_input}

        response = requests.get(api_url, params=Query) #GET REQUEST API 

        data = json.loads(response.text) #GET JSON CONVERT TEXT
        if data ['success']: #SUCCESS
            algorithms = data ['algorithms'] 
            algoritm_hash = ', '.join(algorithms)
            time.sleep(2)
            print(f'\n  {Wh}===================== {Ye}Show Algorithm Hash {Wh}====================')
            print(f'\n  {Wh}[{Gr}+{Wh}] {Gr}Hash :{Wh}', hash_input)
            print(f'  {Wh}[{Gr}+{Wh}] {Gr}Algorithm :{Ye}', algoritm_hash)
            print(f'\n  {Wh}==============================================================')
            while True: # While Tools
                time.sleep(2)
                user_input = input(f"\n  {Wh}Do you want to identify the hash again? {Gr}Y/N {Wh}:{Ye} ")
                if user_input == 'Y' or user_input == 'y':
                    function()
                elif user_input == 'N' or user_input == 'n':
                    print(f'  {Re}Exit ToolS !!!')
                break
        else:
            print(f'  {Wh}[{Gr}!{Wh}] {Gr}Hash :{Re}', data['message']) #ERROR NOT FOUND HASH

    if __name__ == "__main__":
        function() #RUN FUNCTION FUNCTION()
except KeyboardInterrupt: #Keyboard CTRL + C, THEN EXIT!!
    print(f"{Wh} stopped Program...")
