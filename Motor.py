import Conta, DBUsers
import constants
import datetime


def init(webdriver):
    constants.init()
    Conta.login(webdriver)


def update(webdriver):

    start = datetime.datetime.now()

    _check_follow_list(webdriver)
    while True:

        Conta.follow_people(webdriver)

        end = datetime.datetime.now()

        elapsed = end - start

        if elapsed.total_seconds() >= constants.CHECK_FOLLOWERS_EVERY:

            start = datetime.datetime.now()

            _check_follow_list(webdriver)


def _check_follow_list(webdriver):
    print("Procurando usuários para parar de seguir")

    users = DBUsers.check_unfollow_list()

    if len(users) > 0:
        Conta.unfollow_people(webdriver, users)


