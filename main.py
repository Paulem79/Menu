from utils.plugins.update import search_for_updates
from utils.plugins.common import *

def main():
    clear()
    setTitle(f"{name} MENU v{THIS_VERSION}")
    hometitle()
    print(f"""{y}[{r}+{y}]{w} Main options:
\n{y}[{w}01{y}]{w} Soon...
""")
    global choice
    choice = input(f"""{y}[{g}#{y}]{w} Choice: """)

    if choice == '1' or choice == '01':
        transition()
        input(f"{y}[{r}!{y}]{w} Soon...")
        main()
    #elif choice == '2' or choice == '02':
        #transition()
        #exec()
    else:
        clear()
        main()

if __name__ == "__main__":
    import sys
    setTitle(f"Loading... - {name}")
    
    System.Size(120, 30)
    Anime.Fade(Center.Center(banner), Colors.red_to_green, Colorate.Vertical, time=1)
    if not os.path.exists("output"):
        os.makedirs("output", exist_ok=True)
    if os.path.exists("output/QR-Code"):
        shutil.rmtree(f"output/QR-Code")
    if os.path.basename(sys.argv[0]).endswith("exe"):
        search_for_updates()
        clear()
        main()
    try:
        assert sys.version_info >= (3,9)
    except AssertionError:
        input(f"{y}[{Fore.RED}#{y}]{w} Sorry but, your python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with @TIO, please download python 3.9 or higher.")
        sys.exit()
    else:
        search_for_updates()
        clear()
        main()