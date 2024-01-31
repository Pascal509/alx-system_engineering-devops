#!/usr/bin/env ruby
#Your script should output: [SENDER],[RECEIVER],[FLAGS]

log_entry = [
  "Sender: +123456789,
  Receiver: +987654321,
  Flags: A",
  "Sender: Alice, Receiver: Bob, Flags: B",
]

def extract_information(log_entry)
  # Define a regex pattern to extract relevant information
  pattern = /Sender: (\S+), Receiver: (\S+), Flags: (\S+)/

  # Use the pattern to match information in the log entry
  match = pattern.match(log_entry)

  # If a match is found, return the extracted information
  if match
    sender = match[1]
    receiver = match[2]
    flags = match[3]
    return sender, receiver, flags
  else
    return nil
  end
end

def process_log(log_entries)
  # Iterate through each log entry and extract information
  log_entries.each do |log_entry|
    result = extract_information(log_entry)

    # If information is found, print it in the required format
    if result
      sender, receiver, flags = result
      puts "#{sender},#{receiver},#{flags}"
    end
  end
end

# Process the log entries
process_log(log_entries)
