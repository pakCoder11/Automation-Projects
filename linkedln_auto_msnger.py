from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def LoginToLinkedln(browser,username,password):
   browser.get("https://www.linkedin.com/login")  # open the Linkedln login page
   elementID = browser.find_element_by_id("username")  # find id='username'
   elementID.send_keys(username)  # type username/email in username textfield

   elementID = browser.find_element_by_id("password")
   elementID.send_keys(password)  # type password in password textfield
   elementID.submit()
def LinkedlnWebAutomation(browser):
   browser.get("https://www.linkedin.com/messaging/compose-group/")  # id="messaging-nav-item"
   Participants_List = ['ahsan ali']
   MessageToSent = "This is a message from Muhammad Saad Khan to Ahsan Ali using Linkdln web automation bot."
   GroupName = "Linkedln Automation testing"  # <input id="ember59-search-field" class="msg-connections-typeahead__search-field msg-connections-typeahead__search-field--no-recipients ml1" placeholder="Type the participant names" role="combobox" aria-autocomplete="list" aria-owns="ember59-suggestions-menu" aria-expanded="true" type="text" data-ember-action="" data-ember-action-60="60" aria-activedescendant="urn:li:fs_miniProfile:ACoAACf_G0cBafoNQ_PJmsfkmq9ICq_Chj_-sgY">
   # ConservationGroupID = browser.find_element_by_class_name("msg-connections-typeahead")
   ConservationGroupID = browser.find_element_by_class_name("msg-connections-typeahead__search-field")
   GroupNameID = browser.find_element_by_class_name("artdeco-text-input--input")
   NextButtonID = browser.find_element_by_class_name("msg-group-form__next-button")
   for Participant in Participants_List:
      ConservationGroupID.send_keys(Participant)
      ConservationGroupID.send_keys(Keys.ENTER)
   GroupNameID.send_keys(GroupName)
   NextButtonID.click()
   MessageTextBoxID = browser.find_element_by_class_name("msg-form__contenteditable")
   SendButtonID = browser.find_element_by_class_name("msg-form__send-button")
   MessageTextBoxID.send_keys(MessageToSent)
   SendButtonID.click()

if __name__ == '__main__':
   browser = webdriver.Chrome()
   LoginToLinkedln(browser,"saadkhang106031@gmail.com","zzxxcc1234")
   LinkedlnWebAutomation(browser)

'''
def readEmailAndPassFromFile():
   file = open('config.txt')
   lines = file.readlines()
   return lines
data = readEmailAndPassFromFile()
username = data[0]
password = data[1]
browser = webdriver.Chrome()

# Navigate to the application home page
browser.get("https://www.linkedin.com/login") #open the Linkedln login page
elementID = browser.find_element_by_id("username") #find id='username'
elementID.send_keys(username) #type username/email in username textfield

elementID = browser.find_element_by_id("password")
elementID.send_keys(password) #type password in password textfield
elementID.submit()

browser.get("https://www.linkedin.com/messaging/compose-group/") #id="messaging-nav-item"
Participants_List = ['ahsan ali']
MessageToSent = "This is a message from Muhammad Saad Khan to Ahsan Ali using Linkdln web automation bot."
GroupName = "Linkedln Automation testing" #<input id="ember59-search-field" class="msg-connections-typeahead__search-field msg-connections-typeahead__search-field--no-recipients ml1" placeholder="Type the participant names" role="combobox" aria-autocomplete="list" aria-owns="ember59-suggestions-menu" aria-expanded="true" type="text" data-ember-action="" data-ember-action-60="60" aria-activedescendant="urn:li:fs_miniProfile:ACoAACf_G0cBafoNQ_PJmsfkmq9ICq_Chj_-sgY">
#ConservationGroupID = browser.find_element_by_class_name("msg-connections-typeahead")
ConservationGroupID = browser.find_element_by_class_name("msg-connections-typeahead__search-field")
GroupNameID = browser.find_element_by_class_name("artdeco-text-input--input")
NextButtonID = browser.find_element_by_class_name("msg-group-form__next-button")
for Participant in Participants_List:
   ConservationGroupID.send_keys(Participant)
   ConservationGroupID.send_keys(Keys.ENTER)
GroupNameID.send_keys(GroupName)
NextButtonID.click()
MessageTextBoxID = browser.find_element_by_class_name("msg-form__contenteditable")
SendButtonID = browser.find_element_by_class_name("msg-form__send-button")
MessageTextBoxID.send_keys(MessageToSent)
SendButtonID.click()
'''
