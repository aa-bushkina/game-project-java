
# Проверка совпадения количества портов с заявленным
def check(allPorts, ioPorts, groundPorts, uselessPorts):
    if len(allPorts) != 40:
        print("Недостаточное количество рабочих портов\n")
        exit(1)
    if len(ioPorts) != 26 or len(groundPorts) != 8 or len(uselessPorts) != 6:
        print("Недостаточное количество IO-портов\n")
        exit(1)

def clearPorts(ports):
    for i in range(0, 12):
        ports[i].lightOff()

def outForDebug(boolean):
    if boolean:
        print(1, end=' ')
    else:
        print(0, end=' ')