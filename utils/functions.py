import datetime
def convertdates(month=1,day=1,year=21):
    month_dict={1:'Jan',2:'Feb',3:'Mar',4:'Apr',5:'May',6:'Jun',7:'Jul',8:'Aug',9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    backtrader_date = datetime.datetime.strptime(f'{month}-{day}-{year}', '%f-%d-%y')
    str_month=month_dict[month]
    binance_date=f'{str_month} {day}, {year}'
    return backtrader_date, binance_date
