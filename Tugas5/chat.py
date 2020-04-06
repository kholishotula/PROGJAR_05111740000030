import sys
import os
import json
import uuid
import logging
from queue import Queue


class Chat:
    def __init__(self):
        self.sessions = {}
        self.users = {}
        self.users['izza'] = {'name': 'Rahmadani Izzatul', 'country': 'Indonesia', 'password': 'surabaya', 'incoming': {},
                               'outgoing': {}}
        self.users['maya'] = {'name': 'Kholishotul Amaliah', 'country': 'Indonesia', 'password': 'surabaya',
                                   'incoming': {}, 'outgoing': {}}
        self.users['nania'] = {'name': 'Azizatul Hikmaniyah', 'country': 'Indonesia', 'password': 'surabaya', 'incoming': {},
                                 'outgoing': {}}

    def proses(self, data):
        j = data.split(" ")
        try:
            command = j[0].strip()
            if (command == 'auth'):
                username = j[1].strip()
                password = j[2].strip()
                logging.warning("AUTH: auth {} {}".format(username, password))
                return self.autentikasi_user(username, password)
            elif (command == 'send'):
                sessionid = j[1].strip()
                usernameto = j[2].strip()
                message = ""
                for w in j[3:]:
                    message = "{} {}".format(message, w)
                usernamefrom = self.sessions[sessionid]['username']
                logging.warning(
                    "SEND: session {} send message from {} to {}".format(sessionid, usernamefrom, usernameto))
                return self.send_message(sessionid, usernamefrom, usernameto, message)
            elif (command == 'inbox'):
                sessionid = j[1].strip()
                username = self.sessions[sessionid]['username']
                logging.warning("INBOX: {}".format(sessionid))
                return self.get_inbox(username)
            elif (command == 'list'):
                hasil = self.get_list()
                logging.warning("LISTING ALL ACTIVE USERS")
                return {'status': 'OK', 'messages': hasil}
            elif (command == 'logout'):
                sessionid = j[1].strip()
                username = self.sessions[sessionid]['username']
                logging.warning("LOGOUT: {}".format(username))
                return self.logout(sessionid)
            else:
                return {'status': 'ERROR', 'message': '**Wrong protocol'}
        except KeyError:
            return {'status': 'ERROR', 'message': 'Cannot find the information'}
        except IndexError:
            return {'status': 'ERROR', 'message': '--Wrong protocol'}

    def autentikasi_user(self, username, password):
        if (username not in self.users):
            return {'status': 'ERROR', 'message': 'User is not found'}
        if (self.users[username]['password'] != password):
            return {'status': 'ERROR', 'message': 'Wrong password'}
        tokenid = str(uuid.uuid4())
        self.sessions[tokenid] = {'username': username, 'userdetail': self.users[username]}
        return {'status': 'OK', 'tokenid': tokenid}

    def get_user(self, username):
        if (username not in self.users):
            return False
        return self.users[username]

    def send_message(self, sessionid, username_from, username_dest, message):
        if (sessionid not in self.sessions):
            return {'status': 'ERROR', 'message': 'Session is not found'}
        s_fr = self.get_user(username_from)
        s_to = self.get_user(username_dest)

        if (s_fr == False or s_to == False):
            return {'status': 'ERROR', 'message': 'User is not found'}

        message = {'msg_from': s_fr['name'], 'msg_to': s_to['name'], 'msg': message}
        outqueue_sender = s_fr['outgoing']
        inqueue_receiver = s_to['incoming']
        try:
            outqueue_sender[username_from].put(message)
        except KeyError:
            outqueue_sender[username_from] = Queue()
            outqueue_sender[username_from].put(message)
        try:
            inqueue_receiver[username_from].put(message)
        except KeyError:
            inqueue_receiver[username_from] = Queue()
            inqueue_receiver[username_from].put(message)
        return {'status': 'OK', 'message': 'Message Sent'}

    def get_inbox(self, username):
        s_fr = self.get_user(username)
        incoming = s_fr['incoming']
        msgs = {}
        for users in incoming:
            msgs[users] = []
            while not incoming[users].empty():
                msgs[users].append(s_fr['incoming'][users].get_nowait())

        return {'status': 'OK', 'messages': msgs}

    def get_list(self):
        k = [self.sessions[i]['username'] for i in self.sessions.keys()]
        return k

    def logout(self, sessID):
        if (sessID in self.sessions):
            self.sessions.pop(sessID)
            return {'status': 'OK', 'messages': 'Logged out'}



if __name__ == "__main__":
    j = Chat()
    '''
    sesi = j.proses("auth messi surabaya")
    print(sesi)
    # sesi = j.autentikasi_user('messi','surabaya')
    # print sesi
    tokenid = sesi['tokenid']
    print(j.proses("send {} henderson hello gimana kabarnya son ".format(tokenid)))
    print(j.proses("send {} messi hello gimana kabarnya mess ".format(tokenid)))

    # print j.send_message(tokenid,'messi','henderson','hello son')
    # print j.send_message(tokenid,'henderson','messi','hello si')
    # print j.send_message(tokenid,'lineker','messi','hello si dari lineker')

    print("isi mailbox dari messi")
    print(j.get_inbox('messi'))
    print("isi mailbox dari henderson")
    print(j.get_inbox('henderson'))
    '''