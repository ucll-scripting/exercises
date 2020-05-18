# Explanations

Git is similar to DropBox/OneDrive/Google Drive in that it allows you to keep
backups of your code online. Git is specifically geared towards developers and
offers *a lot more* functionality than just backing up code.
None of the three alternatives mentioned above come close to what Git has to offer,
which is why you should never rely on DropBox/OneDrive/Google Drive to
manage your code. Take the time to learn Git instead.

Not every file needs to be stored in a Git repository. For example, when working on a Java project,
you only want Git to keep track of the `.java` files but not of the `.class` files.
This would be redundant as `.class` files can easily be generated given the `.java` files.
Including both `.java` and `.class` files in the repository can quickly lead to problems.

Say for example you modify the `.java` files and add these changes
to the Git repository. However, you do not compile them, meaning the
`.class` files are not up to date. Someone else on your team
might not realize this and use these old `.class` files instead
of recompiling. This situation can be prevented by never
including generated files in the Git repository and instead
expecting people to always regenerate these themselves.
This best practice rule is universal and not limited to Git.

Git allows you to tell it which files should be ignored. In our example,
`.java` files should definitely be tracked by Git, but `.class` files
must be ignored. This is done using a `.gitignore` file which allow
you to specify rules which determine which files to track and which ones
to ignore.

A `.gitignore` file could look as follows:

```text
*.class
```

This tells Git, as you may expect, to ignore all files with the `.class`
extension. Similarly, we could add

```text
*.class
*.jar
javadocs/*
```

All these files can be generated based on the `.java` files,
so none of them should be included in the Git repository.

Different languages need different `.gitignore` files.
IDEs also often produce files that should be ignored.
Setting up a `.gitignore` file can become quite a burden,
as you need to be aware of all possible files that could
possibly be generated.

Fortunately, some people have taken the time to create
a [website named gitignore.io](https://gitignore.io) that generates `.gitignore` files for you.
You only need to list which technologies you use
(e.g. programming language, IDE, framework) and
it will produce a `.gitignore` for you.
Take a few moments to visit it: ask it to generate a `.gitignore` file for Java.
At the moment of writing, the site produces the following file:

```text
# Created by https://www.gitignore.io/api/java
# Edit at https://www.gitignore.io/?templates=java

### Java ###
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*

# End of https://www.gitignore.io/api/java
```

## Task

Write a Python script that can be used as follows:

```bash
$ python fetch-gitignore.py java intellij
```

This should ask [gitignore.io](https://gitignore.io) to generate a `.gitignore`
for Java and IntelliJ. Have the result written to disk.
In other words, after the command above, a `.gitignore` file needs to be created
with as contents

```text
# Created by https://www.gitignore.io/api/java,intellij
# Edit at https://www.gitignore.io/?templates=java,intellij

### Intellij ###
# Covers JetBrains IDEs: IntelliJ, RubyMine, PhpStorm, AppCode, PyCharm, CLion, Android Studio and WebStorm
# Reference: https://intellij-support.jetbrains.com/hc/en-us/articles/206544839

# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# Gradle and Maven with auto-import
# When using Gradle or Maven with auto-import, you should exclude module files,
# since they will be recreated, and may cause churn.  Uncomment if using
# auto-import.
# .idea/modules.xml
# .idea/*.iml
# .idea/modules
# *.iml
# *.ipr

# CMake
cmake-build-*/

# Mongo Explorer plugin
.idea/**/mongoSettings.xml

# File-based project format
*.iws

# IntelliJ
out/

# mpeltonen/sbt-idea plugin
.idea_modules/

# JIRA plugin
atlassian-ide-plugin.xml

# Cursive Clojure plugin
.idea/replstate.xml

# Crashlytics plugin (for Android Studio and IntelliJ)
com_crashlytics_export_strings.xml
crashlytics.properties
crashlytics-build.properties
fabric.properties

# Editor-based Rest Client
.idea/httpRequests

# Android studio 3.1+ serialized cache file
.idea/caches/build_file_checksums.ser

### Intellij Patch ###
# Comment Reason: https://github.com/joeblau/gitignore.io/issues/186#issuecomment-215987721

# *.iml
# modules.xml
# .idea/misc.xml
# *.ipr

# Sonarlint plugin
.idea/**/sonarlint/

# SonarQube Plugin
.idea/**/sonarIssues.xml

# Markdown Navigator plugin
.idea/**/markdown-navigator.xml
.idea/**/markdown-navigator/

### Java ###
# Compiled class file
*.class

# Log file
*.log

# BlueJ files
*.ctxt

# Mobile Tools for Java (J2ME)
.mtj.tmp/

# Package Files #
*.jar
*.war
*.nar
*.ear
*.zip
*.tar.gz
*.rar

# virtual machine crash logs, see http://www.java.com/en/download/help/error_hotspot.xml
hs_err_pid*

# End of https://www.gitignore.io/api/java,intellij
```

## Hints

* Look around on [gitignore.io](https://gitignore.io) to find if there's an API.
* Find out [how to perform HTTP requests in Python](https://lmgtfy.com/?q=python+http+request).
