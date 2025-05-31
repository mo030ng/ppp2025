import sys
sys.path.append("c:/code/ppp2025")

from sfarm_hw import submit_to_api


def main():
    name = "김민주"
    affiliation = "스마트팜학과"
    student_id = "202410064"

    answer1 = 1359.7
    answer2 = 36.5
    answer3 = 45.1
    answer4 = 49
    submit_to_api(name, affiliation, student_id, answer1, answer2, answer3, answer4, verbose=True)


if __name__ == "__main__":
    main()