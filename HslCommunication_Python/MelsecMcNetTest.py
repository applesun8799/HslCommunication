from HslCommunication import MelsecMcNet

def printReadResult(result):
    if result.IsSuccess:
    	print(result.Content)
    else:
    	print("failed   "+result.Message)
def printWriteResult(result):
    if result.IsSuccess:
        print("success")
    else:
        print("falied  " + result.Message)

if __name__ == "__main__":
    melsecNet = MelsecMcNet("192.168.8.12",6002)

    printReadResult(melsecNet.ReadInt16("D300"))