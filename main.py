from lexer import Lexer
def main():

    # hello world
    print("Hello World ^^")

    # test
    test = Lexer()
    test.set_source_code("")
    test.deterministic_finite_automata("main();{if(index==10);{index+=1;}return0;}")

    # Things we need:
    # - main user navigation
    # - Valid Token List
    # -  DFA logic
    # - input file handling
    # - output file handling
    # - Testing
    # - Docs

if __name__ == "__main__":
    main()
