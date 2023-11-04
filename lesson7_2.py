
import tools

def main():
    while(True):
        tools.playGame()
        playAgain = input("您還要繼續嗎(y,n)?")
        if playAgain == 'n':
            break
    
    print("遊戲結束")

if __name__ == "__main__":
    main()