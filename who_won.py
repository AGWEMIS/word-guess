"""
Main file that runs the program
"""

from pc_guess import pcPlay
from player_guess import iPlay


def check_continue(who):
    while True:
        game_cont = input('Do you want to continue to guess the word \n(yes) or (no) \n >>> ').lower()
        if game_cont == 'yes':
            if who == 'player':
                player_attemps = iPlay()
                return player_attemps
            elif who == 'pc':
                pc_attemps = pcPlay()
                return pc_attemps
            break
        elif game_cont== 'no':
            print('That was a great game, have a rest day !!!')
            break
        else:
            print('Please enter the correct answer...')
            continue

def run():
    results = {
        "pc" : 0,
        "player" : 0
        }
    while True:
        queue = input('Who is gonna start the game, PC or Player \n>>> ').lower()
        if queue == 'player':
            results["player"] = iPlay()
            results["pc"] = check_continue('pc')
            break
        elif queue == 'pc':
            results["pc"] = pcPlay()
            results["player"] = check_continue('player')
            break
        else:
            print('Please, check the choice that you entered...\n\n')
            continue
    
    diff = results["pc"] - results["player"]
    
    for key, value in results.items():
        print(f"{key} : {value}")
        
    if diff > 0:
        print(f"Player won with differance {abs(diff)}")
    elif diff < 0:
        print(f"PC won with differance {abs(diff)}")
    else:
        print('Happy Draw, Friends win together!!!')
        
    
    
            
run()
    
    
    
    
    
    
    
    
    
    
        
    
