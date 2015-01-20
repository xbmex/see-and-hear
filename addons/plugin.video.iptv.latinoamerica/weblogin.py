import os
import re
import urllib,urllib2
import cookielib

myusername = ''
mypassword = ''


def check_login(source,username):
    logged_in_string = 'googlecode'
    if re.search(logged_in_string,source,re.IGNORECASE):
        return True
    else:
        return False


def doLogin(cookiepath, username, password):

    if not os.path.isfile(cookiepath):
        cookiepath = os.path.join(cookiepath,'cookies.lwp')

    try:
        os.remove(cookiepath)
    except:
        pass

    if username and password:

        login_url = 'http://www.ece.ualberta.ca/~reyesgal/secure.php'

        header_string = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'

        login_data = urllib.urlencode({'access_login':username, 'access_password':password, 'Submit':'Submit'})

        req = urllib2.Request(login_url, login_data)
        req.add_header('User-Agent',header_string)

        cj = cookielib.LWPCookieJar()

        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

        response = opener.open(req)
        source = response.read()
        response.close()

        login = check_login(source,username)

        if login == True:
            cj.save(cookiepath)
            tvpath = source
        elif login == False:
            tvpath = False

        return tvpath
    
    else:
        return False

if __name__ == "__main__":
    if myusername is '' or mypassword is '':
        print 'YOU HAVE NOT SET THE USERNAME OR PASSWORD!'
    else:
        logged_in = doLogin(os.getcwd(),myusername,mypassword)
        print 'LOGGED IN:',logged_in