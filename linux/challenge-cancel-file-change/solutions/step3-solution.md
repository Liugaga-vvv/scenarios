### Undo and Reset

1. Use the git log command to view the commit history:

   ```bash
   git log
   ```

2. Use the git reset command to undo the most recent commit and reset the current branch to the previous commit:

   ```bash
   git reset HEAD~1
   ```

3. Use the git log command again to confirm that the most recent commit has been undone:

   ```bash
   git log
   ```
