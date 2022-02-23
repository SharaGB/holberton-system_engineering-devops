#!/usr/bin/ruby
# '\b' Find a match at the beginning/end of a word.
#+ '.' Find a single character.
puts ARGV[0].scan(/\bh.n\b/).join
