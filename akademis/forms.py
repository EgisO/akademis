
class Users:

    def register_user(self, username, password):
        file = open('user_db.dat', 'a+')
        file.write("{0}:{1}\n".format(username, password))
        file.close()

    def login_user(self, username, password):
        file = open('user_db.dat', 'r')
        line = file.readline()
        while line:
            if line == "{0}:{1}\n".format(username, password):
                file.close()
                return True
            line = file.readline()
        file.close()
        return False

class Profile:

    def update_name(self, name):
        file = open('profile_db.dat', 'r')
        line = file.readline().split(':')
        file.close()
        print(line)
        file = open('profile_db.dat', 'w+')
        file.write("{0}:{1}".format(name,line[1]))
        file.close()

    def update_tags(self, tags):
        file = open('profile_db.dat', 'r')
        line = file.readline().split(':')
        line[1] = line[1]+';'+str(tags)
        file.close()
        print(line)
        file = open('profile_db.dat', 'w+')
        file.write("{0}:{1}".format(line[0],line[1]))
        file.close()

    def get_profile(self):
        file = open('profile_db.dat', 'r')
        line = file.readline().split(':')
        _tags = line[1].split(';')
        file.close()
        return line[0], _tags
        