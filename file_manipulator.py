import sys

def main(argv):
    if argv[1] == 'reverse':
        reverse(argv[2],argv[3])
    elif argv[1] == 'copy':
        copy(argv[2],argv[3])
    elif argv[1] == 'duplicate-contents':
        duplicateContents(argv[2],argv[3])
    elif argv[1] == 'replace-string':
        replaceString(argv[2],argv[3],argv[4])
    else:
        sys.stdout.buffer.write(b'Command not found...\n')

# inputpathにあるファイルを受け取り、outputpathにinputpathの内容を逆にした新しいファイルを作成する
def reverse(inputpath,outputpath):
    t = ''

    # inputpathを読み込む
    with open(inputpath,'r') as f:
        t = f.read()

    # outputpathにinputpathの内容を逆にして書き込む
    with open(outputpath,'w') as f:
        f.write(t[::-1])

# inputpathにあるファイルのコピーを作成し、outputpathとして保存する
def copy(inputpath,outputpath):
    t = ''

    # inputpathを読み込む
    with open(inputpath,'r') as f:
        t = f.read()

    # outputpathにinputpathの内容を書き込む
    with open(outputpath,'w') as f:
        f.write(t)

# inputpathにあるファイルの内容を読み込み、その内容を複製し、複製されたinputにn回複製する
def duplicateContents(inputpath,n):
    # inputpathを読み込む
    with open(inputpath,'r+') as f:
        t = f.read()
        # outputpathにinputpathの内容をn回複製して書き込む
        f.write(t * int(n))

# inputpathにあるファイルの内容から文字列'needle'を検索し、'needle'のすべてを'newstring'に置き換える
def replaceString(inputpath,needle,newstring):
    t = ''

    # inputpathを読み込む
    with open(inputpath,'r') as f:
        t = f.read()
        
    # inputpathに置換して書き込む
    with open(inputpath,'w') as f:
        f.write(t.replace(needle,newstring))

if __name__ == '__main__':
    main(sys.argv)