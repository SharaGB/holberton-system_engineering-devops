#!/usr/bin/env ruby
# Match with the range of 't', repeated 2, 3, 4 or 5 times.
puts ARGV[0].scan(/hbt{2,5}n/)
