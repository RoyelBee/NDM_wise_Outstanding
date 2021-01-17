import Functions.all_library as lib

conn = lib.db.connect('DRIVER={SQL Server};'
                        'SERVER=---------;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=----;PWD=------')

def numberInThousands(number):
    number = number / 1000
    number = int(number)
    number = format(number, ',')
    number = number + 'K'
    return number

def numberInComma(number):
    number=int(number)
    number = format(number,',')
    return number
