# $language = "Python"
# $interface = "1.0"

import time

# True desc
# False asc
def sortedDictValues(adict,sortType):
    keys = adict.keys()
    keys.sort(reverse = sortType)
    return map(adict.get, keys)

def count():
    # define time here
    # today: just do not modify it
    # someday: like '2013-09-14'
    # somedays: like '2013-09-14,2013-09-15,2013-09-16,2013-09-17'
    date = '2013-10-09'

    objTab = crt.GetScriptTab()
    objTab.Screen.Synchronous = True
    objTab.Screen.IgnoreEscape = True

    # base shell
    pass_add_prefix = './gmalipay.sh kabaoprodserver \'grep "CreatePass,success,Y,'
    taobao_add_prefix = './gmalipay.sh kabaoprodserver \'grep "SyncTBVoucherPass_add,success,Y,'
    all_pass_add_prefix = './gmalipay.sh kabaoprodserver \'grep "CreatePass,success,Y" logs/kabaoprod/kabaoprod-pass-digest.log'
    all_taobao_add_prefix = './gmalipay.sh kabaoprodserver \'grep "SyncTBVoucherPass_add,success,Y" logs/kabaoprod/kabaoprod-pass-digest.log'

    all_call_prefix = './gmalipay.sh kabaoprodserver \'grep "CreatePass,start" logs/kabaoprod/kabaoprod-pass-digest.log'

    middle = '" logs/kabaoprod/kabaoprod-pass-digest.log'
    suffix = ' -c \' | awk -F \':\' \'{sum=sum+$1} END {print \"count='
    endCount = '=\"sum}\''

    # date
    dateList = []
    if len(date) != 0:
        if(date.find(',') >= 0):
            dateList = date.split(',')
        else:
            dateList.append(date)

    # data
    merchantTable = {}
    shellDic = {}

    # merchant Data
    for line in open('merchant.txt', 'r'):
        tempList = line.split(',')
        merchantTable[tempList[0]] = tempList[1].replace('\n', '')

    # multi-day log count
    if(len(dateList) > 0):
        for tempDate in dateList:
            dateShellDic = {}
            for merchant in merchantTable:
                # taobao data
                if merchant == '2088001159940003':
                    shell_coupon = taobao_add_prefix + merchant + middle + '.' + tempDate + suffix + tempDate + '=' + merchant + merchantTable[merchant] + '卡券' + endCount
                    shell_travel = pass_add_prefix + merchant + middle + '.' + tempDate + suffix + tempDate + '=' + merchant + merchantTable[merchant] + '旅行' + endCount
                    dateShellDic[tempDate + '-' + merchant + 'coupon'] = shell_coupon
                    dateShellDic[tempDate + '-' + merchant + 'travel'] = shell_travel
                # normal data
                else:
                    shell = pass_add_prefix + merchant + middle + '.' + tempDate + suffix + tempDate + '=' + merchant + merchantTable[merchant] + endCount
                    dateShellDic[tempDate + '-' + merchant] = shell
            # count all
            tempAllPassShell = all_pass_add_prefix + '.' + tempDate + suffix + tempDate + '=MAPI-OPENAPI成功总数   ' + endCount
            dateShellDic[tempDate + '=all-pass'] = tempAllPassShell

            tempAllTaobaoShell = all_taobao_add_prefix + '.' + tempDate + suffix + tempDate + '=淘宝卡券成功总数        ' + endCount
            dateShellDic[tempDate + '=all-taobao'] = tempAllTaobaoShell

            tempAllCallShell = all_call_prefix + '.' + tempDate + suffix + tempDate + '=MAPI-OPENAPI调用总数   ' + endCount
            dateShellDic[tempDate + '=all-call'] = tempAllCallShell

            shellDic[tempDate] = dateShellDic
    # today log count
    else:
        for merchant in merchantTable:
            # taobao data
            if merchant == '2088001159940003':
                shell_coupon = taobao_add_prefix + merchant + middle + suffix + 'today=' + merchant + merchantTable[merchant] + '卡券' + endCount
                shell_travel = pass_add_prefix + merchant + middle + suffix + 'today=' + merchant + merchantTable[merchant] + '旅行' + endCount
                dateShellDic[merchant + 'coupon'] = shell_coupon
                dateShellDic[merchant + 'travel'] = shell_travel
            # normal data
            else:
                shell = pass_add_prefix + merchant + middle + suffix + 'today=' + merchant + merchantTable[merchant] + '=today' + endCount
                dateShellDic[merchant] = shell

        # count all
        tempAllPassShell = all_pass_add_prefix + suffix + 'today=MAPI+OPENAPI成功总数   ' + endCount
        dateShellDic['today=all-pass'] = tempAllPassShell

        tempAllTaobaoShell = all_taobao_add_prefix + suffix + 'today=淘宝卡券成功总数        ' + endCount
        dateShellDic['today=all-taobao'] = tempAllTaobaoShell

        tempAllCallShell = all_call_prefix + suffix + 'today=MAPI+OPENAPI调用总数   ' + endCount
        dateShellDic['today=all-call'] = tempAllCallShell

        shellDic['today'] = dateShellDic

    # execute shell and get initial output data
    prompt = "count="
    tempResultDic = {}
    for subShellDicKey,subShellDicValue in shellDic.items():
        tempSubResultDic = {}
        for curShellKey,curShellValue in subShellDicValue.items():
            objTab.Screen.Send(curShellValue + '\r')
            objTab.Screen.WaitForString(prompt)
            objTab.Screen.ReadString(prompt)
            resultStr = objTab.Screen.ReadString('$').replace('[log@log-60-1  zue.alipay.com /home/log]', '')
            resultStr = resultStr.replace('\n\r', '')
            resultStr = resultStr.replace('\r', '')

            # using count to be key
            tempArray = resultStr.split('=')
            tempKey = int(tempArray[2])
            # if key exists,change to plus or plus plus
            if(tempSubResultDic.has_key(tempKey)):
                tempKey = tempKey + 1
                if(tempSubResultDic.has_key(tempKey)):
                    tempKey = tempKey + 1

            tempSubResultDic[tempKey] = resultStr

        # sort data and add to result
        tempResultDic[subShellDicKey] = sortedDictValues(tempSubResultDic,True)

    # handle and sort data
    finalResult = sortedDictValues(tempResultDic,False)

    fp = open('output.txt.'+time.strftime('%Y-%m-%d',time.localtime(time.time())), 'w')
    for subResult in finalResult:
        for line in subResult:
            fp.write(line.encode('utf8') + '\n')
    fp.close()

def main():
    count()

main()