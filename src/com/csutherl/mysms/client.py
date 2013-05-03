from mysms import Mysms
import json

class Client():

    __MySms = False

    def login(self):
        # your API key
        api_key = 'YOUR_API_KEY_HERE'
        # initialize class with apiKey and AuthToken(if available)
        self.__MySms = Mysms(api_key)

        # lets login user to get AuthToken
        login_data = {'msisdn': 'YOUR_PHONE_NUMBER', 'password': 'YOUR_PASSWORD'}

        login = self.__MySms.ApiCall('json', '/user/login', login_data, False) # providing REST type(json/xml), resource from http://api.mysms.com/index.html and POST data
        print login
        user_info = json.loads(login)

        if(user_info['errorCode'] is not 0):
            raise Exception('Failed to login. Error code is ' + str(user_info['errorCode'])) # Explanation of codes is here: http://api.mysms.com/resource_User.html#path__user_login.html

        print user_info # debug login data

        self.__MySms.setAuthToken(user_info['authToken']) # setting up auth Token in class (optional)

    def getContacts(self):
        req_data = {} # no required data
        usercontacts = self.__MySms.ApiCall('json', '/user/contact/contacts/get', req_data) # calling method ApiCall
        print usercontacts # print result

    def sendText(self):
        # recipients must have '91' prefix for US numbers
        req_data = {
            "recipients": ['TEST_PHONE_NUMBER'],
            "message": 'hi',
            "encoding": 0,
            "smsConnectorId": 0,
            "store": True,
        }

        sendsms = self.__MySms.ApiCall('json', '/remote/sms/send', req_data) # calling method ApiCall
        print sendsms # print result

if __name__ == "__main__":
    c = Client()
    c.login()
    c.getContacts()
    # c.sendText()
