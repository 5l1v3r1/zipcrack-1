import sys
import zipfile
import optparse
from threading import Thread


def main():
    parser = optparse.OptionParser('usage: zipcracker.py ' + '-f <zipfile> -w <wordlist>')
    parser.add_option('-f', dest='zipf',type='string',help='specify zip file')
    parser.add_option('-w', dest='wordf',type='string',help='specify wordlist file')
    (options,args) = parser.parse_args()
    if (options.zipf == None) | (options.wordf == None):
        print(parser.usage)
    else:
        zipf = options.zipf
        wordf = options.wordf
    zipf = zipfile.ZipFile(zipf)
    wordf = open(wordf)
    for line in wordf.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zipf, password))
        t.start()

def extractFile(zipf, password):
    try:
        zipf.extractall(pwd=password)
        print('\n[+] Brute Force Successful: ' + password)
        return password
    except:
        space = len(password)
        space = ' ' * space
        sys.stdout.write('[+] Trying ' + password + space + '\r')
        sys.stdout.flush()
        return


if __name__ == '__main__':
    main()
