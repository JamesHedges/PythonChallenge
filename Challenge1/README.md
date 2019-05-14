# WorldRemit Denver Python Challenge One - Some Basics
## Variables and Types
1. Primitives
   - booleans
   - integers
   - floats
   - strings
     - Creating - use quote or double quote (must match)
2. Variables
   - What is a variable in Python? *Everything!*
   - Creating and Assigning - simple
     - Naming
       - Lower and uppe rcase letters
       - Digits (0-9)
       - Underscore
       - Cannot start with a digit
       - Starting with underscore - can do this, but Python uses them as 'special' variable. So be careful. More on this in a later challenge
     - They are case sensitive!
     - Assignment - = is not equality
   - Assigning other variables - what works, how it works
   - What type am I? `type(<varName>)`
3. More Strings
   - Its a collection of charactes that can be indexed
     - Get the length: `len(myString)`
     - Indexing: `print(myString[2])` (note: indexes are zero-based)
   - Things you can do
     - Get lower case: `myString.lower()`
     - Get upper case: `myString.upper()`
     - Replace a character: `myString.replace("t", "T")`
     - Replace a substring: `myString.replace("tt", "dd")`
     - More to come later
   - Immutable... what's that?
## Printing
1. Basic print
   - Print a literal string: `print("Hello Python")`
   - Print a variable: `print(myVar)`
   - Mixing it up: `print("myVar is", myVar)`
 ## Integer Operator - Arithmetic
 1. Operators
    - Add (+)
    - Subract (-) 
    - Multiply (*)
    - Divide (/) - floating point
    - Divide (//) - integer truncating
    - Modulus (%)
    - Exponentiation (**)
2. Precedence
## Code Structure - Moving beyond the command prompt
1. Files
   - Create a folder for you application, name it HelloPython
   - Create your main application file with a .py extension, name it Hello.py
   - Add a simple statement to your file: `print("Hello Python")`
   - FYI - in Python lingo, you have just created a module.
   - Save the file!
   - From the terminal window, enter this command *python Hello.py*
2. Functions
   
   To better organize code, we will introduce simple functions (no paramaters). This will make the code more readable and easier to manipulate.

   - Define a function
  
      ```python
      def MyFuncName():
          first line of code
      ```

   - Call a function
      - The function must be defined prior to calling it. If defined in the same file, the function must appear first. If in another file, it will need to be imported (more on that later)
      - To call the function, just enter a line with the function name and parenthesis:
        ```python
        def MyFunc():
            print("Hello Python")
           
        MyFunc()
        ```
    - You can add multiple functions to a file
    - To help with making our code uniform, let's create a file with a main function and call it. Your HelloPython.py should look like this:
        ```python
        def Main():
            Hello()
        
        def Hello():
            print("Hello Python")

        Main()
        ```
    - You can place function in another file and import them
       - Create another file with .py extension and add a function to it
       - In the Hello.py file add an import and call the function
        ```python
        # TestFunc.py
        def Message():
            print("Hello from the other file")
        
        # Hello.py
        import TestFunc

        def Main():
            Hello()
            TestFunc.Message()
        
        def Hello():
            print("Hello Python")

        Main()
        ```
    - imports can be aliased and functions referenced by the alias
        ```python
        import TestFunc as tf

        def Main():
            tf.Message()
        ```
    - imports can be function specific using `from filename import function1, function2, ...`
        ```python
        from TestFunc import Message

        def Main():
            Message()
        ```
## For you to do
1. From the Python command line, try the following
   - Create variables and assing values different types (bool, int, float, and string)
   - Print each of the variable using the differnt print styles
      * `print(myVal)`
      * `print("My vale is", myVal)`
   - Try assiging different variables to each other. What is the type (type(myVar)) of the variable being assigned?
   - Play with the string 
      * Print the length of the string variable
      * Print the string's first, last, and middle characters
   - Try some string functions
      * Call the lower, upper, and replace methods on the string variable.
      * Print the string variable after each call. Did the string variable change?
   - Try some math operations
      * Play with the order of operations
      * Use parenthesis to control the order of operations
2. Files and Imports (Modules)
   - Create a folder. Open the folder in VS Code
   - Add a python file with the .py extension. This is your main file
      * Add a simple print statement
      * Save the file and run it
   - Add a function to your main file
      * Add a simple print statement to your function
      * Add a statement to call the function
      * Save and run it
   - Add another python file (module) to your folder
      * Add a function to the module with a simple print statement
      * Save the file
   - In your main file, add an import for your new module
      * In your main file's function, call the method from your module
      * Save and run it
3. Play, Play, Play
   - Use your new Python skills and play around
   - Try using the different variable types like you did on the command line
   - Try playing around with strings
   - Add more functions to your module, create additional modules with multiple functions
      * Use the differnt import techniques to access your modules' methods:
         * `import MyModule`
         * `import MyModule as mm`
         * `from MyModule import MyFunc`
   
      