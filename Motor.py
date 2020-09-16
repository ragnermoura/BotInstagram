import Conta, DBUsers
import constants
import datetime


def init(webdriver):
    constants.init()
    Conta.login(webdriver)


def update(webdriver):
    #Get start of time to calculate elapsed time later
    start = datetime.datetime.now()
    #Before the loop, check if should unfollow anyone
    _check_follow_list(webdriver)
    while True:
        #Start following operation
        Conta.follow_people(webdriver)
        #Get the time at the end
        end = datetime.datetime.now()
        #How much time has passed?
        elapsed = end - start
        #If greater than our constant to check on followers, check on followers
        if elapsed.total_seconds() >= constants.CHECK_FOLLOWERS_EVERY:
            #reset the start variable to now
            start = datetime.datetime.now()
            #check on followers
            _check_follow_list(webdriver)


def _check_follow_list(webdriver):
    print("Procurando usuários para parar de seguir")
    #get the unfollow list
    users = DBUsers.check_unfollow_list()
    #if there's anyone in the list, start unfollowing operation
    if len(users) > 0:
        Conta.unfollow_people(webdriver, users)


