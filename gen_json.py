import json
sa_info = {
  "test",
  }

if __name__ == '__main__':
    sa_json = 'test_json.json'
    with open(sa_json,'w') as file:
      json.dump(sa_info,file)


