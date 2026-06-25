import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="ukenergy",
        description="Fetch energy data from terminal"
    )
    parser.add_argument(
        "command",
        choices=["carbon"],
        help="Data Sources to Fetch From"
    )

    args = parser.parse_args()

    if args.command == "carbon":
        print("Carbon command coming soon")

if __name__ == "__main__":
    main()