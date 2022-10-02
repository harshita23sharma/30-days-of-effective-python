"""
Sorting By Complex Criteria Using The Key Parameter

"""


class Tool:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return f"Tool({self.name!r}, {self.weight})"


def run():
    numbers = [93, 86, 11, 68, 70]
    sorted_num = sorted(numbers)
    print(f"sorted_num: {sorted_num}")  # sorted_num: [11, 68, 70, 86, 93]

    # Sorting on objects below doesn't work
    tools = [
        Tool("level", 3.5),
        Tool("hammer", 1.23),
        Tool("screwdriver", 0.5),
        Tool("chisel", 0.25),
    ]
    print(
        "Unsorted:", repr(tools)
    )  # Unsorted: [Tool('level', 3.5), Tool('hammer', 1.23), Tool('screwdriver', 0.5), Tool('chisel', 0.25)]
    sorted_tools_names = sorted(tools, key=lambda x: x.name)
    print(
        f"sorted_tools_names: {sorted_tools_names}"
    )  # sorted_tools_names: [Tool('chisel', 0.25), Tool('hammer', 1.23), Tool('level', 3.5), Tool('screwdriver', 0.5)]

    # Note sorting on string, lowercase it first, bcoz
    # capital letters come before lowercase letters

    """
    SORTING ON MULTIPLE CRITERIA: USING TUPLE
    Tuple implements all the __lt__ etc special method comparator,
    required by the sort method
    """

    saw = (5, "circular saw")
    jackhammer = (40, "jackhammer")
    assert not (jackhammer < saw)

    # Above, tuples get compared at first position first,
    # if equal then move to the second position.
    tools.sort(key=lambda x: (x.weight, x.name))
    print(
        f"Sorted: {tools}"
    )  # Sorted: [Tool('chisel', 0.25), Tool('screwdriver', 0.5), Tool('hammer', 1.23), Tool('level', 3.5)]
    # Note: Above you cant execute sorting criteria in any direction
    # You can reverse direction for int types by having unary negation '-'
    # But it is not possible for all types
    # tools.sort(key=lambda x: (x.weight, -x.name), reverse=True)  # Gives Type error
    # print(f"Sorted: {tools}") # Gives Type error

    # Have multiple calls such that sorts are executed in opposite sequence of what
    # we want the final list to contain


if __name__ == "__main__":
    run()
