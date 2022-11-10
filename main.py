class StaticCodeAnalyzer:
    def __init__(self):
        pass

    # length
    @staticmethod
    def check_s001(line, i):
        if len(line) > 79:
            print(f'Line {i}: S001 Too long')

    # indentation
    @staticmethod
    def check_s002(line, i):
        j = 0
        while line[j] == " ":
            j += 1
        if j % 4 != 0:
            print(f'Line {i}: S002 Indentation is not a multiple of four')

    @staticmethod
    def find_comm(line):
        if "#" in line:
            new = line.split("#")
            new_line = new[0]
        else:
            new_line = line
        return new_line

    # semicolon
    def check_s003(self, line, i):
        new_line = self.find_comm(line).rstrip()
        if str(new_line).endswith(";"):
            print(f'Line {i}: S003 Unnecessary semicolon')

    # spaces before inline comments
    def check_s004(self, line, i):
        if "#" in line and line.index("#") != 0:
            new_line = self.find_comm(line)
            if len(new_line) < 2 or new_line[-1] + new_line[-2] != "  ":
                print(f'Line {i}: S004 At least two spaces required before inline comments')

    # checkingTODO
    @staticmethod
    def check_s005(line, i):
        if '#' in line:
            comment_index = line.index('#')
            if "todo" in line[comment_index:].lower():
                print(f'Line {i}: S005 TODO found')

    def check_errors(self):
        with open(input(), 'r') as file:
            counter = 0
            for i, line in enumerate(file, start=1):
                self.check_s001(line, i)
                self.check_s002(line, i)
                self.check_s003(line, i)
                self.check_s004(line, i)
                self.check_s005(line, i)
                # blank lines
                if counter > 2:
                    print(f'Line {i}: S006 More than two blank lines used before this line')
                if line.isspace() or line == "":
                    counter += 1
                else:
                    counter = 0


def main():
    analyzer = StaticCodeAnalyzer()
    analyzer.check_errors()


if __name__ == '__main__':
    main()
