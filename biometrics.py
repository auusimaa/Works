# TIE-02101 Ohjelmointi 1
# Arttu Uusimaa, arttu.uusimaa@tuni.fi, student number: 292395
# A program that compares peoples biometric data
# Solution to excersise 9.7


def read_biometric_registry(filename):
    """
    Reads data drom file and saves it in lists and dicts
    :param filename: file, sourcefile
    :return: Dict, contains all peoples biometric data
    """
    result = {}

    handled_passports = []

    try:
        with open(filename, "r") as file_object:
            for row in file_object:
                fields = row.rstrip().split(";")

                if len(fields) != 8:
                    print("Error: there is a wrong number of fields "
                          "in the file:")
                    print("'", row, "'", sep="")
                    return None

                name = fields[0] + ", " + fields[1]
                passport = fields[2]

                if passport in handled_passports:
                    print("Error: passport number", passport,
                          "found multiple times.")
                    return None
                else:
                    handled_passports.append(passport)

                info = []
                biometrics = []

                info.append(name)

                for i in range(3, 8):
                    try:
                        id_value = float('%.2f' % float(fields[i]))
                    except ValueError:
                        print("Error: there's a non-numeric value on the row:")
                        print("'", row, "'", sep="")
                        return None

                    if 0 <= id_value <= 3.0:
                        biometrics.append(id_value)
                    else:
                        print("Error: there is an erroneous value in the file:")
                        print("'", row, "'", sep="")
                        return None

                info.append(biometrics)

                result[passport] = info

        return result

    except FileNotFoundError:
        print("Error: file", filename, "could not be opened.")
        return None


def execute_match(registry):
    """
    Checks if there are people with similar biometric data.
    :param registry: dict, contains all peoples biometric data
    :return: None
    """

    same_person = {}
    gone_through = []

    for pp_num1 in registry:
        people = []
        info1 = registry[pp_num1]
        meas_points1 = info1[1]

        for pp_num2 in registry:
            if pp_num2 not in gone_through:
                info2 = registry[pp_num2]
                meas_points2 = info2[1]
                distance = (sum([(a - b) ** 2 for a, b in
                                 zip(meas_points1, meas_points2)])) ** 0.5

                if distance < 0.1:
                    gone_through.append(pp_num2)
                    if pp_num1 != pp_num2:
                        people.append(pp_num2)

        if people:
            same_person[pp_num1] = people

    if same_person:
        for passport in same_person:
            print("Probably the same person:")
            info = registry[passport]
            x = [('%.2f' % i) for i in info[1]]
            x = ";".join(x)
            print(info[0], ";", passport, ";", x, sep="")
            for pass2 in same_person[passport]:
                info = registry[pass2]
                x = [('%.2f' % i) for i in info[1]]
                x = ";".join(x)
                print(info[0], ";", pass2, ";", x, sep="")
            print("")
    else:
        print("No matching persons were found.")


def execute_search(registry):
    """
    Searches possible matches to input data
    :param registry: dict, contains all peoples data
    :return: None
    """

    measurement_points = input("enter 5 measurement points"
                               " separated by semicolon: ")
    suspects = []

    try:
        float_meas_points = [float(x) for x in measurement_points.split(";")]
    except ValueError:
        print("Error: enter floats only. Try again.")
        execute_search(registry)
        return

    if len(float_meas_points) != 5:
        print("Error: wrong number of measurements. Try again.")
        execute_search(registry)

    else:
        for passport in registry:
            info = registry[passport]
            points = info[1]

            distance = (sum([(a - b) ** 2 for a, b in
                             zip(points, float_meas_points)])) ** 0.5

            if distance < 0.1:
                suspects.append(passport)

        if not suspects:
            print("No suspects were found.")
            print("")

        else:
            print("Suspects found:")

            for passport in suspects:
                info = registry[passport]
                x = [('%.2f' % i) for i in info[1]]
                x = ";".join(x)
                print(info[0], ";", passport, ";", x, sep="")

            print("")


def command_line_user_interface(registry):
    """
    Command line
    :param registry: dict, contains all peoples data
    :return: None
    """
    while True:
        command = input("command [search/match/<enter>] ")
        if command == "":
            return
        elif command == "match":
            execute_match(registry)
        elif command == "search":
            execute_search(registry)
        else:
            print("Error: unknown command '", command,
                  "': try again.", sep="")


def main():
    registry_file = input("Enter the name of the registry file: ")

    biometric_registry = read_biometric_registry(registry_file)
    if biometric_registry is not None:
        command_line_user_interface(biometric_registry)


main()
