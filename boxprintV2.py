#!/usr/bin/env python3

import sys

def boxprint (vsymbol, hsymbol, width, height):
    if (len(vsymbol)>1) or (len(hsymbol)>1):
        print('')
        print('I TOLD YOU THE SYMBOL COULD ONLY BE ONE CHARACTER. REFLECT ON YOUR CHOICES UP UNTIL THIS MOMENT AND BE SHOWERED IN SHAME.')
        print('')
        print('------------------------------------------------')
        dialogue()
    elif (width < 2) or (height < 2):
        print('')
        print('I TOLD YOU NEITHER WIDTH NOR HEIGHT CAN BE LESS THAN 2. NOW SUFFER THE CONSEQUENCES OF AN EXISTENCE WITHOUT A BOX.')
        print('')
        print('------------------------------------------------')
        dialogue()

    print(hsymbol * width)

    for i in range (height-2):
        print(vsymbol + (' ' * (width-2) + vsymbol))

    print(hsymbol * width)
    print('')
    print('')
    print('')
    afterbox()

def dialogue():
    print('')
    print('')
    print('------------------------------------------------')
    print('')
    print('Welcome to the realm of ultimate box creator.\nCower before the terrifying ability of the unfeeling machine, meatbag.')
    print('')
    print('------------------------------------------------')
    print('Dare to enter the horizontal symbol you wish to use. One character only.')
    hsymbol=input()
    print('------------------------------------------------')
    print('Cower in fear as you enter the vertical symbol you wish to use. One character only.')
    vsymbol=input()
    print('------------------------------------------------')
    print('I demand you the enter desired width of the box. Width must be > 2.')
    width=int(input())
    print('------------------------------------------------')
    print('Shudder as you enter the desired height of the box. Height must be > 2.')
    height=int(input())
    boxprint(vsymbol, hsymbol, width, height)

def cannotread():
    print('Would you like to experience the mighty box printer again?')
    print('------------------------------------------------')
    print('Y or N')
    answer=input()
    if answer.lower() == 'y':
        dialogue()
    elif answer.lower() == 'n':
        sys.exit()
    elif answer.lower() != 'y' or 'n':
        print('I said Y or N, meatbag.')
        print('')
        print('------------------------------------------------')
        cannotread()

def afterbox():
    print(' ')
    print('')
    print('------------------------------------------------')
    print('Would you like to experience the mighty box printer again?')
    print('------------------------------------------------')
    print('Y or N')
    answer=input()
    if answer.lower() == 'y':
        dialogue()
    elif answer.lower() == 'n':
        print('')
        print('')
        sys.exit()
    elif answer.lower() != 'y' or 'n':
        print('I said Y or N, meatbag.')
        print('')
        print('------------------------------------------------')
        cannotread()

dialogue()
