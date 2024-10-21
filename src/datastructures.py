from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    def add_member(self, member):
        if "first_name" not in member or "age" not in member or "lucky_numbers" not in member:
            return False

        member['id'] = self._generate_id()
        member['last_name'] = self.last_name 
        self._members.append(member)

    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
        return None

    def get_member(self, id):
        for member in self._members:
            if member['id'] == int(id):
                return member
        return None

    def get_all_members(self):
        return self._members