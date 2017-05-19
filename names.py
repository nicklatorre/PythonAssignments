users = {
 'Students': [
     {'first_name':  'Tim', 'last_name' : 'Roth'},
     {'first_name' : 'Michael', 'last_name' : 'Madsen'},
     {'first_name' : 'Harvey', 'last_name' : 'Keitel'},
     {'first_name' : 'Steve', 'last_name' : 'Buscemi'}
  ],
 'Instructors': [
     {'first_name' : 'Louis', 'last_name' : 'Ogden'},
     {'first_name' : 'Brian', 'last_name' : 'Nelson'}
  ]
 }

for key in users:
    print key
    index = 1
    for data in users[key]:
        name_len = len(data["first_name"]) + len(data["last_name"])
        print index, "-", data["first_name"], data["last_name"], "-", name_len
        index += 1
