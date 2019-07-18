# Enhanced Livejournal export

This is a fork of [arty-name/livejournal-export](https://github.com/arty-name/livejournal-export) that aims to:

1. Update the code to a modern Python workflow
2. Add a bit more security so you can clone and commit to this repo without saving you credentials.

Thank you @arty-name. With your code, I can now preserve my embarrassing junior high and high school posts for modern platforms.

## Requirements

- Python 3
- Pipenv

## How to use this script

You'll need to add cookies from your Livejournal session to a `.env` file that's read in my `auth.py`. To do this:

1. Create a copy of `.env-template` and name it `.env` (`cp .env-template .env`)
2. Log into Livejournal with the account you want to archive
3. Open the web inspector in the browser
4. Click on the Network tab
5. Select the root HTML document (usually shown as `/` at the top of the network tab)
6. Click on Cookie
7. Copy the values from the web inspector into `.env`
8. Add the years you'd like to archive in `.env`
9. Run `make` from the command line

This will create several directories with the content from your Livejournal. You can now rest easy that no one will read your Dragon Ball Z fan fiction from 2006.

I looked through the original source code and didn't see any malicious code, but as a general rule, **you should never run code on your computer that you haven't looked through**. If you're paranoid, be sure to read through my source code as well as [the original](https://github.com/arty-name/livejournal-export).
