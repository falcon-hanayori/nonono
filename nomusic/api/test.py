'''生成静态音乐列表，不去开api（懒狗行为）'''
import os
import json

if __name__ == "__main__":
    resource_path = os.path.join(os.path.relpath(os.path.dirname(os.path.dirname(__file__))), 'audio')
    g = os.walk(resource_path)
    music_src = list()
    music_name = list()
    for path,dir_list,file_list in g:
        path = '/'.join(path.split('/')[1:])
        path_name = '_'.join(path.split('/')[1:])
        for file_name in file_list:
            music_name.append('_'.join([path_name, file_name]))
            music_src.append(os.path.join(path, file_name))
    data = list()
    for i, name in enumerate(music_name):
        data.append(dict(src=music_src[i], img="icon/album.svg", sc_name=name, jp_name=name, num=i))
    with open(os.path.join(os.path.dirname(resource_path), 'music_list.json'), 'w') as f:
        json.dump(data, f)