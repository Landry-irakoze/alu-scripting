# Regular Expressions

Project built with Ruby regular expressions using the Oniguruma engine
(Ruby's default regex library).

Each task is a standalone Ruby script that takes one command-line
argument, runs it through `String#scan` with a specific regex, and
prints the joined result.

## Requirements
- Ubuntu 20.04 LTS
- Ruby (uses `/usr/bin/env ruby`)
- All scripts are executable and start with `#!/usr/bin/env ruby`

## Tasks

| File | Description |
|---|---|
| `0-simply_match_school.rb` | Matches the literal string `School` |
| `1-repetition_token_0.rb` | Matches `hbt` followed by zero or more `n` (`hbtn*`) |
| `2-repetition_token_1.rb` | Matches `hbt` followed by one or more `n` (`hbtn+`) |
| `3-repetition_token_2.rb` | Matches `hbt` followed by zero or one `n` (`hbtn?`) |
| `4-repetition_token_3.rb` | Matches `hbt` followed by exactly two `n` (`hbtn{2}`), no square brackets used |
| `5-beginning_and_end.rb` | Matches a string that starts with `h`, ends with `n`, with exactly one character in between |
| `6-phone_number.rb` | Matches an exact 10-digit phone number (no spaces or dashes) |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | Extracts only capital letters from a string |
| `8-textme.rb` | Parses a TextMe log line and outputs `SENDER,RECEIVER,FLAGS` |

## Usage

```bash
./0-simply_match_school.rb "Best School"
```

## Author
Landry - ALU

