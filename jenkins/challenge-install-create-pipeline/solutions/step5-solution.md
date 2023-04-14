# Note

1. Launch Jenkins and create a new pipeline job by clicking `New Item` on the dashboard.
2. Enter a name for the job and select `Pipeline` as the type of job, then click `OK`.
3. Scroll down to the `Pipeline` section and choose `Pipeline script` as the definition.
4. In the `Script` text area, enter the following code:

```pipeline
pipeline {
agent any

    stages {
        stage('Hello') {
            steps {
                echo 'Hello World'
            }
        }
    }

}
```

5. Save the pipeline script by clicking `Apply` and `Save`.
6. Run the pipeline job by clicking `Build Now`. This will start the pipeline and execute the `Hello` stage, which will print `Hello World` to the console output.
