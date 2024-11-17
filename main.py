from init import *
from modules.mongodb import MongoDB

def main():
    mongodb = MongoDB()
    mongodb.run()

if __name__ == "__main__":
    main()