# Conventional Commits

## Why you should use them?

- Conventional Commits encourages us to make more of certain types of commits such as fixes.
- Hack freely and make sense of your changes later.
- Let other people quickly understand, what your commit is about without looking at actual pushed changes.

## How to use them?

Links of official docs:
- [Dosc in english](https://www.conventionalcommits.org/en/v1.0.0/)
- [Dosc in russian](https://www.conventionalcommits.org/ru/v1.0.0/)

### Format
 
`<type>(optional scope): <description>`
Example: `feat(pre-event): add speakers section`
 
### 1. Type
 
Available types are:
 
- feat     → Changes about addition or removal of a feature. Ex: `feat: add table on landing page`, `feat: remove table from landing page`
- fix      → Bug fixing, followed by the bug. Ex: `fix: illustration overflows in mobile view`
- docs     → Update documentation (README.md)
- style    → Updating style, and not changing any logic in the code (reorder imports, fix whitespace, remove comments)
- chore    → Installing new dependencies, or bumping deps
- refactor → Changes in code, same output, but different approach
- revert   → When reverting commits
- perf     → Fixing something regarding performance (deriving state, using memo, callback)
- hotfix   → Fixing something in the master branch
 
### 2. Optional Scope
 
Labels per page Ex: `feat(pre-event): add date label`
 
**If there is no scope needed, you don't need to write it**
 
### 3. Description
 
Description must fully explain what is being done.
 
Add BREAKING CHANGE in the description if there is a significant change.
 
**If there are multiple changes, then commit one by one**
 
- After colon, there are a single space Ex: `feat: add something`
- When using `fix` type, state the issue Ex: `fix: file size limiter not working`
- Use imperative, and present tense: "change" not "changed" or "changes"
- Don't use capitals in front of the sentence
- Don't add full stop (.) at the end of the sentence

## This repo is an example of how to write conventional commit messages.

The structure od this repo is pretty simple.

We have main.py program that uses files from pkg to do some logic of:
- Calculating length of a line given its two points
- Calculating circle's square given its radius of `Line` class