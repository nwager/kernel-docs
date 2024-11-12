# How to contribute to Kernel documentation

We believe that everyone has something valuable to contribute, whether you're a
coder, a writer, or a tester. Here's how and why you can get involved:

- **Why join us?** Work with like-minded people, develop your skills, connect
with diverse professionals, and make a difference.
- **What do you get?** Personal growth, recognition for your contributions,
early access to new features, and the joy of seeing your work appreciated.
- **Start early, start easy**: Dive into code contributions, improve
documentation, or be among the first testers. Your presence matters, regardless
of experience or the size of your contribution.

The guidelines below will help keep your contributions effective and meaningful.

## Code of conduct

When contributing, you must abide by the [Ubuntu Code of Conduct].

## Licence and copyright

By default, all contributions to Kernel documentation are licensed under the
Creative Commons Attribution-Share Alike (CC-BY-SA) 3.0 Unported License. To
view a copy of this license, visit http://creativecommons.org/licenses/by-sa/3.0/
or send a letter to Creative Commons, 171 Second Street, Suite 300, San
Francisco, California, 94105, USA.

All contributors must sign the [Canonical contributor licence agreement], which
grants Canonical permission to use the contributions. The author of a change
remains the copyright owner of their code (no copyright assignment occurs).

## Environment setup

Kernel documentation is built on top of [Canonical's Sphinx starter pack] and
hosted on [Read the Docs].

To work on the project, you will need to have Python, `python3.12-venv`, and
`make` packages installed.

```{code-block} console
sudo apt install make
sudo apt install python3
sudo apt install python3.12-venv
```

## Submissions

If you want to address and issue or bug in this project, leave a comment in the
issue indicating your intent to work on it. Also, reference the issue when you
submit the changes.

- (Kernel docs members) Create a branch off the `main` branch of the
[Kernel documentation GitHub repository] and add your changes to it.

- (External contributors) Fork the [Kernel documentation GitHub repository] and
add the changes to your fork.

- Properly structure your commits, provide detailed commit messages, and
{ref}`sign your commits <how-to-contribute-signed-commits>`.

- Make sure the updated project builds and runs without warnings or errors; this
includes linting, documentation, code (where applicable), and tests.

- Submit the changes as a [pull request (PR)].

Your changes will be reviewed in due time; if approved, they will eventually be
merged.

### Describing pull requests

To be properly considered, reviewed, and merged, your pull request must provide
the following details:

- **Title**: Summarise the change in a short, descriptive title.
- **Description**: Explain the problem that your pull request solves. Mention
any new features, bug fixes, or refactoring.
- **Relevant issues**: Reference any [related issues, pull requests, and repositories].
- **Testing**: Explain whether new or updated tests are included.
- **Reversibility**: If you propose decisions that may be costly to reverse,
list the reasons and suggest steps to reverse the changes if necessary.

### Commit structure and messages

Use separate commits for each logical change, and for changes to different
sections in the Kernel documentation.
Prefix your commit messages with the names of sections or pages that they
affect, using the code tree structure. For example, start a commit that updates
the explanation page about SRU cycles with `explanation/about-sru:`.

Use [conventional commits] to ensure consistency across the project:

```none
Update generic format for source package repository

* Added new URL structure details for Noble: https://github.com/canonical/kernel-docs/issues/12345
* Separate content for pre- and post-24.04 release
```

Such structure makes it easier to review contributions and simplifies porting
fixes to other branches.

(how-to-contribute-signed-commits)=
### Signing commits

All changes that go into the Kernel documentation repository require signed
commits (using the `-S` or `--sign-off` option).

```{code-block} console
git commit -S -m "explanation/about-sru: updated life cycle diagram"
```

Signed commits will have a GPG, SSH, or S/MIME signature that is
cryptographically verifiable, and will be marked with a "Verified" or
"Partially verified" badge in GitHub. This sign off verifies that you made the 
changes or have the right to commit it as an open-source contribution.

To set up locally signed commits and tags, see [GitHub Docs - About commit
signature verification].

````{tip}
Configure your Git client to sign commits by default for any local repository by
running:

```{code-block} console
git config --global commit.gpgsign true
```

See [GitHub Docs - Signing commits] for more information.
````

If you made an unsigned commit and encounter the "Commits must have verified
signatures" error when pushing your changes to remote:

1. Amend the most recent commit, add a signature without changing the commit
message, and push again:

   ```{code-block} console
   git commit --amend --no-edit -n -S
   git push
   ```

1. If you still encounter the same error, confirm that your GitHub account has
been set up properly to sign commits as described in the [GitHub Docs - About
commit signature verification].
   ```{tip}
   If you are using SSH keys to sign your commits, make sure that you added a
   "Signing Key" type in your GitHub account. See [GitHub Docs - Adding a new
   SSH key to your account] for more information.
   ```

<!--
## Code

### Formatting and linting

Kernel documentation relies on these formatting and linting tools:

- [TODO: Tool 1](http://example.com)
- [TODO: Tool 2](http://example.com)

To configure and run them:

```bash
TODO: lint command 1
TODO: lint command 2
```

### Structure

- **Check linked code elements**: Ensure coupled code elements, files, and directories are adjacent. For instance, store test data close to the corresponding test code.
- **Group variable declaration and initialisation**: Declare and initialise variables together to improve code organisation and readability.
- **Split large expressions**: Break down large expressions into smaller self-explanatory parts. Use multiple variables where appropriate to make the code more understandable and choose names that reflect their purpose.
- **Use blank lines for logical separation**: Insert a blank line between two logically separate sections of code to improve its structure and readability.
- **Avoid nested conditions**: Avoid nesting conditions to improve readability and maintainability.
- **Remove dead code and redundant comments**: Drop unused or obsolete code and comments to promote a cleaner code base and reduce confusion.
- **Normalise symmetries**: Treat identical operations consistently, using a uniform approach to improve consistency and readability.

### Best practices

## Tests

All code contributions must include tests.

To run the tests locally before submitting your changes:

```bash
TODO: test command 1
TODO: test command 2
```

## Documentation

Kernel documentation's documentation is stored in the `DOCDIR` directory of the repository. It is based on the [Canonical starter pack](https://canonical-starter-pack.readthedocumentation-hosted.com/latest/) and hosted on [Read the documentation](https://about.readthedocumentation.com/).

For general guidance, refer to the [starter pack guide](https://canonical-starter-pack.readthedocumentation-hosted.com/latest/).

For syntax help and guidelines, refer to the [Canonical style guides](https://canonical-documentation-with-sphinx-and-readthedocumentationcom.readthedocumentation-hosted.com/#style-guides).

In structuring, the documentation employs the [Diátaxis](https://diataxis.fr/) approach.

To run the documentation locally before submitting your changes:

```bash
make run
```

### Automatic checks

GitHub runs automatic checks on the documentation to verify spelling, validate links, and suggest inclusive language.

You can (and should) run the same checks locally:

```bash
make spelling
make linkcheck
make woke
```
-->

% LINKS
[Ubuntu Code of Conduct]: https://ubuntu.com/community/ethos/code-of-conduct
[Canonical contributor licence agreement]: https://ubuntu.com/legal/contributors
[Canonical's Sphinx starter pack]: https://github.com/canonical/sphinx-docs-starter-pack
[Read the Docs]: https://about.readthedocs.com/
[Kernel documentation GitHub repository]: https://github.com/canonical/kernel-docs
[pull request (PR)]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requestsproposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork
[related issues, pull requests, and repositories]: https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls
[conventional commits]: https://www.conventionalcommits.org/
[GitHub Docs - About commit signature verification]: https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification
[GitHub Docs - signing commits]: https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits
[GitHub Docs - Adding a new SSH key to your account]: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account#adding-a-new-ssh-key-to-your-account
