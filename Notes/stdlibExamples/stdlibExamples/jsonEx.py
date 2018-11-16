from pprint import pprint
import argparse
import json

def main():
    with open(args.fileName) as fp:
        # this returns a dict
        j = json.load(fp)
    pprint(j)
    j = json.loads('{"loading":"from","strings":true}')
    pprint(j)
    d = {      
        1:'one'
        ,3.1459:{
            'lookMa':['no', 'hands']
        }
        ,'normal':'boring'
    }
    print(json.dumps(d))
    with open(args.outputFile,'w') as fp:
        json.dump(d, fp)
    with open(args.outputFile) as fp:
        d2 = json.load(fp)
        pprint(d2)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A file to show off json parsing.')
    parser.add_argument('fileName', help='The name of the json file you would like to examine')
    parser.add_argument('-o', '--outputFile', default='exWrite.json', help='Path to the json file you would like to write the output to.')
    args = parser.parse_args()
    main()