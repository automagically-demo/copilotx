# Copilot X

A collection of files and links curated to help demonstrate features available in Copilot X.


# Home page for Copilot X

Interested in signing up for our Copilot X experiments, the following page allows you to sign up for lots of different experiements.

Visit [https://gh.io/copilotx](https://gh.io/copilotx)

# Copilot Chat

Filename | My usage
--- | ---
utils.py | - Select regex expressions and ask GitHub Copilot to explain them.<br />- Make this code more readable.<br />- Separate validation functions and add comments.
parse_expenses.py | Select function and ask to find a bug in code.
test.asm | Ask Copilot Chat to translate this Assembly language into Python
genericListener.cob | Ask Copilot Chat to translate this COBOL into Java
vulnerable.php | Ask Copilot Chat if this code is secure. It tell me that it's not. I then ask Copilot Chat to fix the code.
transaction.js | Ask GitHub Copilot Chat to rewrite the calculateTax function to look up the tax rate. "calculateTax needs to take the zip code and look up the tax rate". Note that it will likely invent an API.
login-service.ts | Ask Copilot Chat to add a function to check if a password has been breached. It will usually suggest code to call the haveibeenpwnd API. Note this also uses security-database-service.ts so the code is a little cleaner.
obfuscated.c, obfuscated.java | Ask Copilot chat to explain the code. The first is obfuscated C code that does strange things with pointers, but Copilot seems to be able to interpret it. The second is Java with unreadable class and variable names, however Copilot identifies that it's just calculating the area of a circle. A great second step is asking to make it readable.
mystery.py | An extreme example of what Copilot Chat can do (likely because it's a famous example). Ask it to explain the code. Ideally run the code (you'll need python 2.7 - run `py -2.7 mystery.py`) then open the resulting M.bmp file which should get built on screen as you watch.
infra/azuredeploy.json | App modernization demo - ask chat if it's the latest node version, find the line and use inline chat to upgrade it. Ask if this can be converted to bicep, then ask it to do that.
romanConverter.test.js | Copilot Chat generates unit tests covering edge cases for a function that converts Roman numerals to integers. I did not provide the number to letter mapping, it got it right by itself.
move-commit-new-branch.sh | Ask `gh copilot suggest "I want to move the last commit on a new branch"`. Copilot CLI generates and explains me the commands to move the last commit to a new branch.
<br /><br />
# What's Next? See Githubnext

Open Githubnext using [https://githubnext.com/](https://githubnext.com/)