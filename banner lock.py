import os
import getpass
import sys

# Termux এর ডেটা ফাইল পাথ
DATA_DIR = '/data/data/com.termux/files/usr/share/'
LOCK_FILE = os.path.join(DATA_DIR, "usr_nd_pwd.txt")

# গ্লোবাল ফ্লাগ এবং কনস্ট্যান্ট
flag = True
endc = '\033[0m'
black = '\033[30m'
red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
blue = '\033[34m'
magneto = '\033[36m'

# প্রাথমিক সেটআপ
def initial_banner():
    try:
        os.system('figlet -c -k -f slant Termux-Lock | lolcat')
        print(magneto + '\n\t\t[ ★ Termux - Lock ★ ]\n', endc)
        print(green + '\t\tcoded by - Mr.Anonymous\n', endc)
    except:
        # যদি figlet/lolcat ইন্সটল না থাকে
        print("\n[ ★ Termux - Lock ★ ]")
        print("coded by - Mr.Anonymous\n")

# নতুন ব্যানার তৈরির ফাংশন
def create_custom_banner():
    dash = '-'
    print(blue + '\n' + dash * 15 + 'Custom-Banner' + dash * 15)
    
    # ব্যানার টেক্সট ইনপুট
    text = input(yellow + '\nEnter the text for your banner (e.g., your name): ' + endc).strip()
    
    # ফন্ট নির্বাচনের অপশন (ঐচ্ছিক, তবে ভালো)
    font = input(yellow + 'Enter figlet font (default: slant): ' + endc).strip() or 'slant'
    
    if text:
        try:
            # figlet এবং lolcat ব্যবহার করে ব্যানার তৈরি
            # --c মানে সেন্টারড, -k মানে কমাণ্ড লাইন থেকে ফন্ট ইনপুট
            os.system(f"figlet -c -k -f {font} '{text}' | lolcat")
        except Exception as e:
            print(red + f"Error creating banner. Make sure 'figlet' and 'lolcat' are installed. Error: {e}")
    else:
        print(red + "Text cannot be empty.")
        
    print(blue + '\n' + dash * 15 + 'Complete' + dash * 15)


# --- মেনু ফাংশন ---
def main_menu():
    dash = '-'
    print(blue + '\n' + dash * 15 + 'Main-Menu' + dash * 15)
    print(yellow + '''
    1. Register
    2. Login
    3. Remove Lock
    4. Create Custom Banner  <-- নতুন অপশন
    5. Exit\n''' + endc)
    print(blue + '\n' + dash * 13 + 'Select option' + dash * 13)

# --- রেজিস্ট্রেশন ফাংশন (পূর্বের মতোই) ---
def register():
    dash = '-'
    print(blue + '\n' + dash * 15 + 'Register' + dash * 15)
    
    usr = input(blue + '\nEnter username : ' + endc).strip()
    pw = getpass.getpass(prompt=green + '\nEnter password : ' + endc, stream=sys.stderr)
    rpw = getpass.getpass(prompt=green + '\nRetype password : ' + endc, stream=sys.stderr)

    if pw == rpw and usr:
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
            
        try:
            with open(LOCK_FILE, 'w') as usrpwd:
                usrpwd.write(usr + '\n')
                usrpwd.write(pw + '\n')
            print(magneto + '\nRegistered Successfully...')
        except Exception as e:
            print(red + f"Error saving file: {e}")
            
    elif not usr:
         print(red + "Username cannot be empty.")
    else:
        print(red + "Password doesn't match")
        
    print(blue + '\n' + dash * 15 + 'Complete' + dash * 15)

# --- লগইন ফাংশন (পূর্বের মতোই) ---
def check_usr_pass():
    dash = '-'
    global flag
    print(blue + '\n' + dash * 15 + 'Login' + dash * 15)
    
    if not os.path.exists(LOCK_FILE):
        print(red + '\n\t[×] Lock file not found. Please register first. [×]' + endc)
        return

    username = input(yellow + '\n\t[+] Username : ' + endc).strip()
    password = getpass.getpass(prompt=yellow + '\n\t[*] Password : ' + endc, stream=sys.stderr)
    
    try:
        with open(LOCK_FILE, 'r') as usrpwd:
            lines = usrpwd.readlines()
            
        if len(lines) >= 2:
            stored_usr = lines[0].strip()
            stored_pwd = lines[1].strip()
            
            if username == stored_usr and password == stored_pwd:
                print(green + '\n\t\t[★] Welcome to the Termux [★]\n' + endc)
                flag = False
            else:
                print(red + '\n\t\t[×] Invalid username or password [×]' + endc)
        else:
            print(red + '\n\tLock file is corrupted or empty. Please re-register.')
            
    except FileNotFoundError:
        print(red + '\n\t[×] Lock file not found. Please register first. [×]' + endc)
    except Exception as e:
        print(red + f'\n\tAn error occurred during login: {e}' + endc)

    print(blue + '\n' + dash * 13 + 'Completed' + dash * 13)

# --- রিমুভ ফাংশন (পূর্বের মতোই) ---
def remove():
    dash = '-'
    print(blue + '\n' + dash * 40)
    
    if os.path.exists(LOCK_FILE):
        try:
            os.remove(LOCK_FILE)
            print(magneto + '\n\tTermux-Lock disabled successfully...')
        except Exception as e:
            print(red + f"\n\tError removing lock file: {e}")
    else:
        print(red + '\n\tYou have already removed your lock')
        print(blue + '\tSo, first register to login')
        
    print(blue + '\n' + dash * 40)

# --- এক্সিট ফাংশন (পূর্বের মতোই) ---
def exit_program():
    global flag
    print(blue + '\n\tThank you for Using...', endc)
    flag = False

# --- প্রধান প্রোগ্রাম লজিক ---

# প্রাথমিক ব্যানার ডিসপ্লে
initial_banner()

# কম্যান্ড লাইন আর্গুমেন্ট চেক
if len(sys.argv) >= 2:
    arg = sys.argv[1]
    if arg == '-l':
        check_usr_pass()
        sys.exit()

# মেনু লুপ
while flag == True:
    # মেনুতে নতুন অপশন যুক্ত করা হয়েছে: 4: create_custom_banner
    menu = {1: register, 2: check_usr_pass, 3: remove, 4: create_custom_banner, 5: exit_program}
    main_menu()
    
    try:
        choice = int(input(magneto + '\nEnter choice : ' + endc))
        if choice in menu:
            menu[choice]()
        else:
            print(red + "Invalid choice. Please select a valid number from the menu.")
    except ValueError:
        print(red + "Invalid input. Please enter a number.")
    except KeyError:
        print(red + "An unexpected error occurred with menu selection.")
