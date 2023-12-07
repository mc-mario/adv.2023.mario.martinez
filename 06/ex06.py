import re
with open('data/input') as f:
    # times, records = list(
    #     map(lambda line:
    #         list(map(int, re.findall('\d+', line))),
    #         f.read().splitlines())
    # )
     times, records = list(map(lambda line: int(''.join(re.findall('\d+', line))),f.read().splitlines()))
     times, records = [times], [records]
record_beaten = 0
for c_time, c_record in zip(times, records):
    c_record_beaten = 0
    for wind_up in range(c_time+1):
        our_record = wind_up * (c_time-wind_up)
        if our_record > c_record:
            c_record_beaten += 1

    if record_beaten == 0:
        record_beaten = c_record_beaten
    else: record_beaten *= c_record_beaten

print(record_beaten)