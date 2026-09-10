# Week 1 — Python Foundations

This folder contains my Week 1 Python learning journey.

The goal of Week 1 is not just to complete Python exercises, but to build one small application step by step while learning the fundamentals of Python and Git/GitHub.

## Project: LinkNest

**LinkNest** is a basic command-line bookmark manager.

The application allows a user to save and manage useful web bookmarks from the terminal.

Each bookmark contains:

- ID
- Title
- URL
- Category

The project will gradually evolve as I learn new Python concepts.

---

## Learning Approach

Instead of building multiple unrelated Python exercises, I am using one evolving project throughout the learning process.

The progression is:

```text
Python Basics
     ↓
LinkNest CLI
     ↓
Functions
     ↓
Validation & Error Handling
     ↓
Object-Oriented Programming
     ↓
File / JSON Persistence
     ↓
Testing
     ↓
API Development
     ↓
Future Application Improvements
```

The application will become more structured as my Python knowledge improves.

---

# Day 1 — Basic Bookmark Manager

## Objective

Build a simple command-line bookmark manager using fundamental Python concepts.

The focus of Day 1 is understanding how Python variables, lists, dictionaries, conditions, and loops work together to create a small interactive application.

## Features

The current application supports:

- Add a new bookmark
- View saved bookmarks
- Search for a bookmark by title
- Delete a bookmark by title
- Exit the application
- Handle invalid menu options
- Generate a simple numeric ID for each bookmark

## Bookmark Structure

Each bookmark is represented using a Python dictionary:

```text
{
    "_id": 1,
    "title": "Python",
    "url": "https://python.org",
    "Category": "Learning"
}
```

Multiple bookmarks are stored inside a Python list.

```text
Bookmarks
    ├── Bookmark 1
    ├── Bookmark 2
    ├── Bookmark 3
    └── ...
```

---

## Python Concepts Practiced

Day 1 focuses on:

- `print()`
- `input()`
- Variables
- Strings
- Integers
- Lists
- Dictionaries
- `if`
- `elif`
- `else`
- `while`
- `for`
- `break`
- `.append()`
- `.remove()`
- `.get()`

---

## Current Application Flow

```text
Start Application
       ↓
Display Welcome Message
       ↓
Display Menu
       ↓
User Selects Option
       ↓
┌──────────────────────────┐
│ 1. Add Bookmark          │
│ 2. View Bookmarks        │
│ 3. Search Bookmark       │
│ 4. Delete Bookmark       │
│ 5. Exit                  │
└──────────────────────────┘
       ↓
Perform Selected Operation
       ↓
Return to Menu
       ↓
Continue Until Exit
```

---

## Day 1 Limitations

The current version intentionally has some limitations because this is a beginner learning project.

- Bookmarks are stored only in memory.
- Closing the application removes all saved bookmarks.
- Search is based on title.
- Delete is based on title.
- No database is used.
- No JSON/file storage is used.
- No classes are used.
- No external libraries are used.
- No API is used.
- No automated tests are included yet.

These limitations will be addressed gradually in later stages of the project.

---

## Day 1 Testing Checklist

Before considering Day 1 complete, the following scenarios should work:

- [x] Start the application
- [x] Display the menu
- [x] Add one bookmark
- [x] Add multiple bookmarks
- [x] View saved bookmarks
- [x] Search for an existing bookmark
- [x] Search for a non-existing bookmark
- [x] Delete an existing bookmark
- [x] Try deleting a non-existing bookmark
- [x] Handle an invalid menu option
- [x] Exit the application

---

# Day 2 — Planned Learning

Day 2 will focus on improving the structure of the Day 1 program.

The main goal is to introduce **functions** and divide the application into smaller responsibilities.

Instead of having all application logic inside one large `while` loop, the application will gradually move toward:

```text
Main Program
     │
     ├── Add Bookmark
     ├── View Bookmarks
     ├── Search Bookmark
     ├── Delete Bookmark
     └── Display Menu
```

## Day 2 Learning Goals

- Understand why functions are useful.
- Create functions using `def`.
- Pass information into functions using parameters.
- Return information using `return`.
- Reduce repeated code.
- Give each function one clear responsibility.
- Improve the readability of the existing LinkNest code.
- Keep the application behavior the same while improving its structure.

Day 2 is primarily a **refactoring exercise** rather than adding many new features.

---

# Git & GitHub Learning

This repository is also being used to practice Git and GitHub.

The objective is to maintain meaningful commits instead of uploading everything at once.

Example progression:

```text
Day 1
  ↓
Initial LinkNest application
  ↓
Fix multiple bookmark handling
  ↓
Add search
  ↓
Add delete
  ↓
Improve display
  ↓
Day 1 complete
```

Example commit messages:

```text
feat: create basic LinkNest bookmark manager
feat: support multiple bookmarks
feat: add bookmark search
feat: add bookmark deletion
refactor: improve bookmark display
docs: add Week 1 README
```

The commit history should show how the application evolved and what was learned at each stage.

---

# Learning Journal

For each day, I will track:

- What I learned
- What I built
- Problems I faced
- How I solved them
- Python concepts used
- Git/GitHub concepts practiced
- What I will learn next

The purpose is to make this repository a record of my learning progress, not just a collection of completed code.

---

# Week 1 Goal

By the end of Week 1, LinkNest should demonstrate a solid understanding of Python fundamentals and provide a foundation for future development.

The long-term goal is to evolve LinkNest from a simple CLI application into a more structured application as new Python concepts are learned.

---

## Repository

GitHub repository:

`Python_Basic`

Week 1:

`Week1/`

Project:

`LinkNest`