import json

def write_json(info, filename='datos.json'):
    with open('datos.json', 'r+') as f:
        list = json.load(f)
        list['lugar'].append(info)
        f.seek(0)
        json.dump(list, f, indent=4)
        print('archivos anexados correctamente')
