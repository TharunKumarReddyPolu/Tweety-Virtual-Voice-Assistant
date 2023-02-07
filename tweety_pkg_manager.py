# Importing subprocess for command line simulation
import subprocess
# Importing urllib to check internet connectivity
import urllib

# Initializing host as project's github repository
def check_internet_connection():
    # Host url to check internet access
    host = "https://github.com/TharunKumarReddyPolu/Tweety-Virtual-Voice-Assistant"
    # Trying to open the host url
    # Returns 1(i.e, true) if there is a valid internet access
    try:
        urllib.request.urlopen(host)
        return 1
    # Trying to catch exception
    # Returns 0(i.e, False) when unable to reach the host.
    except Exception as e:
        #print("Exception details : "+ e)
        return 0

def install_module(module_name, module_version,version_type):
    # Updating pip to the latest version
    subprocess.run('python -m pip install --upgrade pip')

    # Commanding terminal to pip install
    if version_type == "latest" and module_version == False:
        subprocess_response = subprocess.run('pip3 install {}'.format(module_name))
    elif version_type == "specific" and module_version:
        subprocess_response = subprocess.run('pip3 install {0}=={1}'.format(module_name, module_version))

    # Installation worked fine
    if subprocess_response.returncode == 0 and module_version == False:
        print("Hurray! {} latest version is successfully installed".format(module_name))
    elif subprocess_response.returncode == 0 and module_version:
        print("Hurray! {0} with {1} version is successfully installed".format(module_name, module_version))

    # If there is no valid internet connection
    elif subprocess_response.returncode == 1 and check_internet_connection() == 0:
        print("Oops! Error occurred, Please check your Internet connection")

    # If the name of module to be installed wrong
    elif subprocess_response.returncode == 1 and check_internet_connection() == 1:
        print("Oops! error occurred. Please check the name of module to be installed")

def uninstall_module(module_name):
    # Updating pip to latest version
    subprocess.run('python -m pip install --upgrade pip')
    try:
        # Commanding terminal to pip uninstall
        subprocess_response = subprocess.run('pip3 uninstall '+module_name)

        # Uninstallation worked fine
        if subprocess_response.returncode == 0:
            print("Hurray! " + module_name + " is successfully uninstalled")
    # Retreiving the exception details
    # If some error occurs during uninstall
    except Exception as e:
        print("Oops! Error occured while uninstalling with details: " + e)

def installed_modules_list(type):
    # Updating pip to latest version
    subprocess.run('python -m pip install --upgrade pip')

    if type == "list":
        # Commanding terminal get installed modules names as list 
        subprocess_response = subprocess.run('pip3 list')
    elif type == "freeze":
        # Commanding terminal get installed modules names as freeze 
        subprocess_response = subprocess.run('pip3 freeze')

    # post displaying the installed modules list
    if subprocess_response.returncode == 0:
        print("Above modules are currently installed in your system")

def exit_session():
    # Exits the current command line session
    print("Thanks for using the package manager!")
    quit()    


# Driver program
if __name__=='__main__':
    # Below variable holds the user desired input from command line
    user_action_menu = input(
        "Hello! Welcome to Tweety Package Manager!\n"+
        "1. Install module latest version\n"+
        "2. Install module specific version\n"+
        "3. Uninstall\n"+
        "4. List\n"+
        "5. Freeze\n"+
        "6. Exit\n"+
        "Choose the operation? " )
    # Pro Tip: Switch case can be used but it's available from Python 3.10+ version
    # But we are currently running on Python 3.7 Stable edition.
    if user_action_menu.isnumeric():
        if user_action_menu == "1":
            # Takes module name and installs the latest version of the module
            module_name = input("Enter the module name to install : ")
            print("Latest version will be installed automatically")
            install_module(module_name,False, "latest")
        elif user_action_menu == "2":
            # Takes module name, module specific version and installs the that version of the module
            module_name = input("Enter the module name to install : ")
            module_version = input("Enter the version of module: ")
            install_module(module_name, module_version, "specific")
        elif user_action_menu == "3":
            # Takes module name and uninstalls the module irrespective of version
            module_name = input("Enter the module name to uninstall : ")
            uninstall_module(module_name)
        elif user_action_menu == "4":
            # To get the list of installed modules as a table in command line
            installed_modules_list("list")
        elif user_action_menu == "5":
            # To get the list of installed modules as a table in command line with name==version
            installed_modules_list("freeze")
        elif user_action_menu == "6":
            # To exit the command line session/ to exit the program
            exit_session()
        else:
            # Prompts the user to select atleast one of the option from above
            print("Please select one option from the above")
    else:
        print("Please enter a numeric value eg. 1,2,3,4,5,6...")
