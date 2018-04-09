#encoding:utf-8

import json

a={'name':'shitou','age':37,'tel':123456789}
print(a['name'])

#修改字典的数值
a['name']='shitou1'
print(a['name'])

#删除key
del(a['name'])
print(a)

#添加字典
a[123]= 321
print(a)

for ss in a:
    print(a[ss])

#做一个遍历统计
languages = ['python','java','python','c','c++','go','c#','c++','lisp','c','java','python','go','java','python','mathlab']
my_dict = {}
for a in languages:
    if a in my_dict:
        my_dict[a]+=1
    else:
        my_dict[a] = 1
print(my_dict)

print(my_dict.fromkeys('c',123))
print(my_dict.get('javaa',456))

def main():
    print('haha')

print(__name__)
if __name__ == '__main__':
    main()


my_json=json.dumps(languages)
print(my_json)










