import os
from os import path, getcwd

x = os.path.exists('nygdziennik')

def pisanko():
    wyb_data = input(print('podaj date: ')) 
    with open (f'nygdziennik/{wyb_data}.txt', 'a+') as myfile:
        wyb_txt = input(print('jaka notatka wariacie??? '))
        myfile.write('####    ##   ##     ##    ######     ######     ########    ##    #######   ####    ##   ####    ##  ##   ##    ##')
        myfile.write('## ##   ##    ##   ##    ##          ##    ##       ###     ##    ##        ## ##   ##   ## ##   ##  ##   ##   ## ')
        myfile.write('##  ##  ##     ## ##    ##     ###   ##     ##     ###      ##    #####     ##  ##  ##   ##  ##  ##  ##   ####    ')
        myfile.write('##   ## ##      ###      ##     ##   ##    ##    ###        ##    ##        ##   ## ##   ##   ## ##  ##   ##   ## ')
        myfile.write('##    ####      ###       #######    ######     ########    ##    #######   ##    ####   ##    ####  ##   ##    ##')
        myfile.write('\n')
        myfile.write('tfuj najlepszy dziennik :) .!.')
        myfile.write('\n')
        myfile.write(wyb_txt)

if x == True :
    pisanko()
else:
    cwd = getcwd()
    os.chdir(cwd)
    os.makedirs('nygdziennik')
    pisanko()
