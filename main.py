""" import logging
import requests # need istall it befor  pip install requests
logging.basicConfig(level='ERROR', filename='mylog.log', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
#logging.basicConfig(filename='my.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

logger = logging.getLogger()
print('logger -> ', logger)
print()
print('logger level -> ', logger.level)
print()
print('logger.handlers -> ', logger.handlers)
print()
#logger.setLevel('DEBUG')
#print('logger level -> ', logger.level)

#r = requests.get('https://www.google.ru')

#for key in logging.Logger.manager.loggerDict:
#    print('key --->>>> ', key)
#logger.setLevel('DEBUG')

logger = logging.getLogger('urllib3').setLevel('ERROR')


 

def main():
    pass
    #logger.warning(f'Enter in the main() function: name = {name}')

    #print(dir(logger))

if __name__ == "__main__":
    main() """