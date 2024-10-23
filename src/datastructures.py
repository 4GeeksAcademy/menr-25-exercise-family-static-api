from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # self._next_id = 1
        self._members = ([{
        'id': self._generateId(),
        'age': 33,
        'first_name': 'John',
        'lucky_numbers': [7, 13, 22]
    },
    {
        'id': self._generateId(),
        'age': 35,
        'first_name': 'Jane',
        'lucky_numbers': [ 10, 14, 3]
    },
    {
        'id': self._generateId(),
        'age': 5,
        'first_name': 'Jimmy',
        'lucky_numbers': [1]
    }
        
    ])

    # def _generate_id(self):
    #     generated_id = self._next_id
    #     self._next_id += 1
    #     return generated_id
    
    def _generateId(self):
        return randint(0, 99999999)

    # def add_member(self, member):
    #     # if "first_name" not in member or "age" not in member or "lucky_numbers" not in member:
    #     #     return False

    #     member['id'] = self._generateId()
    #     # member[last_name] = self.last_name 
    #     self._members.append(member)

    def add_member(self, member):
        if not member.get("id"):
            member[id] = self._generateId()
        self._members.append(member)

    # def delete_member(self, id):
    #     for position in range(len(self._members)):
    #         if self._members[position]['id'] == id:
    #             self._members.pop(position)
    #     return None

    # def delete_member(self, id):
    #     for position in range(len(self._members)-1):
    #         if self._members[position]['id'] == id:
    #             self._members.pop(position)
    #             return True
    #     return None
    
    def delete_member(self, id):
        for member in self._members:
            if member ["id"] == id:
                self._members.remove(member)
                return True
        return False

    # def get_member(self, id):
    #     for member in self._members:
    #         if member['id'] == int(id):
    #             return member
    #     return None

    def get_member(self, id):
        for member in self._members:
             if member ["id"] == id:
                 return member

    def get_all_members(self):
        return self._members