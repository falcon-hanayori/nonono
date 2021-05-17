import os
from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['REFRESH_MSEC'] = 1000
# 动态加载静态资源
app.jinja_env.auto_reload = True

@app.route('/get_music_list')
def get_music_list():
    resource_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'audio')
    g = os.walk(resource_path)
    music_src = list()
    music_name = list()
    for path,dir_list,file_list in g:
        path = '/'.join(path.split('/')[1:])
        path_name = '_'.join(path.split('/')[1:])
        for file_name in file_list:
            music_src.append('_'.join([path, file_name]))
            music_name.append(os.path.join(path, file_name))
    return(dict(music_src=music_src, music_name=music_name))