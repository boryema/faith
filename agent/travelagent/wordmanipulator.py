import nltk


def formatargvalues(userresponselist):
    value = {}
    airportName = {}
    travelDate = {}
    demAirport= ''
    #userresponselist = userresponselist.split()
    userResponseListLen = len(userresponselist)
    # print userresponselist
    # print userResponseListLen

    for i in range(userResponseListLen):
        tokenizedSentenceUserResponse = nltk.word_tokenize(userresponselist[i])
        tokenizedSentenceUserResponsetag = nltk.pos_tag(tokenizedSentenceUserResponse) #Tokenizing the sentence
        tokenizedSentenceUserResponsetaglen = len(tokenizedSentenceUserResponsetag) #Length of tokenized sentence

        for j in range(tokenizedSentenceUserResponsetaglen):
            indexForTheTagName = 0
            indexForTheTagValue = 1

            #Getting the airportName
            if(tokenizedSentenceUserResponsetag[j][indexForTheTagValue] == 'NNP'):

                demAirport = demAirport+ " " + tokenizedSentenceUserResponsetag[j][indexForTheTagName]
                demAirport = demAirport.strip()

                airportName = {"destinationairport": demAirport}
                value.update(airportName)

            # Getting the travelDate
            if (tokenizedSentenceUserResponsetag[j][indexForTheTagValue] == 'CD'):
                travelDate = {"traveldate": tokenizedSentenceUserResponsetag[j][indexForTheTagName]}
                value.update(travelDate)

    return value
