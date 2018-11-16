import os

from pprint import pprint

def main():
    print(os.name)
    print(os.getcwd())
    os.chdir('..')
    print(os.getcwd())
    print(os.getpid())
    os.system('ECHO Hello World')
    print(os.listdir())
    for tpath, dirs, files in os.walk('.'):
        print(tpath)
        if dirs:
            print('The following directories exist:')
            pprint(dirs)
        if files:
            print('the following files exist:')
            pprint(files)
        print()
    
    for f in os.listdir():
        print(os.path.abspath(f))
    
    print(os.path.exists('D:\\Documents\\teaching\\Basic Python.pptx'))
    print(os.path.exists('C:\\Path\\mic\\doesn\\exist'))
    
    print(os.path.join('\\path\\I\\Want','to','make'))

if __name__ == '__main__':
    main()