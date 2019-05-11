# PythonChallenge
WorldRemit Denver Python Challenge

## Challenge Zero - Setting Up Your Environment

Set-up Python Environment *** REQUIRES ADMIN PRIVILEGES
1. Install Python
* Download version 3.7.3 from [Python Download](https://www.python.org/downloads/) - save to file, do not run it
* Go to the download folder and run the Python install as administrator
* Select option add Python to the path
2. Install VS Code -- optional, but you will need a development environment
* Download VS Code from [Visual Studio Download](https://code.visualstudio.com/Download)
- select the version that matches your computer
- Save to a file
* Go to the download folder  and run the VS Code install as an administrator
* Once installed and running, go to the Extensions (bottom icon on the left) and search for "python"
* Select the Microsoft Python extention and click the install button
3. Verify your Python environment is working
* In VS Code, a terminal window should be open in the bottom pane.
- If not, click on the Terminal menu and select the New Terminal option
* In the terminal window at the prompt, type: python
* You should have a >>> prompt, enter: print("Hello Python")
* Press enter and you should see "Hello Python"
* At the >>> prompt, enter: import this
* You should some text printed that starts with "Simple is better than complex."
* If you see the expected text displayed, congratulations! Your Python environment is now working
* If you don't see the expected text, contact your team's mentor for assistance

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
  
## 