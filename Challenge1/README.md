# PythonChallenge
WorldRemit Denver Python Challenge

## Challenge One - Some Basics
### Code Structure
1. Files
   - Create a folder for you application, name it HelloPython
   - Create your main application file with a .py extension, name it Hello.py
   - Add a simple statement to your file: `print("Hello Python")`
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
    - 