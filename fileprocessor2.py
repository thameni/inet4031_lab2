import sys

for line in sys.stdin:
    line = line.strip()

    if line.startswith('#'):
        print(f"{line} is skipped because it starts with a hashtag (is commented out)")
        continue
    user_infos = line.split(':')
    if len(user_infos) == 4:
        username, password, userid, groupid = user_infos
        print(f"The user {username} has a password of {password} and has {userid} and groupid {groupid}")
    else:
        print(f"{line} is skipped because there are no values")
print("\nEnd of User Data")
