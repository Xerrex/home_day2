import requests,time

class Iss_API(object):
    base_url    = "http://api.open-notify.org/iss-now.json"
    base_urlnow = "http://api.open-notify.org/iss-pass.json"

    def iss_info(self,latitude,longitude):
        """
        the function return the passing of the
         International space station at current location as per this cooordinates
        :param lattitude: of curent location
        :param longitude: of current location
        :return: dictionary of iss details as per the passed coordinaates
        """
        coordinates= {"lat":latitude , "lon":longitude}
        response = requests.get("http://api.open-notify.org/iss-pass.json",params=coordinates)
        data = response.json()
        print (data)

        return data


    def user_input_coordinates(self,option_msg='Enter your option'):
        print('------------------------------------------------------')
        print('----choose one of the cities or enter custom----------')
        print('-----1 Nairobi       :1.2921° S, 36.8219° E    -------')
        print('---  2 Mombasa       :4.0435° S, 39.6682° E    -------')
        print('---  3 Kisumu        :0.0917° S, 34.7680° E    -------')
        print('---  4 Thika         :1.0388° S, 37.0834° E    -------')
        print('---  5 Busia         :0.4608° N, 34.1115° E    -------')
        print('-----6 Kampala       :0.3476° N, 32.5825° E    -------')
        print('-----7 Dar-es-salam  :6.7924° S, 39.2083° E    -------')
        print('-----8 Enter custom coordinates    -------')
        print('------------------------------------------------------')
        option = input(option_msg)

        if int(option)==1:
            self.iss_info(-1.2921,36.8219)
        elif int(option)==2:
            self.iss_info(-4.0435, 39.6682)
        elif int(option)==3:
            self.iss_info(-0.0917, 34.7680)
        elif int(option)==4:
            self.iss_info(-1.0388, 37.0834)
        elif int(option)==5:
            self.iss_info(0.4608, 34.1115)
        elif int(option) == 6:
            self.iss_info(0.3476, 32.5825)
        elif int(option) == 7:
            self.iss_info(-6.7924, 39.2083)
        elif int(option) == 8:
            lat = input("Enter the Latittude:")
            lon = input("Enter the Longitude")
            self.iss_info(lat,lon)
        else:
            option2 = input('Do you want to go_back,exit,Go to Main Menu[g/e/m]')
            option2 = str(option2)
            if option2=='g':
                self.user_input_coordinates()
            elif option2=='e':
                exit()
            elif option2=='m':
                self.user_menu()
            else:
                self.user_input_coordinates('choose from menu:Enter your option')
                return 'invalid option'








    def iss_position(self,url=base_url):
        """
        this function returns details  of the International Space Station
        :return:{coordiantes,time}
        """

        response = requests.get(url)
        data = response.json()

        #print(data)
        #message = data['message']
        coordinates = data['iss_position']
        timestamp = data['timestamp']
        datetime=time.ctime(timestamp)

        return {"coordinates": coordinates, "was_there_on": datetime}

    def user_input_process(self,option):
        option=int(option)

        if option==1:
            print(self.iss_position())
        elif option==2:
            self.user_input_coordinates()
        elif option==3:
            yes_no= input('Are you sure you want to exit[y/n]:')
            if str(yes_no)=='n':
                self.user_menu('welcome back:enter your choice')
            elif str(yes_no)=='y':
                exit()
            else:
                self.user_menu()
        else:
            self.user_menu('Choose valid option from menu')




    def user_menu(self,option_msg='enter your choice: '):
        print('------------------------------------------------')
        print('Welcome i am ISS:International Space Station\n  ')
        print('----------what do you want to do----------------')
        print('---  choose                                -----')
        print('---  1. to know where i am the             -----')
        print('---  2. find out when i will be at a place -----')
        print('-    3. to exit                            -----')
        print('------------------------------------------------')
        print('------------------------------------------------')
        option=input(option_msg)
        self.user_input_process(option)



iss = Iss_API()
iss.user_menu()




