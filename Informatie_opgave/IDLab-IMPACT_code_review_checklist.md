# Master Thesis Code Review Checklist

**IDLab-IMPACT**

## 1. General Information

At the start of the second semester, a code review is organized to provide feedback on the code written so far.

Before requesting a review, ensure that:

- Your code is available on GitHub (UGent or github.com).
- Your supervisors have been added as collaborators.
- You have notified your supervisors via your Master Thesis Microsoft Teams channel once the code is ready for review.

## 2. Code Review Checklist

Your supervisors will review your code using the following checklist.

### 2.1 Code Readability & Structure

- [ ] The comments, function names, classes and variable names are in English.
- [ ] The code is understandable and sufficiently documented where behavior is not immediately obvious.
- [ ] The documentation clearly explains the main workflow (i.e. the sequence of files used to produce results), distinguishes it from helper scripts, and describes the purpose of each file.
- [ ] The project is well structured and avoids spaghetti code.
- [ ] There is a clear separation between:
  - data loading
  - preprocessing
  - modeling / core logic
  - evaluation / visualization
- [ ] There is no dead code or abandoned experiments in the main branch.

### 2.2 Coding Style & Maintainability

- [ ] Naming conventions are consistent and meaningful.
- [ ] Code formatting is consistent (indentation, spacing, line length).
- [ ] Code repetition is avoided by using functions or reusable components.
- [ ] Variables are used appropriately instead of repeatedly hardcoding the same values.

### 2.3 Configuration & Parameters

- [ ] Values that may change are not hardcoded inside the code logic.
- [ ] Configurable values are declared at the top of scripts or loaded via configuration files or settings.
- [ ] Different datasets or experimental settings can be handled without modifying core code.

### 2.4 Documentation

- [ ] A README.md is present where necessary (e.g. per folder or module).
- [ ] The documentation clearly explains the purpose of the code.
- [ ] There are clear instructions on how to run the code.
- [ ] Required data is accessible (e.g. via OneDrive or a shared folder provided by the supervisors).

### 2.5 Version Control Hygiene

- [ ] Commit messages clearly describe what was changed (e.g. "Improved sorting function").
- [ ] Vague commit messages such as "changes to code" are avoided.
- [ ] A proper .gitignore file is used.
- [ ] Temporary, generated, or unnecessary files are not committed.

### 2.6 Reproducibility

- [ ] Random seeds are fixed where relevant.
- [ ] Dependencies are clearly specified (e.g. requirements.txt, environment.yml).
- [ ] Instructions are provided to recreate the software environment.

### 2.7 Testing & Validation (if applicable)

- [ ] Basic sanity checks are implemented.
- [ ] Critical functions are covered by unit tests where appropriate.
- [ ] Validation scripts or notebooks demonstrate correctness of results.

### 2.8 Performance Considerations

- [ ] Obvious inefficiencies (e.g. unnecessary loops or recomputation) are avoided.
- [ ] If inefficient code is unavoidable, trade-offs are clearly documented in comments.

## 3. Important Note

The code review focuses on code quality, structure, and maintainability, not on final research results. The code does not need to be final or perfect at this stage.
