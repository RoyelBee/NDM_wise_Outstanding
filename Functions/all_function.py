import Functions.all_library as lib

conn = lib.db.connect('DRIVER={SQL Server};'
                        'SERVER=137.116.139.217;'
                        'DATABASE=ARCHIVESKF;'
                        'UID=sa;PWD=erp@123')

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