debug = True

def debug_print(variable_name, variable):
    if debug:
        print (f"***{variable_name} is [{variable}].")

def main():
    nothing = "nope"
    debug_print("nothing", nothing)

if "__main__" == __name__: 
    main()
