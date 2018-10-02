import random
class generator:
    def generate_list(self, difficulty_level=None):
        if(difficulty_level is None or difficulty_level >= 4):
            difficulty_level = 1
        difficulty_level += 4
        generated_list = []
        while(difficulty_level > 0):
            generated_string = ""
            for x in range(3):
                generated_string += str(random.randint(1,3))
            generated_list.append(generated_string)
            difficulty_level -= 1
        return generated_list

    def choose_password(self, potential_passwords):
        return potential_passwords[0]
        