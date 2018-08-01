import vk
import time
from keys import *

version = '5.50'

permissions = ['messages', 'groups']

half_an_hour = 1800

def send_message(userID):
	vk_api.messages.send(user_id = userID, message ='check')

def show_users(groupID):
	users = vk_api.groups.getMembers(group_id = groupID, sort = 'id_asc')
	return users

def show_banned(groupID):
	banned_users = vk_api.groups.getBanned(group_id = groupID)
	return banned_users['items']

session = vk.AuthSession(app_id = bot_app_id, user_login = bot_login, user_password = bot_password, scope = permissions)

vk_api = vk.API(session, v = version, scope = permissions)

base_users = show_users(test_group_id)
base_count_of_members = base_users['count']

while True:

	black_list = []

	actualy_users = show_users(test_group_id)
	actualy_count_of_members = actualy_users['count']

	for i in range(base_count_of_members):
		check = False
		for j in range(actualy_count_of_members):
			#Каждый из base должен быть в actualy
			if base_users['items'][i] == actualy_users['items'][j]:
				check = True
		if check == False:
			black_list.append(base_users['items'][i])

	base_users = show_users(test_group_id)
	base_count_of_members = base_users['count']

	banned_users = show_banned(test_group_id)
	for i in range (len(black_list)):#проверка тех кто отсутствует в банлисте
		for j in range (len(banned_users)):
			if black_list[i] == banned_users[j]:
				black_list.remove[i]

	for i in range(len(black_list)):
		send_message(black_list[i])

	time.sleep(60)