def transpose(data):
    output = []
    if isinstance(data, dict):
        keys = tuple(data.keys())
        values = tuple(data.values())
        output.extend((keys, values))
    else:
        names = []
        since_days = []
        karma_points = []
        bitecoin_earned = []
        for member in data:
            names.append(member.name)
            since_days.append(member.since_days)
            karma_points.append(member.karma_points)
            bitecoin_earned.append(member.bitecoin_earned)
        output.extend(
            (
                tuple(names),
                tuple(since_days),
                tuple(karma_points),
                tuple(bitecoin_earned),
            )
        )

    return output
