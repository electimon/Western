import sys, os


#Credits
def credits() :

    os.system("clear")

    print("Main Credits: Noah Scott (@CorruptByte on Twitter), @Vyce_Merculous, Dingdongding30 on reddit\nSoftware Used: XPwn, idevicerestore, ipwndfu\nSpecial Thanks To: Axi0mX, Planetbeing, and The iPhoneDevTeam.")

    gotoMain()

#Info
def information_fkp() :

    os.system("clear")

    print("Nothing, really. Just a project the @32Bites maintains... sometimes.")
    credits()

    gotoMain()

#Update manually, lol
def update_fkp() :

    os.system("clear")

    print("I won't bother to add this option, If you need to update, do it manually.")

    gotoMain()

#Verbose Boot
def install_verbose_boot() :

    os.system("clear")

    print("This option, only supports these versions on both BR: \n1) iOS 3.1.3\n2) iOS 4.1\n3) iOS 4.2.1\n4) iOS 5.0.1\n5) iOS 5.1.1\n6) iOS 6.1\n7) iOS 6.1.3\n8) iOS 6.1.6")

    try:

        verbose_option = input("Your selected version ! ")

    except:

        print("The option you have chosen is not a integer!")

        main()

    if verbose_option == 1:
        enter_pwned_dfu()

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/3.1.3_.dump")

    elif verbose_option == 2:
        enter_pwned_dfu()

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/4.1_.dump")

    elif verbose_option == 3:
        enter_pwned_dfu()

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/4.2.1_.dump")

    elif verbose_option == 4:
        enter_pwned_dfu()

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/5.0.1_.dump")

    elif verbose_option == 5:
        enter_pwned_dfu()

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/5.1.1_.dump")

    elif verbose_option == 6:
        enter_pwned_dfu()

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/6.1_.dump")

    elif verbose_option == 7:
        enter_pwned_dfu()

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/6.1.3_.dump")

    elif verbose_option == 8:
        enter_pwned_dfu()

        os.system("clear && cd ipwndfu/ && ./ipwndfu --flash-nor=NOR/6.1.6_.dump")

    else:

        print("NOT A VALID OPTION!")

        main()
    
    gotoMain()


#Restore to a Custom firmware
def restore_cfw() :

    os.system("clear")

    print("Your going to restore to a custom ipsw.\nBE IN DFU NOT PWNED DFU!!!\n")

    cfw_path = raw_input("Path to custom ipsw ! ")

    os.system("idevicerestore -c " + cfw_path)

    gotoMain()


#Create Custom Firmware ipsw
def create_cfw() :

    os.system("clear")

    print("Your about to create a custom ipsw. \nNOTE: you have to have the proper FirmwareBundle in the .resources/FirmwareBundles/ folder.")

    base_ipsw_path = raw_input("Path to base ipsw ! ")

    save_cfw_path = raw_input("Path to save ipsw (WITH FILENAME) ! ")
    
    input = raw_input("Do you want to update the baseband? (Y/n) ! ")
    
    if input == "Y" or "y" :
        os.system("./ipsw " + base_ipsw_path + " " + save_cfw_path + "-b Logos/0.png -r Logos/1.png -bbupdate")
    elif input == "N" or "n" :
        os.system("./ipsw " + base_ipsw_path + " " + save_cfw_path + "-b Logos/0.png -r Logos/1.png")
    else :
        os.system("./ipsw " + base_ipsw_path + " " + save_cfw_path + "-b Logos/0.png -r Logos/1.png -bbupdate")

    gotoMain()



#Pwned DFU
def enter_pwned_dfu() :

    print("Be in dfu, then hit Enter once in dfu.")

    ddffuu = raw_input("")

    os.system("clear && cd ipwndfu/ && ./ipwndfu -p")

    gotoMain()


#24KPwn
def install_24kpwn_exploit() :

    enter_pwned_dfu()

    os.system("clear && cd ipwndfu/ && ./ipwndfu --24kpwn")

    gotoMain()


#Alloc8
def install_alloc8_exploit() :

    enter_pwned_dfu()

    os.system("clear && cd ipwndfu/ && ./ipwndfu -x")

    gotoMain()

def gotoMain() :
    gotoMainn = raw_input("Do you want to continue using Western? (Y/n) ! ")

    if gotoMainn == "Y" or "y" :
        main()
    elif (gotoMainn) == "N" or "n" :
        exit()
    else :
        main()


def main() :

    os.system("clear")

    print("Western has started.\n Script Written By Noah Scott (@CorruptByte on Twitter)\n")

    print("Options:\n")

    print("1) Create ipsw\n2) Install custom ipsw (Be in DFU, not PWNed DFU)\n3) Update\n4) Credits :D\n5) Info\n6) Install verbose boot (BE IN DFU)\n7) Install 24kpwn on old BR devices(BE IN DFU)\n8) Install Alloc8 on new BR devices(BE IN DFU)\n9) Enter PWNed DFU")

    try:

        option_1 = input("Your Option ! ")

    except:

        print("The option you have chosen is not a integer!")

        exit()

    if option_1 == 1:

        create_cfw()

    elif option_1 == 2:

        restore_cfw()

    elif option_1 == 3:

        update_fkp()

    elif option_1 == 4:

        credits()

    elif option_1 == 5:

        information_fkp()

    elif option_1 == 6:

        install_verbose_boot()

    elif option_1 == 7:

        install_24kpwn_exploit()

    elif option_1 == 8:

        install_alloc8_exploit()

    elif option_1 == 9:

        enter_pwned_dfu()

    else :

        print("NOT A VALID OPTION!")

        exit()
    credits()

    print("\nI am done doing my job.")

main()
