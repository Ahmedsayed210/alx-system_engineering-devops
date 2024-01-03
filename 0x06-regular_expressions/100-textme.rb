#!/usr/bin/env ruby

from = ARGV[0].scan(/from:(.*?)\]/).flatten.first
to = ARGV[0].scan(/to:(.*?)\]/).flatten.first
flags = ARGV[0].scan(/flags:(.*?)\]/).flatten.first

puts "[#{from}], [#{to}], [#{flags}]"

