import re
import time
def WriteDataInTextFile(tel_list,mob_list):
    file1 = open('mobile_numbers_list.txt','a')
    file2 = open('telephone_numbers_list.txt','a')
    for items in mob_list:
    	if(len(items)==10):
            file1.write(items)
    for items in tel_list:
    	if(len(items)==10):
            file2.write(items)
    file2.write("\n")
    file1.write("\n")
    file1.close()
    file2.close()
def GetThreeMiddleDigits(string):
    '''this function is used to get the middle digits of the number '''
    number = re.sub('\D','',string)
    three_middle_digits = number[3:6]
    if str(three_middle_digits) in ['218','217','216','215','252','253','251','250','254','255','242','240','239','243','237','238','290','291','292','293','294','309','310','308','311','312','259','253','336','337','338','339','330','331','332','376','272','311','375','373','383','385','386','391','392','393','403','404','405','406','420','425','430','431','451','452','453','454','470','473','474','475','490','491','497','517','518','519','520','521','580','539','540','538','565','564','','596','597','599','632','633','634','660','626','627','628','629','680','681','682','731','730','732','733','734','747','748','771','710','711','712','715','786','787','789','785','784','745','802','803','804','805','806','807','808','944','945','946','947','943','942','941','948','980','981','982','983','971','972','973','970','969']:
        return True
    else:
        return False
def ReadDataFromTxtFile(fileName): #read data from .txt file
    file = open(fileName,"r")
    data = file.readlines()
    file.close()
    return data
if __name__ == '__main__':
    TELEPHONE_NUM_LIST = []
    MOBILE_NUM_LIST = []
    file_to_input = input("Enter File name : ")
    print("Please wait for a moment...")
    time.sleep(3)
    land_line_numbers = ReadDataFromTxtFile('data.txt')
    for lln in land_line_numbers:
        three_middle_digits = GetThreeMiddleDigits(lln)
        if three_middle_digits == True:
            MOBILE_NUM_LIST.append(lln)
            print(lln,' is a mobile number')
        else:
            TELEPHONE_NUM_LIST.append(lln)
            print(lln, ' is a telephone number')
    WriteDataInTextFile(TELEPHONE_NUM_LIST,MOBILE_NUM_LIST)
    print("Thanks...")
