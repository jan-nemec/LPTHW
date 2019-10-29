# Automated Testing

# Having to type commands over and over to make sure it's working is annoying.
# It would be better to write little pieces of code that test your code.
# Then when you make a change, or add a new thing to your program, you just
# "run your tests" and tests make sure things are still working. These auto-
# mated tests won't catch all your bugs, but they will cut down on the time
# you spend repeatedly typing and running your code.
# Also this process of writing a test that runs some code you have written
# forces you to understand clearly what you have just written.

# Writing a Test Case
# 1. Copy skeleton to ex47.
# 2. Rename everything with NAME to ex47.
# 3. Change the word NAME in all the files to ex47.
# 4. Remove all the *.pyc files to make sure you're clean.

# 5. Create file ex47.py and put there code to test.
# 6. Change the unit test skeleton.

# Testing Guidelines
# 1. Test files go in tests/ and are named BLAH_tests.py, otherwise nosetests
# won't run them.
# 2. Write on test file for each module you make.
# 3. Keep your test cases short, but don't worry if they are a bit messy.
# 4. Even though test cases are messy, try to keep them clean and remove
# any repetitive code you can. Create helper functions that get rid of
# duplicate code.
# 5. Do not get too attached to your tests. Sometimes, the best way to redesing
# something is to just delete it and start over.