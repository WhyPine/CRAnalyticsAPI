from client import CrunchyrollClient
import methods

def main():
    client = CrunchyrollClient("goodingaidan@gmail.com",  "Sx/6@SBzk&.ghKP")
    client.auth()
    #client.popular()
    methods.getAllAlphabetical(client)

if __name__ in '__main__':
    main()