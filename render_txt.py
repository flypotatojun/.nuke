#this plugin made by mightyang 
#-*-coding:cp936-*-
import time
def render_txt():
    root = nuke.toNode('root')
    root_Name = root.name()
    cmd_path = 'subst n:' + ' \"' + os.path.dirname(nuke.env['ExecutablePath']) + '\"' + '\n'
    create_txt_Cmd = cmd_path+ 'n:\\' + os.path.basename(nuke.env['ExecutablePath']) + ' -x' + ' ' + '\"' + root_Name + '\"' + '\n'
    edit_txt_Cmd = 'n:\\' + os.path.basename(nuke.env['ExecutablePath']) + ' -x' + ' ' + '\"' + root_Name + '\"' + '\n'
    _current_time = time.strftime('%Y_%m_%d')
    file_path_name = get_desktopPath() + '\\' + _current_time + '.bat'
    if judgement_txt_exist(file_path_name):
        edit_textFile(file_path_name,edit_txt_Cmd)
    else:
        create_textFile(file_path_name,create_txt_Cmd)

def create_textFile(file_name,content):
    file = open(file_name,'w')
    file.write(content)
    file.close()

def get_desktopPath():
    HOME_Path = os.environ['HOME']
    env_desktop = HOME_Path + '\\' + 'desktop'
    if os.path.exists(env_desktop) == False:
        unicode_env_desktop = HOME_Path + '\\' + '桌面'
        env_desktop = unicode(unicode_env_desktop,'gbk')
    return env_desktop


def judgement_txt_exist(fileName):
    if os.path.exists(fileName):
        return 1
    else:
        return 0

def edit_textFile(file_name,content):
    file = open(file_name,'a')
    file.write(content)
    file.close()
