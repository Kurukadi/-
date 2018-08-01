import vk
import time
from keys import *

version = '5.50'

minute = 60

session = vk.AuthSession(app_id = bot_app_id, user_login = bot_login, user_password = bot_password, scope = 'messages, groups')
vk_api = vk.API(session, v = version)

print('Authorization was successful')

def send_message(userID):
	vk_api.messages.send(user_id = userID, message ='', attachment = we_know)

def show_users(groupID):
	users = vk_api.groups.getMembers(group_id = groupID, sort = 'id_asc')
	return users

def show_banned(groupID):
	banned_users = vk_api.groups.getBanned(group_id = groupID)
	return banned_users['items']

base_users = show_users(test_group_id)
base_count_of_members = base_users['count']

while True:
	print('start iteration')
	black_list = []

	actualy_users = show_users(test_group_id)
	actualy_count_of_members = actualy_users['count']

	for i in range(base_count_of_members):
		check = False
		for j in range(actualy_count_of_members):
			if base_users['items'][i] == actualy_users['items'][j]:
				check = True
		if check == False:
			black_list.append(base_users['items'][i])

	base_users = show_users(test_group_id)
	base_count_of_members = base_users['count']

	banned_users = show_banned(test_group_id)
	for i in range (len(black_list)):
		for j in range (len(banned_users)):
			if black_list[i] == banned_users[j]['id']:
				black_list.remove(black_list[i])

	for i in range(len(black_list)):
		send_message(black_list[i])

	time.sleep(minute)