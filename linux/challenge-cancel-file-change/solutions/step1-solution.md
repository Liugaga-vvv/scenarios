### Undo the Changes You Made

1. Make some changes to the myfile.txt file. You can add a new line of text to the file using the following command:

   ```bash
   echo "This is a new line of text." >> myfile.txt
   ```

2. Use the git status command to see the changes you've made.

   ```bash
   git status
   ```

3. Undo the changes you made to the myfile.txt file using the restore command:

   ```bash
   git restore myfile.txt
   ```
