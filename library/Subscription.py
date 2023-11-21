import json
from cli.CLI import CLI

class Subscription:
    def add_subscribers(self, user):
        super(Subscription, self).__getattribute__('subscribers').append(user)

    def remove_subscribers(self, user):
        super(Subscription, self).__getattribute__('subscribers').remove(user)

    def notify_subscribers(self, message):
        if CLI.instance.user is not None and CLI.instance.user in self.subscribers:
            print(message)

        with open('data/users.json', 'r') as json_file:
            users = json.load(json_file)

        for subscriber in self.subscribers:
            for user in users:
                if user['username'] == subscriber.username:
                    user['message'] = message

        with open('data/users.json', 'w') as json_file:
            json.dump(users, json_file)