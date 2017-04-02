import os
from grab import Grab

def grab_single_page():
    #Initialize a Grabber object
    g=Grab()
    #Go to the webpage where the form exists
    g.go('https://gsa.gov/portal/staffDirectory/searchStaffDirectory')
    
    #Shoot up the chrome web inspector. Check what is the name of the input box in the HTML
    #Enter that here:
    inputbox_name='associateSearchVO.criteriaVOs[0].attValue'
    
    #Set some string to the input box
    g.set_input(inputbox_name,'A')
    
    #Submit the FORM.
    g.submit()

    #Capture the response
    response=g.doc
    
    #Convert it into BSoup HTML Tree
    soup=BeautifulSoup(response.body)
    
    #Parse the relevant information from the content
    relevant_info=parse_content(soup)


def grab_multiple_pages():

    for firstchar in string.ascii_uppercase:
        for secondchar in string.ascii_uppercase:
            #We will pass the search strings as AA,AB,AC,AD,....
            # as there is a cap of 250 results being returned.
            searchstr=firstchar+secondchar
            g.set_input('associateSearchVO.criteriaVOs[0].attValue', searchstr)
            g.submit()

            response=g.doc()
            soup=BeautifulSoup(response.body)
            relevant_info=parse_content(soup)


def parse_content(soup)
    #Write your own function for parsing the content.

