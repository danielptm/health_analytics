# import matplotlib.pyplot as plt
from typing import List
import matplotlib.pyplot as plt
import numpy as np

class Analyze:
    def readfile(self):
        with open('resources/data.txt', 'r') as file:
            data = file.read()
        return data

    def get_lines(self, data: str):
        lines = data.splitlines()
        return lines

    # Gets
    def get_objects(self, data: List):
        objects = []
        itr = filter(lambda d: "..." not in d, data)
        refined_list = list(itr)

        i = 0
        while i < len(refined_list):
            new_object = {}
            new_object["outcomes"] = []
            new_object["age"] = refined_list[i].replace("$", "")
            new_object["outcomes"].append(refined_list[i+1].split("|"))
            new_object["outcomes"].append(refined_list[i+2].split("|"))
            new_object["outcomes"].append(refined_list[i+3].split("|"))
            new_object["outcomes"].append(refined_list[i+4].split("|"))
            new_object["outcomes"].append(refined_list[i+5].split("|"))
            new_object["outcomes"].append(refined_list[i+6].split("|"))
            new_object["outcomes"].append(refined_list[i+7].split("|"))
            new_object["outcomes"].append(refined_list[i+8].split("|"))
            new_object["outcomes"].append(refined_list[i+9].split("|"))
            new_object["outcomes"].append(refined_list[i+10].split("|"))
            new_object["outcomes"].append(refined_list[i+11].split("|"))
            new_object["outcomes"].append(refined_list[i+12].split("|"))
            new_object["outcomes"].append(refined_list[i+13].split("|"))
            new_object["outcomes"].append(refined_list[i+14].split("|"))
            new_object["outcomes"].append(refined_list[i+15].split("|"))
            objects.append(new_object)
            i += 16
        return objects


    def get_age_groups(self, objects):
        age_groups = objects[1:11]
        age_group_names = []
        for item in age_groups:
            age_group_names.append(item['age'])
        return age_group_names


    def get_distinct_outcomes(self, objects):
        age_groups = objects[1:11]
        outcomes = []
        for obj in age_groups:
            for inner in obj['outcomes']:
                if inner[0] not in outcomes:
                    outcomes.append(inner[0])
        return outcomes

    # Return a list of objects. Each object has the outcome and then the corresponding
    # proportions for each age range.
    def get_outcomes_with_age(self, objects):
        outcomes = self.get_distinct_outcomes(objects)
        refined = objects[1:11]
        outcomeObjects = {}
        for outcome in outcomes:
            outcomeObjects[outcome] = {"ages": []}
            for ref in refined:
                for obj in ref['outcomes']:
                    if obj[0] == outcome:
                        outcomeObjects[outcome]["ages"].append({"age": ref["age"], "rate": float(obj[2])})
        return outcomeObjects

    # https://matplotlib.org/stable/tutorials/introductory/pyplot.html
    # plot get_outcomes_with_age here
    def plot_subs(self, objects):
        outcomes_with_age = self.get_outcomes_with_age(objects)

        for key, value in outcomes_with_age.items():
            plt.figure(figsize=(9, 6))
            plt.suptitle(key)
            plt.ylabel('Y-axis')


            # plt.gca().invert_yaxis()
            names = []
            values = []
            # plt.ylim(25)
            # /Users/danieltuttle/Documents/school/GeorgiaTech/courses/intro_to_health_info/projects/module2/project2
            for ref in value["ages"]:
                names.append(ref["age"])
                values.append(ref["rate"])

            plt.bar(names, values)
            plt.savefig('/Users/danieltuttle/Documents/school/GeorgiaTech/courses/intro_to_health_info/projects/module2/project2/images/' + key + '.png')

        # plt.show()












