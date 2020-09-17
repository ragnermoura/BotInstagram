from time import sleep
import datetime
import DBUsers, constants
import traceback
import random


def login(webdriver):
    # Abrir o Instagram
    webdriver.get( 'https://www.instagram.com/accounts/login/?source=auth_switcher' )
    # Esperar e segundos até o Serviço responder
    sleep( 3 )
    # Buscar o nome do usuário e senha
    username = webdriver.find_element_by_name( 'username' )
    username.send_keys( constants.INST_USER )
    password = webdriver.find_element_by_name( 'password' )
    password.send_keys( constants.INST_PASS )
    # Get no Botão do Instagram
    try:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button' )
    except:
        button_login = webdriver.find_element_by_xpath(
            '//*[@id="loginForm"]/div/div[3]/button/div' )
    # Aqui espera um pouquinhho
    sleep( 2 )
    #Pronto, aqui ele clica no BTN do Login
    button_login.click()
    sleep( 3 )
    #Sempre aparece aqueles modais no inicio do Instagram. Se aparecer, ele vai clicar em "AGORA NÃO"
    #Se não aparcecer nada, aqui ele ignora e retorna

    try:
        notnow = webdriver.find_element_by_css_selector(
            '//*[@id="react-root"]/section/main/div/div/div/div/button' )
        notnow.click()

    except:
        return


def unfollow_people(webdriver, people):

    if not isinstance( people, (list,) ):
        p = people
        people = []
        people.append( p )

    for user in people:
        try:
            webdriver.get( 'https://www.instagram.com/' + user + '/' )
            sleep( 5 )
            unfollow_xpath = '//*[@id="react-root"]/section/main/header/div[2]/div/button'

            unfollow_confirm_xpath = '/html/body/div[3]/div/div/div[3]/button[1]'

            if webdriver.find_element_by_xpath( unfollow_xpath ).text == "Following":
                sleep( random.randint( 4, 15 ) )
                webdriver.find_element_by_xpath( unfollow_xpath ).click()
                sleep( 2 )
                webdriver.find_element_by_xpath( unfollow_confirm_xpath ).click()
                sleep( 4 )
            DBUsers.delete_user( user )

        except Exception:
            traceback.print_exc()
            continue


def follow_people(webdriver):

    prev_user_list = DBUsers.get_followed_users()

    new_followed = []

    followed = 0
    likes = 0

    for hashtag in constants.HASHTAGS:

        webdriver.get( 'https://www.instagram.com/explore/tags/' + hashtag + '/' )
        sleep( 5 )


        first_thumbnail = webdriver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div' )

        first_thumbnail.click()
        sleep( random.randint( 1, 3 ) )

        try:

            for x in range( 1, 200 ):
                t_start = datetime.datetime.now()

                username = webdriver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[1]/span/a' ).text
                likes_over_limit = False
                try:

                    likes = int( webdriver.find_element_by_xpath(
                        '/html/body/div[4]/div[2]/div/article/div[3]/section[2]/div/div[2]/button/span' ).text )
                    if likes > constants.LIKES_LIMIT:
                        print( "likes over {0}".format( constants.LIKES_LIMIT ) )
                        likes_over_limit = True

                    print( "Detected: {0}".format( username ) )

                    if username not in prev_user_list and not likes_over_limit:

                        if webdriver.find_element_by_xpath(
                                '/html/body/div[4]/div[2]/div/article/header/div[2]/div[1]/div[2]/button' ).text == 'Follow':
                            # Use DBUsers to add the new user to the database
                            DBUsers.add_user( username )
                            # Click follow
                            webdriver.find_element_by_xpath(
                                '/html/body/div[3]/div[2]/div/article/header/div[2]/div[1]/div[2]/button' ).click()
                            followed += 1
                            print( "Followed: {0}, #{1}".format( username, followed ) )
                            new_followed.append( username )

                        #Curtindo a foto
                        button_like = webdriver.find_element_by_xpath(
                            '/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button' )

                        button_like.click()
                        likes += 1
                        print( "Liked {0}'s post, #{1}".format( username, likes ) )
                        sleep( random.randint( 5, 18 ) )


                    webdriver.find_element_by_link_text( 'Next' ).click()
                    sleep( random.randint( 20, 30 ) )

                except:
                    traceback.print_exc()
                    continue
                t_end = datetime.datetime.now()


                t_elapsed = t_end - t_start
                print( "This post took {0} seconds".format( t_elapsed.total_seconds() ) )


        except:
            traceback.print_exc()
            continue


        for n in range( 0, len( new_followed ) ):
            prev_user_list.append( new_followed[n] )
        print( 'Liked {} photos.'.format( likes ) )
        print( 'Followed {} new people.'.format( followed ) )
