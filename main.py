import sys
from twython import Twython
import time
import json
import os
import re

# Secret Keys
apiKey = "qaiHFqWKyHuHWibbBOuJl3grj"
apiSecret = "mQ0w0YyeY5z5WkkDByI3TG9kI9OWzmmKGoe9A9BLEPeAhbm6Sj"
accessToken = "832293691888918533-6Mjald6xTQoGQw5UsLjyUNqkYbo1Ipo"
accessTokenSecret = "PKJJzwCU05e7UHgRtoRdVTYDRjZ48ksewf4arpQwlw18S"

#tweetStr="Hey, Jesse White!"
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
#api.update_status(status=tweetStr)

tweet = api.get_mentions_timeline()
results = api.search(q="@project_mayo",count = 10);
all_tweets = results['statuses']
song_List = []
reading = True
content = ""
for tw in all_tweets:
    if reading:
        if tw['text'].find("NAME:")> 0:
            song_List.append(tw['text'])
    if tw['text'].find("DONE") < 0:
        reading = False

song_List.reverse()
for x in song_List:
    content = content + x

#everything is in content
songNameLoc = content.find("NAME:")+6
toLoc = content.find("TO")

songName = content[songNameLoc:toLoc-1]
print(songName)

toLoc += 4
#print(content[toLoc])
recp = content[toLoc:content.find("!")]
print(recp)

end = content.find("DONE")
notes = content[content.find("!")+2:end]
print(notes)
#The song that is going to be played


#Name of file
songName = songName.replace(" ","_")
# print(songName)

#conversion section
notes = notes.replace ("&lt;","<")
notes = notes.replace ("&gt;",">")

print(songName)
test = songName + ".txt"
test_object = open(test,"w")
test_object.write(notes)
test_object.close()
os.system("./alda play -f "+test)
