import re

def parse_iperf_output(output):
    pattern = re.compile(r'\[ *5\] *0.00-10.00\s+sec\s+([0-9.]+) [GMK]Bytes\s+([0-9.]+) [GMK]bits/sec\s+sender')

    
    match = pattern.search(output)

    if match:
        transfer = match.group(1)
        bitrate = match.group(2)
        return {
            'transfer': float(transfer),
            'bitrate': float(bitrate)
        }
    else:
        print("Failed to parse the output.")
        return None
