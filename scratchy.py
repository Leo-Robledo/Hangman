'''
-how to add a new entry
-how to delete an entry
-how to access a special component of the tuple value
-create file to save memory
-persistant memory
'''

import pickle

def rate_winning(dict,player):
    rate = dict[player][1]/dict[player][0]
    return print("The rate of winning for ", player, "is ", round(rate,2))




# key = name of player, valuet is tuple(# of games played, #victories)
# history = {'dean':(12,4),'castiel':(10,6)}

# file_p5 = open('myhistorypickle,p', 'wb')
# pickle._dump(history,file_p5)
# file_p5.close()


# read to file
file_p5 = open('myhistorypickle,p','rb')
history = pickle.load(file_p5)
file_p5.close()

print(history)
# history['sam']= (90,85)
# print(history)
#
# # update the myhistorypickle
#
# file_p5 = open('myhistorypickle,p','wb')
# pickle.dump(history,file_p5)
# file_p5.close()



# rate_winning(history,'dean')
# rate_winning(history,'castiel')
#
# history['sam']= (9,8)
# print(history)
#
# for key in history.keys():
#     rate_winning(history,key)


# print(history)
# print(history['dean'])
# print(history['dean'][0])
# print(history['dean'][1])
# print(history['castiel'])
# print(history['castiel'][0])
# print(history['castiel'][1])

#add new entry to dictionary
# history['sam'] = (8,3)
# print(history)

# delete an entry
# del history['sam']
# print(history)
#
# rate_wins = history['dean'][1]/history['dean'][0]
# print("The rate of winning for Dean is ", rate_wins)
#
# rate_wins = history['castiel'][1]/history['castiel'][0]
# print(" The rate of winning for castiel is ",rate_wins)

