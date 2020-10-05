import argparse
from learner import learnConstraints

if __name__=="__main__":
    CLI=argparse.ArgumentParser()
    CLI.add_argument("--filename", type=str, default="nurse.xlsx")
    CLI.add_argument("--sheet", type=str, default="nurse")
    CLI.add_argument("--data_ranges", nargs="*", type=str, default=["B3:V14"])

    args=CLI.parse_args()

    constraints,tmp=learnConstraints(args.filename, args.sheet, args.data_ranges)

    for constraint in constraints:
        # print(constraint)
        for key, val in constraint.items():
            print("M,S= ",key)
            print("constraints:", val)
            print("\n")

