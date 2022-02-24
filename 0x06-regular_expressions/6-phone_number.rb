#!/usr/bin/env ruby
# '^' Matches any string with n at the beginning of it.
#+ '\d' Find a digit.
puts ARGV[0].scan(/^\d{10}/).join
