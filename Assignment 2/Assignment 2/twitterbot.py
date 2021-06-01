# Jonathan Williams
# Assignment 2
# jwilli66@syr.edu
# 03/21/2021
import sys
import time
from urllib.error import URLError
from http.client import BadStatusLine
import json
from twitter import *
from functools import partial
from sys import maxsize as maxint
import networkx as nx 
import matplotlib.pyplot as plt 
from prettytable import PrettyTable
from CookBook import *

# Caps
maxFriends = 5000
maxFollowers = 5000
maxNodes = 100

# Token Authorizations
CONSUMER_KEY = '7YjYsiv2BFHEayteg6xOlrkII'
CONSUMER_SECRET = 'NI9691P5BzasF7U8mGDtuzI4RxE67NJ8tHUzDNG74o8aiMk7VD'
OAUTH_TOKEN = '1415807012-z9R1lUy19txxE6nZbHjrP5KHelO6vRZp84YrMQd'
OAUTH_TOKEN_SECRET = 'WNJMBcoyTwRNx30e1QRKzVnl0TXXW5cP0sjxQtEPSrugi'

# Select a starting point (Myself) and retireve friends as a list of ids and 
# followers as another list of ids using get_friends_followers_ids()

# Twitter API call from CookBook and Class Slides
t = Twitter(auth=(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET))
twitter_api = oauth_login() 

#################################################
# PART 1
# Starting point: My personal Twitter profile 
screen_name = 'CaptainSeli'
response = twitter_api.users.show(screen_name=screen_name) # Show user profile information
captainSeli = get_user_profile(twitter_api, screen_names="CaptainSeli") # Get user profile
profilejson = json.dumps(captainSeli) # json for starting profile
#################################################

# PART 2
# get_friends_followers_id() to retrieve friends and followers IDs Functions from Cookbook
follower_ids, friend_ids = get_friends_followers_ids(twitter_api, screen_name="CaptainSeli", friends_limit=5000, followers_limit=5000)
followersjson = json.dumps(follower_ids) # json for follower ids
friendsjson = json.dumps(friend_ids) # json for friend ids
# Two extremely long lists of User IDs ... 
friends_list = [1370025966639083524, 1234724472885858309, 2918147856, 1223950494932131841, 1222957955592740864, 1319477281186865153, 1244695921, 701328650, 1191083566433742848, 14524865, 1187751293995159556, 1189810275756707842, 1252797049604579328, 525286163, 244337418, 1354630111, 1049708514677940224, 114892021, 818844250603483136, 1121564275104014336, 1219828051929980929, 1153090425336532992, 953719814408716288, 283580474, 69045109, 799663488876453888, 1726854216, 22709122, 269591746, 761167885720956929, 1604233824, 2751369148, 830776194010382337, 2912142815, 345555611, 1101177276689993733, 2912007148, 749556217802993664, 1138518047684272129, 938874665027678208, 888414720641945601, 3113758555, 978887149838848000, 866389776823353344, 1003799005187461120, 912674755169411073, 962805206391156737, 1150068951709339648, 3775599503, 132655244, 159134455, 1128531016954417152, 349801895, 19663737, 1666247810, 1117526457973129219, 41691714, 15686103, 90378596, 964366681978978305, 995353487247425536, 372034656, 950940936296587269, 1514778284, 430555349, 1091096870695432194, 591459959, 999694966912831488, 1072992012809527297, 1080653884253564928, 631623005, 4149758438, 152515045, 2296287618, 1068929458286063621, 1881672758, 2150277690, 873360482228289536, 1052237738144088065, 391889164, 724329045815640065, 1033957933946691584, 856818692931375105, 879502220898598912, 948175412831621120, 1042970721205534726, 2477450022, 1026619477654470662, 3296270394, 15434743, 3096694050, 1000530569015545857, 1012036432666361857, 1005241338059808770, 8271722, 964772927710351360, 2271976452, 928870563237548033, 989346968697753610, 717391134, 757894392116051968, 955971628416032769, 983355738176344064, 455846456, 398821009, 633959365, 960169613882425344, 266898967, 957340787804688384, 954280593071714304, 883077623332655104, 15706061, 880464606791180288, 403027727, 933101553258393600, 947308973430050816, 843803524618182656, 937691797500956672, 81297605, 882242467722125313, 875101277482397697, 886883012218163200, 921886891460452352, 2261127930, 785582446330785792, 920610426198532096, 853562492844363777, 855573907146977280, 880423949103808513, 907627815981297667, 887090664927895555, 898243924304830470, 163640341, 902319807638405120, 875106697559379968, 868594219618889729, 39565695, 3003401062, 899322444326080512, 886677170504044546, 489558128, 856649841241468928, 885032758237646849, 873661855662833665, 2380667550, 881782744057090048, 875393667749556224, 870318978823880704, 881962308343287808, 880298883624177664, 299176360, 880478351651217410, 880155220680077312, 855058505862184960, 214130756, 879147578855747584, 572977864, 877891854305550336, 3066038331, 763816904809152512, 2342658948, 4925825848, 860574825881903104, 224769492, 780934537, 751866347349372928, 843923049112047621, 789112466953252864, 838899186464620544, 817730833079566337, 2936492967, 799661157590110209, 4380599413, 1868067930, 796161293182992385, 423844321, 14875001, 793155832879783936, 958158217, 797556030439821312, 1954032186, 93404430, 790934134357188608, 796461349492707331, 1057080500, 1536713088, 789144350190145537, 792728963399426052, 4128849202, 790991116418027522, 763091740270047232, 598588674, 1281389118, 4663232412, 783127966377181184, 766481766098100224, 2780878681, 240443440, 65960969, 149659057, 2757831192]
followers_list = [1370025966639083524, 1043193814377066496, 17446273, 59318218, 208711264, 255860782, 3288850229, 804220036525289472, 3350581005, 24457744, 1182041806294409221, 1235610347500974081, 1333800441260298241, 1303873858936737793, 1324810821550120962, 1339618330357936128, 1319689022508310530, 2990124384, 14123624, 783792992, 1331333951554777090, 1324389533186547714, 1352064843432472578, 2239350253, 31013444, 1354898820400877571, 1282418324228337665, 3185716686, 53596405, 17494010, 65431632, 38233510, 984819646082797568, 4329898994, 1155233445603418115, 353253058, 956779022, 180107694, 1323730225067339784, 1300848298409037831, 803694179079458816, 978265628426432512, 1349170292564905988, 1349149096909668363, 712179042, 1162002819592982531, 130496027, 1038082275689340928, 18759851, 583172153, 829796055344517120, 19637934, 57084769, 1171755060, 11212862, 977298824489140224, 36618079, 1313780486062452736, 51241574, 261375916, 2357400848, 395451664, 2356335972, 1128783590677012480, 345986986, 569607215, 286256231, 293046977, 65937781, 23544596, 90672134, 1277870713135935488, 827905139101073408, 3775599503, 46726590, 3021460584, 1199000687184531456, 15004694, 74669397, 1214242499616595969, 1114917500, 900868190, 602317143, 48776603, 322751087, 2785866648, 1290215481190895616, 1173782564, 1301575216791945219, 22771961, 22548838, 347831597, 974306250396717057, 1145323862969790464, 14772775, 2537867839, 1243560408025198593, 2731627149, 1173487706359259136, 1134552730146500608, 30354991, 36668057, 356866129, 4200834237, 1053450787, 15796148, 1100933556522508288, 74286565, 2381898944, 1079104563280527364, 713839291210792960, 1284974744727511040, 1285163954424217600, 770400481965408256, 19373710, 176976565, 400286802, 763118866226634752, 767788995962998784, 114892021, 1234682312, 884536647542607873, 286523226, 1009467377585704962, 47285504, 926620369, 931468093, 879147821915615233, 14247236, 13393052, 26657119, 36711022, 230527949, 225235528, 279390084, 1604931252, 500042487, 939091, 739192329978941440, 1252797049604579328, 221454258, 1180851786921451526, 244337418, 808741231, 3121310627, 612782611, 26280712, 1243248298317746176, 22948057, 917210408, 34266258, 626592883, 354515115, 162610681, 3027366130, 2515725115, 758041924036997120, 1085890740100784129, 17064600, 19658936, 146569971, 40899383, 305012429, 1200042964350885888, 1158827140151951363, 3840534676, 78431026, 148529707, 1195016015047987201, 19638927, 45553126, 1153090425336532992, 25629019, 250831586, 1182979873, 350379608, 824333698728333312, 4839817864, 3027082515, 956692683661107201, 927315681502253056, 59414975, 3165817215, 1189810275756707842, 4499223455, 2596123165, 16513335, 821102114, 837987264, 15496738, 1048018930785083392, 15222083, 913203265466257408, 4516315185, 117652722, 333690275, 1088189605885620224, 26906309, 562823652, 2912007148, 112726313, 14652182, 828119474, 4350793648, 517441231, 2325831067, 3002056342, 1604444052, 1074815357519577094, 1138518047684272129, 866426699193491459, 938874665027678208, 25029495, 443215941, 1009177298782875648, 28187205, 1067891123312455680, 36751532, 1119309623649943552, 110365072, 824066331167199232, 824338843327361024, 970207298, 34321294, 830953400, 950491178, 357606935, 57903424, 1047643163895238660, 2240082462, 2232827756, 105929745, 3383806043, 912674755169411073, 59130827, 5988062, 5402612, 3108351, 163436555, 15113565, 8775672, 54885400, 19611483, 190403384, 458773316, 829095470873997317, 15234657, 14922225, 38232487, 745461850880413696, 14294848, 3306440342, 839318427009417217, 822475925422034944, 158414847, 846314880378585088, 783362721819406336, 1446004207, 768049658, 1666247810, 2300848045, 2420944560, 1020742989558239232, 13201312, 888414720641945601, 29221344, 1013203958922346496, 937007682451591169, 1039566779050323968, 278365614, 46146200, 2724711809, 301185491, 18209635, 978887149838848000, 327989347, 178362255, 257076658, 41148474, 1905181502, 46453032, 20119483, 138203134, 1126545296, 152805785, 90378596, 54059560, 209938251, 995353487247425536, 964366681978978305, 15686103, 1024997290040324101, 46335511, 701328650, 1091096870695432194, 18948541, 35827447, 22029553, 110798209, 132655244, 71019945, 830487828718985216, 192890922, 950940936296587269, 82208992, 758006690356695040, 841775263935483904, 718938043579637760, 616454138, 430555349, 3434345169, 5880462, 48966037, 986964352912814080, 925429290581229568, 965477998790135808, 1051131309806866433, 152515045, 982751483589472256, 424914514, 320422381, 241382835, 75974281, 2893511188, 65289126, 984234517308243968, 865635702121185280, 71779837, 121258930, 2437167086, 2895961351, 125688706, 454340464, 29758446, 14207199, 821218695502565376, 11928542, 7157132, 1345471728, 18927441, 879502220898598912, 2238810722, 3897436340, 1951062752, 726631312589606912, 2384991482, 1948208700, 19170041, 247407637, 3433407921, 15434743, 1935675295, 3421762703, 63062645, 989081467, 2470442620, 2820596422, 2851345879, 717391134, 266020924, 2342658948, 17088779, 1884603416, 360196369, 26599573, 308693201, 983355738176344064, 570111831, 11344472, 197052458, 487730016, 89228085, 22527376, 425871040, 455846456, 81297605, 3369308747, 886396579984404480, 40749456, 478910055, 22461427, 246915368, 325633686, 1330253916, 15706061, 1337311717, 275722475, 48519871, 2787450546, 47349679, 3250976195, 44100037, 749671856924307456, 1959556592, 2334193741, 709221044633128960, 625022363, 815836615901937664, 41038781, 22940219, 2962868158, 13850422, 28785486, 45055696, 738028185397383168, 898243924304830470, 1482779976, 45125325, 39565695, 868594219618889729, 760049781628559361, 32789224, 824366696517562369, 487736815, 766481766098100224, 838899186464620544, 873661855662833665, 554487897, 596572961, 761167885720956929, 18732790, 611941828, 729468343, 3375660701, 824726751209066496, 824119137031094273, 297925007, 9300262, 55948054, 32871086, 880423949103808513, 2380667550, 880884489999851521, 863439662336978944, 1195067004, 759251, 16303106, 2233154425, 3852772337, 4107438429, 879147578855747584, 2839430431, 96879107, 5162861, 23363326, 299176360, 874667362603081729, 843909367007272963, 2293263018, 4925825848, 72571040, 224769492, 24025736, 216776631, 5392522, 21884158, 5741722, 398323499, 45668062, 454237315, 473493882, 48294321, 166739404, 789067176678453248, 807095, 2467791, 51105297, 193771633, 16135536, 16664681, 14647570, 2359926157, 824190260338954240, 824342512844222464, 237845487, 824467746436120576, 824450140131975168, 62513246, 813286, 3240143771, 824400401797619712, 824277855832014848, 2989089036, 878881230, 824320219866923018, 824153054731759617, 824157441248153600, 824116562768621568, 824126001936474113, 824028553067032576, 824270573203292160, 824332206952714240, 824264707641057281, 824315778866417664, 824137712286441472, 824139632354988033, 824473943931293697, 823565852922576897, 4757735607, 736172947551977472, 3116112371, 553552636, 3429064114, 14875001, 729479918074134529, 1378911769, 799663488876453888, 3526382061, 799661157590110209, 4585086136, 3426803615, 735599078747320325, 3325229602, 2966657308, 17781165, 1954032186, 34554134, 19515424, 19402238, 8963722, 16895274, 16817883, 59265808, 3873936134, 53919756, 469689725, 709226545, 66369181, 10126672, 3223751774, 1057080500, 794800315363115008, 367284950, 61593861, 2209268101, 351752318, 3236659668, 2225764458, 3192600414, 1603439773, 2206757473, 134250342, 1265727487, 20273398, 15880163, 790991116418027522, 763091740270047232, 14584200, 16736535, 47787563, 214792523, 235348644, 158642445, 42993311, 2434676702, 26281970, 2218177956, 598588674, 18795591, 41381939, 29442313, 15078840, 11214332, 1536713088, 93404430, 19721402, 110783489, 857520001, 19802879, 304679484, 8623332, 2215461732, 2303822179, 1281389118, 1699593492, 16890969, 3342069310, 1222746529, 2889355460, 211879310, 732654649442963456, 726869958, 4663232412, 273405670, 4373450308, 15473958, 19725644, 37710752, 15431856, 160974322, 113696592, 112511880, 186259984, 391444599, 20475491, 729547316, 13298072, 726804680269926400, 306664735, 309366491, 3065618342, 3301952815, 20106852, 1868067930, 240443440, 3096694050, 15643730, 2713285249, 34743251, 65960969, 23645599, 11348282, 3621849439, 2918147856, 2780878681, 3251176305, 25374930, 36803580, 555532681, 2965146125, 2757831192]
# Use the above two lists to find reciprocal friends. These will be the distance-1 friends

# Helper function to get the intersection of two lists
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

###################################################

# PART 3
# Function to find the reciprocal friends, distance-1
def reciprocal(user):
    # Get the friends/followers ids
    friends, followers = get_friends_followers_ids(twitter_api, user_id=user, friends_limit=5000, followers_limit=5000)
    # Get the reciprocals
    reciprocal_friends = intersection(friends, followers)
    return reciprocal_friends 

# Call to reciprocal
reciprocal_list = reciprocal(1415807012)
##################################################

# PART 4
# Loop through the reciprocal_friends list and call a count function to determine which 5 
# have the most followers
def topFive(reciprocal_list):
    # Make a list of user dictionaries and pull the profile information to get the follower_count
    user_id_dictionary_list = get_user_profile(twitter_api, user_ids=reciprocal_list)
    count_of_followers = [] #Empty List to build into
    # Loop through the dictionary list to retrieve the keys for user_id and follower_count
    for key in user_id_dictionary_list:
        count_of_followers.append((user_id_dictionary_list[key]["id"], user_id_dictionary_list[key]["followers_count"]))
    # Sort the list from the most followers to the least
    sorted_count_followers = sorted(count_of_followers, key=lambda x: x[1], reverse=True)
    # Get the top five off the sorted list
    topFiveSorted = sorted_count_followers[:5]
    
    # Unzip the follower_id from the follower count
    # Try Except for cases where the user doesn't have reciprocal friends :'(
    try: 
        follower_id, count_followers = list(zip(*topFiveSorted))
    except(ValueError):
        print("Value Error Hit - Moving to next item...")
        # Pass an empty list to the call if the user has 0 reciprocal friends and continue to the next user
        return []
        pass 

    return follower_id
# Call to topFive 
topFive(reciprocal_list)
##################################################

# PART 5: Crawler
# Repeat the above process for distance-1 to distance-n until you get at least 100 users/nodes
# Crawler modified from CookBook
def crawler(twitter_api, user_id=None, limit=5000):
    # Get reciprocal friends
    friends_reciprocal = reciprocal(screen_name)
    # Get reicprocal friends top 5
    topFive2 = topFive(friends_reciprocal)
    # Insert that top 5 into the next_queue
    next_queue = topFive2

    ######################################
    # PART 6 Graph Creation: Root Node ID: 1415807012 (My personal twitter)
    rootList =[1415807012, 1415807012, 1415807012, 1415807012, 1415807012]
    depth1 = list(zip(rootList, next_queue))
    social_network = nx.Graph()
    social_network.add_edges_from(depth1)
    # Draw the graph of the root node and its first 5 most popular friends
    nx.draw(social_network)
    plt.show()
    ######################################

    depth = 1 # Root Node
    maxDepth = 3 # 5^3 to get the first 125 nodes (Only care about the first 100)
    while depth < maxDepth:
        (queue, next_queue) = (next_queue, []) # queue becomes the top five friends and next_queue becomes empty list
        # Loop through all depths of friends
        for i in queue:
            # Get the next round of reciprocal friends
            friends_reciprocal1 = reciprocal(i)
            # Get the next round of top fives
            topFive3 = topFive(friends_reciprocal1)
            # Get the depth-n nodes added to the Graph
            depthN = list(zip([i, i, i, i, i], topFive3))
            # This completes the social network
            social_network.add_edges_from(depthN)
            next_queue += topFive3      
        depth = depth + 1

    ###################################
    # PART 6 Final Social Network Graph
    nx.draw(social_network)
    plt.show()
    ###################################
    return social_network

# Call the crawler for passing into the Part 7 functions
social_network = crawler(twitter_api, user_id=1415807012, limit=5000)
################################################# 

# PART 7 Diameter and Avg Distance from Networkx PDF sections 3.23 and 3.51
# Average Shortest Distance taken from Networkx PDF
avgDistance = nx.average_shortest_path_length(social_network, weight=None, method=None)
# Diameter taken from Networkx PDF
diameter = nx.diameter(social_network, e=None, usebounds=False)
print("The Average Distance is:")
print(avgDistance)
print()
print("The diameter is:")
print(diameter)
print()
# Number of nodes and edges
print("The number of nodes:")
print(social_network.number_of_nodes())
print()
print("The number of edges:")
print(social_network.number_of_edges())
###################################